from goodway_configs.config_loader.base import ConfigLoaderBase
from goodway_configs.config_loader.multi_loader import MultiConfigLoader


class DummyConfigLoader(ConfigLoaderBase):
    def __init__(self, config: dict):
        self.config = config

    async def load_config(self) -> dict:
        return self.config


async def test_load_config():
    loader = MultiConfigLoader(
        config_loaders=[
            DummyConfigLoader(config={
                'a': 1,
                'b': {
                    'c': 2,
                },
                'd': 3,
            }),
            DummyConfigLoader(config={
                'a': 12,
                'b': {
                    'e': 13,
                },
                'f': 15,
            }),
        ]
    )

    config = await loader.load_config()

    assert config == {
        'a': 12,
        'b': {
            'c': 2,
            'e': 13,
        },
        'd': 3,
        'f': 15,
    }
