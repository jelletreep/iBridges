# iBridges
[![PyPI version](https://badge.fury.io/py/ibridges.svg)](https://badge.fury.io/py/ibridges)
[![](https://github.com/UtrechtUniversity/iBridges/actions/workflows/integration-tests-irods.yml/badge.svg?branch=develop)](https://github.com/UtrechtUniversity/iBridges/actions/workflows/integration-tests-irods.yml) [![](https://github.com/UtrechtUniversity/iBridges/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/UtrechtUniversity/iBridges/actions/workflows/main.yml) 
[![](https://github.com/UtrechtUniversity/iBridges/actions/workflows/integration-tests-yoda.yml/badge.svg)](https://github.com/UtrechtUniversity/iBridges/actions/workflows/integration-tests-yoda.yml) ![](https://readthedocs.org/projects/ibridges/badge/?version=latest&style=flat-default)

iBridges is a library for scientific programmers who are working with data in [iRODS](https://irods.org/). We provide a wrapper around the [python-irodsclient](https://pypi.org/project/python-irodsclient/) to facilitate easy interaction with iRODS. iBridges is currently still in very active development.


## Highlights

- Works on Windows, Mac OS and Linux
- Runs on Python 3.8 or higher.
- Supported iRODS server versions: 4.2.11 or higher and 4.3.0 or higher.
- **Interactive connection** to your iRods server.
- **Upload** and **Download** your data.
- Manipulate the **metadata** on the iRODS server.
- **Synchronize** your data between your local computer and the iRODS server.
- Create and manipulate **Tickets** to temporarily grant access to outside users.
- **Search** through all metadata for your dataset or collection.
- Small number of dependencies (`python-irodsclient` and `tqdm`)
- Safe default options when working with your data.


 <p align="center">
    <a href="https://github.com/UtrechtUniversity/iBridges/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=%5BBUG%5D">Report Bug</a>
    .
    <a href="https://github.com/UtrechtUniversity/iBridges/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=%5BFEATURE%5D">Request Feature</a>
    .
    <a href="https://github.com/UtrechtUniversity/iBridges/discussions/categories/ideas">Share an idea</a>
    .
    <a href="https://github.com/UtrechtUniversity/iBridges/discussions/categories/general">Leave some feedback</a>
    .
    <a href="https://github.com/UtrechtUniversity/iBridges/discussions/categories/q-a">Ask a question</a>
  </p>
</p>

## Installation

iBridges is installed using `pip`([get started with pip](https://pip.pypa.io/en/stable/getting-started/)). The recommended way is to use the stable version that is available on PyPi:

```bash
pip install ibridges
```

If you want to install the unstable version to test out new features, you can install the development branch:

```bash
pip install git+https://github.com/UtrechtUniversity/iBridges.git@develop
```

## Usage

Below are some basic examples of the features in iBridges.

```py
# Create an iRODS session
from ibridges import Session

session = Session(irods_env_path="~/.irods/irods_environment.json", password="mypassword")

# Upload files or directories
from ibridges import upload

upload(session, "/your/local/path", "/irods/path")

# Download files or directories/collections
from ibridges import download

download(session, "/irods/path", "/other/local/path")

```

## Tutorials
### Documentation
- **[ReadTheDocs](https://ibridges.readthedocs.io/en/latest/)**

### Guides
- [QuickStart](tutorials/QuickStart.ipynb)
- [Working with iRODS Paths](tutorials/iRODS_paths.ipynb)
- [Data synchronisation](tutorials/Data_sync.ipynb)

### Beginners tutorials
- [Setup and connect to iRODS](tutorials/01-Setup-and-connect.ipynb)
- [Working with data](tutorials/02-Working-with-data.ipynb)
- [Introduction to iRODS and local Paths](tutorials/03-iRODS-Paths.ipynb)
- [Working with Metadata](tutorials/04-Metadata.ipynb)
- [Sharing data](tutorials/05-Data-Sharing.ipynb)

## Authors

**Christine Staiger (Maintainer) [ORCID](https://orcid.org/0000-0002-6754-7647)**

- *Wageningen University & Research* 2021 - 2022
- *Utrecht University* 2022

**Tim van Daalen**, *Wageningen University & Research* 2021

**Maarten Schermer (Maintainer) [ORCID](https://orcid.org/my-orcid?orcid=0000-0001-6770-3155)**, *Utrecht University* 2023

**Raoul Schram (Maintainer) [ORCID](https://orcid.org/my-orcid?orcid=0000-0001-6616-230X)**. 
*Utrecht University* 2023

## Contributors

**J.P. Mc Farland**,
*University of Groningen, Center for Information Technology*, 2022

## How to contribute
We are very happy with any suggestions or contributions to improve the contents. 

### Issues
The easiest way to contribute is to submit an [issue](https://github.com/UtrechtUniversity/iBridges/issues), and describe abug, typos or any other suggestions or request a new feature.

### Let us and the community know
If you have interesting use cases for iBridges, you want to show how you used iBridges etc please let us and the community know! We are always interested! You can do so in the [Discussions](https://github.com/UtrechtUniversity/iBridges/discussions/categories/general).

### Pull requests
If you are comfortable with git and pull requests, you can also submit a pull request where you directly suggest changes to the content. Read more about how pull requests work [here](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github).

In short:

1. Fork the repository and clone it locally.
2. Create a new branch in your desktop copy of this repository.
3. Commit the change in that branch.
4. Push that branch to your fork of this repository on GitHub
5. Submit a pull request from that branch to the main branch of the master repository. 
6. If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.

## License
This project is licensed under the MIT license.
The full license can be found in [LICENSE](LICENSE).
