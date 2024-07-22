# Python Package Templates
## Table of Contents
1. [Overview](#overview)
2. [Running Tests](#tests)

## Overiew <a name="overview"></a>
This repository contains three sample project templates to help you get started with Python Packaging. `setuptools_template` covers the traditional setuptools approach, while `pyproject_setuptools_template` and `pyproject_hatchling_template` covers the modern pyproject.toml approach. 

`pyproject_setuptools_template` -> uses the setuptools build backend <br>
`pyproject_hatchling_template` -> uses the hatchling build backend 

## Running Tests <a name="tests"></a>
Tests can be run using the bash script inside the `./tests` folder
```bash
$ pytest tests/run_test.sh
```
