import pytest
from httpx import Response

from goodway_configs.base import ConfigsError
from goodway_configs.etcd_loader import EtcdConfigLoader

HTTPS_BASE_URL = 'https://localhost:1234'
HTTP_BASE_URL = 'http://localhost:1234'


@pytest.mark.respx()
async def test_load_config(respx_mock):
    respx_mock.post(
        f'{HTTPS_BASE_URL}/v3/kv/range',
        json={
            'key': 'Zm9v',
        },
    ).mock(
        return_value=Response(
            status_code=200,
            json={
                'headers': {
                    'cluster_id': '14841639068965178418',
                    'member_id': '10276657743932975437',
                    'raft_term': '3',
                    'revision': '3',
                },
                'kvs': [
                    {
                        'key': 'Zm9v',
                        'value': 'ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAxOTk1Cn0=',
                        'mod_revision': '3',
                        'create_revision': '2',
                        'version': '2',
                    },
                ]
            }
        )
    )

    loader = EtcdConfigLoader(
        host='localhost',
        port=1234,
        username=None,
        password=None,
        use_ssl=True,
        key='foo',
    )

    config = await loader.load_config()

    assert config == {
        "key1": "value1",
        "key2": 1995
    }


@pytest.mark.respx()
async def test_load_config_not_found(respx_mock):
    respx_mock.post(
        f'{HTTP_BASE_URL}/v3/kv/range',
        json={
            'key': 'Zm9v',
        },
    ).mock(
        return_value=Response(
            status_code=200,
            json={
                'headers': {
                    'cluster_id': '14841639068965178418',
                    'member_id': '10276657743932975437',
                    'raft_term': '3',
                    'revision': '3',
                }
            }
        )
    )

    loader = EtcdConfigLoader(
        host='localhost',
        port=1234,
        username=None,
        password=None,
        use_ssl=False,
        key='foo',
    )

    with pytest.raises(ConfigsError):
        await loader.load_config()


@pytest.mark.respx()
async def test_load_config_with_auth(respx_mock):
    respx_mock.post(
        f'{HTTPS_BASE_URL}/v3/kv/range',
        json={
            'key': 'Zm9v',
        },
    ).mock(
        return_value=Response(
            status_code=200,
            json={
                'headers': {
                    'cluster_id': '14841639068965178418',
                    'member_id': '10276657743932975437',
                    'raft_term': '3',
                    'revision': '3',
                },
                'kvs': [
                    {
                        'key': 'Zm9v',
                        'value': 'ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAxOTk1Cn0=',
                        'mod_revision': '3',
                        'create_revision': '2',
                        'version': '2',
                    },
                ]
            },
            headers={
                'Authorization': 'Basic myuser:p@ssword'
            }
        )
    )

    loader = EtcdConfigLoader(
        host='localhost',
        port=1234,
        username='mahdi',
        password='p@ssword',
        use_ssl=True,
        key='foo',
    )

    config = await loader.load_config()

    assert config == {
        "key1": "value1",
        "key2": 1995
    }
