# CodeLog

CodeLog is a simple, custom version control system (VCS) built in Python. It allows users to track changes in their codebase, similar to other VCS like Git. This project aims to provide basic version control features like commits, log tracking, and more.
Features

    init: Creation of init file .codelog to store all objects and refs.
    Basic CLI interface: Interact with CodeLog through the terminal.

## Installation
1. Clone this repository

Clone this project to your local machine:

```console
git clone https://github.com/yourusername/codelog.git
cd codelog
```

2. Create a Virtual Environment (optional but recommended)

It's a good practice to use a virtual environment to isolate your project dependencies:

```console
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```



## Usage

Once installed, you can use the codelog command to interact with the system.

### Available Commands

For creating hidden .codelog directory to store objects, commits, logs etc
```console
codelog init
```




## Edit for self usage

After Cloning the repo we can

Install CodeLog in editable mode, use the following command:

```console
pip install setuptools
pip install --editable .
```

This will install the package setuptools for the setup of my VCS.
And second line is used to install the package in editable mode.
