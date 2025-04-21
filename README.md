# Python Deep Dive
This repo will be used to explore the content of the book "Fluent Python" and learning the specifics and quirks of the Python language in detail

## Cloning the repo to your local

You should start by cloning this repo to your local machine. You can do that by running:

```bash
git clone https://github.com/micheldc55/python_deep_dive.git
cd python-deep-dive
```

## Environment Setup and Usage

Below are the instructions to set up the environment correctly and run the code. This project uses uv to manage the environment and dependencies, so first thing is to install it.

### Prerequisites
```bash
pip install uv
```

### Virtual Environment Setup

Create a virtual environment using the `.venv` directory alias and activate it.

```bash
uv venv .venv
source .venv/bin/activate
```

If you happen to have a different version of python installed, you need to specify the python version to use.

```bash
uv venv --python 3.11 .venv
```

If this fails, you probably need to go to the `uv` website and follow the instructions to install a specific python version on point uv to use that version.

### Install Dependencies

```bash
uv sync
```

### Environment Activation

**MacOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### Running project Files

With the environment activated, you can run the project files by running the files with the python interpreter. An example of how to run the `pattern_matching.py` file is:

```bash
python data_structures/pattern_matching.py
```

You can also use uv to run the files. This will use the python version specified in the `.venv` directory. This is useful if you want to run the files without activating the environment.

```bash
uv run python data_structures/pattern_matching.py
```

### Adding Dependencies

If you need to add a dependency, you can do so by running:

```bash
uv add package_name
```


### Running Marimo Notebooks

Marimo is a modern tool for creating and sharing data apps. It's a great tool for building notebooks both for prototyping and reporting.

To run a marimo notebook, you can use the following command:

```bash
marimo run your_notebook.py
```

### Requirements
- Python >=3.11
- marimo >=0.13.0
- numpy >=2.2.5
- pandas >=2.2.3
