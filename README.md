[![PyPI version](https://badge.fury.io/py/pytest-kasima.svg)](https://badge.fury.io/py/pytest-kasima)
[![Python Versions](https://img.shields.io/pypi/pyversions/pytest-kasima.svg)](https://pypi.org/project/pytest-kasima)

# pytest-kasima

![normal](https://github.com/k4sima/pytest-kasima/blob/main/screenshots/normal.png?raw=true)

## install

```
pip install pytest-kasima
```

If you're a fan of [rich library](https://github.com/Textualize/rich), can integrate

![with_rich](https://github.com/k4sima/pytest-kasima/blob/main/screenshots/rich.png?raw=true)

```
pip install pytest-kasima[rich]
```

## usage

Display horizontal lines above and below the captured standard output for easy viewing.

`--capture=no` or `-s` option is not required.

### options

- `--kasima-skip` - If you don't like this plugin, disable it :smiley:
- `--kasima-rich-skip` - Skip the rich integration
