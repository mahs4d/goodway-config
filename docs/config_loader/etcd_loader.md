# Etcd Loader

`EtcdConfigLoader` class can be used to load configuration from etcd.

## Installation

`pip install goodway-configs[etcd-loader]`

## Usage

```python
from goodway_configs.config_loader.etcd_loader import EtcdConfigLoader

loader = EtcdConfigLoader(
    host='localhost',
    port=2379,
    username='user',
    password='p@ssword',
    use_ssl=True,
    key='path/to/config'
)

config = await loader.load_config()
```

!!! note
    `EtcdConfigLoader` is using etcd grpc proxy server. The default port for it is 2379.

### Usage without Auth

You can pass `None` for `username` and `password` to skip authentication.

```python
from goodway_configs.config_loader.etcd_loader import EtcdConfigLoader

loader = EtcdConfigLoader(
    host='localhost',
    port=2379,
    username=None,
    password=None,
    use_ssl=True,
    key='path/to/config'
)
```
