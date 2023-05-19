# How to update submodule

## 1. pull the latest repo

```
$ cd oop-python-nycu
$ git pull
```

You can see a submodule called **movingpandas**, but it's empty.

## 2. init/update submodule
run the following commands
```
$ git submodule init
$ git submodule update
```

Now you can see a complete folder of submodule.

If the submodule is further updated

Make sure you are in the master branch
```
$ cd movingpandas
$ git checkout master
$ git pull
```
