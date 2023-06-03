# Yaml Loader

`YamlConfigLoader` class can be used to load configuration from yaml files.

## Installation

`pip install goodway-configs[yaml-loader]`

## Usage

```python
from pathlib import Path

from goodway_configs.config_loader.yaml_loader import YamlConfigLoader

loader = YamlConfigLoader(
    file_path=Path('./config.yaml'),
)

config = await loader.load_config()
```
