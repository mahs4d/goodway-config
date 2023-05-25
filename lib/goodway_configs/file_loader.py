import json
from pathlib import Path

import yaml

from goodway_configs.base import ConfigLoaderBase, ConfigsError


class FileConfigLoader(ConfigLoaderBase):
    """ConfigLoader implementation that loads config from files."""

    def __init__(self, file_path: Path):
        super().__init__()

        self.file_path = file_path

    async def load_config(self) -> dict:
        """Load config from a file."""
        if not self.file_path.exists():
            raise ConfigsError(f'File not found: `{self.file_path}`!')

        if self.file_path.suffix in {'.json'}:
            return json.loads(self.file_path.read_text())

        if self.file_path.suffix in {'.yaml', '.yml'}:
            return yaml.safe_load(self.file_path.read_text())

        raise ConfigsError(f'Unsupported config file format: `{self.file_path.suffix}`!')
