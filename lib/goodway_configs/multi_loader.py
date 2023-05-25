from pydantic.utils import deep_update

from goodway_configs.base import ConfigLoaderBase


class MultiConfigLoader(ConfigLoaderBase):
    """ConfigLoader implementation that combines config from multiple config loaders."""

    def __init__(self, config_loaders: list[ConfigLoaderBase]):
        super().__init__()

        self.config_loaders = config_loaders

    async def load_config(self) -> dict:
        """Load config from a file."""
        config = {}

        for config_loader in self.config_loaders:
            config_update = await config_loader.load_config()
            config = deep_update(config, config_update)

        return config
