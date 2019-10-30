# Article Metadata Harvesting for B.P.

[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://img.shields.io/badge/python-3.7-yellow.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Getting Started

You'll need an [Elsevier API key](https://dev.elsevier.com/apikey/manage). Export it as an environment variable named `ELSEVIER_API_KEY`:

```
$ export ELSEVIER_API_KEY=<my key>
```

You may want to put this in your `~/.bash_profile` to avoid having to set in in each terminal session.

### Installation and Dependencies

N.B., on OS 10.X you'll need xcode: `$ xcode-select --install`

[`pipenv`](https://github.com/pypa/pipenv#installation) is used for development/debugging. After cloning, do:
```
$ pipenv --python 3.7
$ pipenv install
```
You should only need to do this the first time. Then:

To run a script, do:
```
$ pipenv run python <my_script>
```
To add a dependency (add `--dev` and `--pre` as necessary):
```
$ pipenv install <my_dep>
```
To remove a dependency:
```
$ pipenv uninstall <my_dep>
```
To update all dependencies:
```
$ pipenv update --outdated
```
Keep your environment tidy by occasionally running:
```
$ pipenv clean
```
If you need a `requirements.txt`, generate and keep it up to date with:
```
$ pipenv lock -r > requirements.txt
```

Call `pipenv --help` or `pipenv <subcommand> --help` or see [the docs](https://github.com/pypa/pipenv#-usage) for details.

### Style

When in doubt, run [Black](https://black.readthedocs.io/en/stable/index.html)

```
$ pipenv run black -t py37 -l 79 .
```

## License

### Elsevier

Use of content provided by Elsevier is subject to [their terms](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions), including the terms to which you agreed when generating your API key (and copied into the [`elsevier_api_terms`](elsevier_api_terms) directory of this repository for convenience.)

### Code

MIT. See [LICENSE](LICENSE)
