# oop-python-nycu

This repo is used for OOP and Advanced OOP courses in NYCU.

## Docker

We have a Dockerfile with minimum installations of the packages we will use.
* Nginx + Flask
* vim-python-ide
* pybind11

For first time user or any Dockerfile update
```
docker pull argnctu/oop:latest
```

Clone the repo
```
git clone git@github.com:ARG-NCTU/oop-python-nycu.git
```
or if you do not have ssh key yet (you should set it up soon)
```
git clone https://github.com/ARG-NCTU/oop-python-nycu.git
```

For your first docker terminal:
```
source docker_run.sh
```

More terminal:
```
source docker_join.sh
```

## Sync your fork
Go to your fork page and click "Sync fork" then "Update branch"


Open your terminal and get ready for the repo:
```sh
cd oop-python-nycu/
git pull
```

## Check your user name with user email in the repository
To add an exception for this directory:
```sh
git config --global --add safe.directory /home/arg/oop-python-nycu
```

Check your user name with user email:
```sh
git log --pretty="%an <%ae>" | grep "your email signed in github" | sort | uniq
```

For example:
```sh
git log --pretty="%an <%ae>" | grep "brian910724@gmail.com" | sort | uniq
```

## If you have not set the user name in your local machine
Exit the docker
```sh
exit
```

Set the user name in your local machine:
```sh
git config --global user.name your_github_username
```

For example:
```sh
git config --global user.name Brian2074
```

Check your global username:
```sh
git config --list
```
Result should be like:
```
user.email=brian910724@gmail.com
user.name=Brian2074
```