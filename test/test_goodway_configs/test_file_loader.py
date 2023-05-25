from pathlib import Path

import pytest

from goodway_configs.base import ConfigsError
from goodway_configs.file_loader import FileConfigLoader


async def test_load_config_json():
    loader = FileConfigLoader(file_path=Path(__file__).parent / Path('./data/config.json'))

    config = await loader.load_config()

    assert config == {
        'key1': 'value1',
        'key2': 12345,
    }


async def test_load_config_yaml():
    loader = FileConfigLoader(file_path=Path(__file__).parent / Path('./data/config.yaml'))

    config = await loader.load_config()

    assert config == {
        'key1': 'value1',
        'key2': 54321,
    }


async def test_load_config_unsupported_format_error():
    loader = FileConfigLoader(file_path=Path(__file__).parent / Path('./data/config.toml'))

    with pytest.raises(ConfigsError):
        await loader.load_config()


async def test_load_config_file_not_found_error():
    loader = FileConfigLoader(file_path=Path(__file__).parent / Path('./data/missing.json'))

    with pytest.raises(ConfigsError):
        await loader.load_config()
