# Base

Config loaders are used for loading configuration from different places. All loaders inherit from `ConfigLoader` class
and override the `load_config`. This function returns a dictionary containing the loaded config.
