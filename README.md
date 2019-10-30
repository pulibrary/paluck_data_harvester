# Article Metadata Harvesting for B.P.

[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://img.shields.io/badge/python-3.7-yellow.svg)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-orange.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Getting Started

You'll need an [Elsevier API key](https://dev.elsevier.com/apikey/manage). Export it as an environment variable named `ELSEVIER_API_KEY`:

```
$ export ELSEVIER_API_KEY=<my key>
```

You may want to put this in your `~/.bash_profile` to avoid having to set in in each terminal session.

### Installation for Running Queries

Use Python 3.7 or greater.

If you do not want to develop the code and just need to run queries, install the dependencies with:

```
$ pip install -r requirements.txt
```

Then have a look at `main.py`.

### Installation for Development

NB: on OS 10.X you'll need xcode: `$ xcode-select --install`

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
To keep `requirements.txt` in sync (run this after any dependency changes), do:
```
$ pipenv lock -r > requirements.txt
```
To update all dependencies:
```
$ pipenv update --outdated
```
Keep your environment tidy by occasionally running:
```
$ pipenv clean
```

Call `pipenv --help` or `pipenv <subcommand> --help` or see [the docs](https://github.com/pypa/pipenv#-usage) for details.

### Style

When in doubt, run [Black](https://black.readthedocs.io/en/stable/index.html):
```
$ pipenv run black -t py37 -l 79 main.py api/
```

Follow [Google's Style Guide](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings.

## License

BSD 3-Clause. See [LICENSE](LICENSE).

Note well that the use of content provided by Elsevier is subject to [their terms](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions), including the terms to which you agreed when generating your API key (and copied into the [`elsevier_api_terms`](elsevier_api_terms) directory of this repository for convenience).
