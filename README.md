[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![license](https://img.shields.io/github/license/reitzig/espanso-nice-dev-refs.svg)](https://github.com/reitzig/espanso-nice-dev-refs/main/LICENSE)
[![GitHub release date](https://img.shields.io/github/tag-date/reitzig/espanso-nice-dev-refs.svg)](https://github.com/reitzig/espanso-nice-dev-refs/tags)
[![Test](https://github.com/reitzig/espanso-nice-dev-refs/actions/workflows/python-test.yml/badge.svg)](https://github.com/reitzig/espanso-nice-dev-refs/actions/workflows/python-test.yml)
[![CodeQL](https://github.com/reitzig/espanso-nice-dev-refs/actions/workflows/codeql.yml/badge.svg)](https://github.com/reitzig/espanso-nice-dev-refs/actions/workflows/codeql.yml)

# Nice Developer References – an espanso package

A package for [espanso/espanso](https://github.com/espanso/espanso).

Takes URLs from the clipboard and inserts a formatted link based on it.

## Usage

➡️ [nice-dev-refs](nice-dev-refs/README.md)

## Installation

Requirements: Python >= 3.9

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

🥳 Support for additional URL patterns is welcome –
unless and until replace performance decreases too much.
To limit the scope _somewhat_,
let's stick to things you link to _all the time_ in software development.

Whether you want to fix a bug or add a feature,

- add at least one (red) test,
- make it green,
- make sure `ruff` does not complain, and
- create a PR.

> ℹ️ While the code structure is simple in its spaghettific glory,
>    the construction of and interaction between the different 
>    regexps is definitely bespoke.
>    The approach here is to tame weird code with tests;
>    if there is no test for any given URL schema, 
>    the behaviour is undefined.
>    If your change does not break any tests, go for it!

## Development

Prepare a checkout of your fork:

```shell
mise install # if you want to
uv sync
# activate .venv
```

Now you should be able to run the relevant commands:

```shell
ruff format . # formatting
ruff check .  # linting
pytest        # testing
```

For convenience, there are also

```shell
poe lint
poe test
```

We include configuration for
    [evilmartians/lefthook](https://github.com/evilmartians/lefthook)
which we encourage you to use:

```bash
lefthook install
```

We also consider
    [direnv/direnv](https://github.com/direnv/direnv)
to be inherently useful,
and therefore include our
    [`.envrc`](.envrc).
