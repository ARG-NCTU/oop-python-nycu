# Guide: How to check your commit count

## Sync your fork
Go to your fork page and click "Sync fork" then "Update branch"


Open your terminal and get ready for the repo:
```sh
cd oop-python-nycu/
git pull
```

## Run the docker
```sh
source docker_run.sh
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

Rerun the docker
```sh
source docker_run.sh
cd utils/
```

## Run the script to get commit count
Run the script:
```sh
python3 git_commit_count.py --user username --start_date YYYY-MM-DD
```

For example:
```sh
python3 git_commit_count.py --user zhuchi76 --start_date 2024-08-26
```

Result should be like:
```
User: zhuchi76, Commit Count: 1
```