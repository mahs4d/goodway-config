# Json Loader

`JsonConfigLoader` class can be used to load configuration from json files.

## Installation

`pip install goodway-configs`

## Usage

```python
from pathlib import Path

from goodway_configs.config_loader.json_loader import JsonConfigLoader

loader = JsonConfigLoader(
    file_path=Path('./config.json'),
)

config = await loader.load_config()
```
