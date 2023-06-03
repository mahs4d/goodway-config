# Multi Loader

`MultiConfigLoader` class can be used to combine configuration from multiple config loaders in an incremental way.

## Installation

`pip install goodway-configs`

## Usage

```python
from pathlib import Path

from goodway_configs.config_loader.json_loader import JsonConfigLoader
from goodway_configs.config_loader.multi_loader import MultiConfigLoader

loader = MultiConfigLoader(config_loaders=[
    JsonConfigLoader(file_path=Path('./config1.json')),
    JsonConfigLoader(file_path=Path('./config2.json')),
])

config = await loader.load_config()
```
