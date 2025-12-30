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

# 2025 AOOP Commit & Pytest Result
<!--START_SECTION:pytest-->

| Pytest Status   | Group Name   | Group Leader         | Group Member 1      | Group Member 2            |
|:---------|:-------------|:---------------------|:--------------------|:--------------------------|
| ✅        | Group 1      | bryson7736 : 33      | Chiang-Ian : 36     | peppa1122ee13 : 33        |
| ✅        | Group 2      | ginny923 : 12        | joanna0420 : 45     | bondyhung : 0             |
| ✅        | Group 3      | tpvupu : 25          | xiaotin22 : 32      |                           |
| ✅        | Group 4      | yt-chen1230 : 27     | Huang-Kun-wei : 26  |                           |
| ❌        | Group 5      | htyunn : 0           | okkohero : 2        |                           |
| ❌        | Group 6      | jerrywustarwars : 37 | FrosterMonster : 42 | doralu950413ee13-gif : 24 |
| ✅        | Group 7      | unknown899 : 37      | LeeYinWei : 29      |                           |
| ✅        | Group 8      | hatthebutterfly : 5  | August0117 : 44     | hungchi0222 : 31          |
| ❌        | Group 9      | pieapple1587 : 9     | terrycc9375 : 0     |                           |
| ✅        | Group 10     | iamkyleh : 100       | billlllllllly : 100 |                           |
| ✅        | Group 11     | Nelson0314 : 19      |                     |                           |
| ✅        | Group 12     | jui-pixel : 68       |                     |                           |
| ❌        | Group 13     | max052028 : 3        | jeffjun113 : 27     | ngvihoee11-nycu : 13      |
| ✅        | Group 14     | lilil0724 : 26       | noobLeo536 : 27     |                           |
| ✅        | Group 15     | minopeng : 25        | KuoShengHsin : 30   |                           |
<!--END_SECTION:pytest-->