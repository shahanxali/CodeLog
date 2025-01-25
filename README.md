# CodeLog

CodeLog is a simple, custom version control system (VCS) built in Python. It allows users to track changes in their codebase, similar to other VCS like Git. This project aims to provide basic version control features like commits, log tracking, and more.
Features like init, commit, log etc.

This project have 2 text files named info.txt and explaininfo.txt.
info.txt have info related to setup and system.
explaininfo.txt is a text file to explain how each command is made and about whys and hows. The basic information to explain the project

The main parts of the project, which contains data.py, base.py, cli.py
cli.py is where the commands are handled and user input is manipulated
data.py is where directories are controlled, it just visits files here and there according to need
base.py is for high level programming, fetching data, doing linkings of OID, logical parts, things to ignore etc

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

For creating hidden .codelog directory to store objects, commits, logs etc. init is created
```console
codelog init
```

For Creating hash of file using SHA-1 algorithm and then storing it in .codelog directory (the hash is called OID here) we be using heash-object
```console
codelog hash-object <file-name>
```

To read the raw data of the corresponding OID provided, OID made by hash-object for that we use cat-file
```console
codelog cat-file <OID>
```

Creating hash of file is not enough, so we created a command which creates hash key of the directory
```console
codelog write-tree
```

Reading the directory and it's info using corresponding OID. just like cat-file for file, we will use read-tree for directories OID
```console
codelog read-tree <OID>
```

commit command is also made which is just like that of git command. Providing additional info to the hash key, use -m to tell the machin you have a message
```console
codelog commit -m <info>
```

To print all the previous commits made, and not just the commit text, also their OID and type of OID it is, we have log function for it
```console
codelog log
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
