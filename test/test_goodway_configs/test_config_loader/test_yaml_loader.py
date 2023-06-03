from pathlib import Path

import pytest

from goodway_configs.config_loader.base import ConfigsError
from goodway_configs.config_loader.yaml_loader import YamlConfigLoader


async def test_load_config():
    loader = YamlConfigLoader(file_path=Path(__file__).parent / Path('data/config.yaml'))

    config = await loader.load_config()

    assert config == {
        'key1': 'value1',
        'key2': 54321,
    }


async def test_load_config_file_not_found_error():
    loader = YamlConfigLoader(file_path=Path(__file__).parent / Path('./data/missing.json'))

    with pytest.raises(ConfigsError):
        await loader.load_config()
