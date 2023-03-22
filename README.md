# URL referencing rules for espanso

## Usage

TODO

## Installation

```shell
mkdir -p ~/.config/espanso/scripts/
ln -s (realpath .)/scripts/*.py ~/.config/espanso/scripts/
ln -s (realpath .)/match/*.yml ~/.config/espanso/match/
```

For more selective application refer to [Include and Exclude rules](https://espanso.org/docs/configuration/include-and-exclude/)

## Development

```shell
python3 -m venv .venv
(if not direnv: activate venv)
pip install -r test/requirements.txt

flake8
pytest
```