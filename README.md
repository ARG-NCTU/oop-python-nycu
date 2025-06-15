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
git log --pretty="%an <%ae>" | grep "tzuchichen.sc08@nycu.edu.tw" | sort | uniq
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
git config --global user.name zhuchi76
```

Check your global username:
```sh
git config --list
```
Result should be like:
```
user.email=tzuchichen.sc08@nycu.edu.tw
user.name=zhuchi76
```

<!--START_SECTION:pytest-->

| status   | group_name   | Group Leader        | Group Member 1        | Group Member 2         |
|:---------|:-------------|:--------------------|:----------------------|:-----------------------|
| ✅        | Group 1      | LeeYinWei : 50      | unknown899 : 25       |                        |
| ❌        | Group 2      | neoAurora : 25      | Lawrence16428 : 0     | howardhung14 : 26      |
| ❌        | Group 3      | yoyo0213 : 50       | JonathanYangSW : 37   | GinoChen113511247 : 32 |
| ✅        | Group 4      | JumboZhang1119 : 52 | peienwu1216 : 33      | chxyuuu : 46           |
| ❌        | Group 5      | ginny923 : 18       | joanna0420 : 24       | dua0505 : 17           |
| ✅        | Group 6      | jui-pixel : 66      | SamTung113511034 : 29 | charles691 : 35        |
| ✅        | Group 7      | Tony104147 : 13     |                       |                        |
| ❌        | Group 8      | haleychang0530 : 31 | Hazel-1212 : 41       | tree1014 : 24          |
| ✅        | Group 9      | CHENG-JE : 26       | lwc-ed : 26           |                        |
| ✅        | Group 10     | tpvupu : 56         | xiaotin22 : 62        | calistayang : 43       |
| ❌        | Group 11     | Rickycheong0515 : 3 | hfchiang : 3          | Samuel11GitHub : 0     |
| ❌        | Group 12     | kufanghua : 25      | yezh0915 : 65         | fiesta0217 : 21        |
| ❌        | Group 13     | lucasliu0910 : 7    | carabapy : 6          | jing1688 : 65          |
| ✅        | Group 14     | weiouo-0817 : 24    | NiNialpaca : 4        |                        |
| ❌        | Group 15     | gamemode0701 : 11   | Tonyyu2403 : 36       |                        |
| ❌        | Group 16     | TerryCheese : 8     | junlin27 : 36         |                        |
| ❌        | Group 17     | Miiaow3011 : 26     | bonnieliao774 : 54    | emmazheng0318 : 21     |
| ✅        | Group 18     | ChocomintTW : 1     | TedChueh : 12         | pitinghsu : 0          |
| ❌        | Group 19     | max052028 : 3       | 113511080 : 25        |                        |
| ❌        | Group 20     | houyuankai : 4      |                       |                        |
| ✅        | Group 21     | 0u88 : 12           |                       |                        |
<!--END_SECTION:pytest-->
