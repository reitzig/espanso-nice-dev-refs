# Nice Developer References -- an espanso package

A package for [espanso/espanso](https://github.com/espanso/espanso).

Takes URLs from the clipboard and inserts a formatted link based on it.

## Usage

➡️ [nice-dev-refs](nice-dev-refs/README.md)

## Installation

Requirements: Python >= 3.8

Unfortunately, we have to perform the installation 
with a _little_ bit more finger-grease as we are used to 
([Discussion](https://github.com/espanso/espanso/discussions/1558)):

```bash
# cd anywhere/you/want
git clone git@github.com:reitzig/espanso-nice-dev-refs.git
cd espanso-nice-dev-refs

espanso install nice-dev-refs --git "$(realpath "$(pwd)")" --external

mkdir -p ~/.config/espanso/scripts/
ln -s "$(realpath "$(pwd)")"/scripts/*.py ~/.config/espanso/scripts/
```

For more selective application refer
to [Include and Exclude rules](https://espanso.org/docs/configuration/include-and-exclude/)


## Contributing

🥳 Support for additional URL patterns is welcome --
unless and until replace performance decreases too much.
To limit the scope _somewhat_, 
let's stick to things you link to _all the time_ in software development.

Whether you want to fix a bug or add a feature,
- add at least one (red) test,
- make it green, 
- make sure `flake8` does not complain, and
- create a PR.


## Development

<!-- TODO: add devenv / devcontainer -->

Prepare a checkout of your fork:
```shell
python3 -m venv .venv
direnv allow # cf. .envrc
# or activate .venv and set PYTHONPATH yourself
pip install -r test/requirements.txt
```

Now you should be able to run the relevant commands:
```shell
flake8 # linting
pytest # testing
```
