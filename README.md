<a href="url"><img src="https://team5419.org/wp-content/uploads/2021/08/Artboard-7-copy-3@4x-1.png" height="180" width="410" ></a>

# itemSorter

MAPPS (Multipurpose Automatic Partitioned Sorting Solution) is a custom workspace organization management software designed for use by the Berkelium robotics team.

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/team5419/MAPSS.git
```
Install dependancies:

(Using a virtual environment is recomended. Also make sure you are running python 3)

You will need [Flask](https://pypi.org/project/Flask/), [Google API Client](https://pypi.org/project/google-api-python-client/), [GitPython](https://pypi.org/project/GitPython/), and [configparser](https://pypi.org/project/configparser/)

```bash
pip3 install Flask google-api-python-client GitPython configparser
```

## Running

```bash
python3 readSheet.py
```

You should then go to [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/) in your web browser.

## Contributing

Internal users should make a branch and then a pull request to merge your changes. External users can do the same but start by making a fork. If you dont know how to fix your problem, [make an issue](https://github.com/lemmaammel/itemSorter/issues/new) and a kind coder can help you.