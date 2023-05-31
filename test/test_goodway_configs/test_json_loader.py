from pathlib import Path

import pytest

from goodway_configs.base import ConfigsError
from goodway_configs.json_loader import JsonConfigLoader


async def test_load_config_json():
    loader = JsonConfigLoader(file_path=Path(__file__).parent / Path('./data/config.json'))

    config = await loader.load_config()

    assert config == {
        'key1': 'value1',
        'key2': 12345,
    }


async def test_load_config_file_not_found_error():
    loader = JsonConfigLoader(file_path=Path(__file__).parent / Path('./data/missing.json'))

    with pytest.raises(ConfigsError):
        await loader.load_config()
