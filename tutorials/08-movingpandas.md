# Moving Pandas

## Use OOP Python NYCU Docker

We have installed the dependencies in the oop-python-nycu docker. 
Most of the movingpandas functions will work well.
However, using the interactive interface of hvplot() in jupyter notebook requires a lot more dependency (up to 13 GB).
We intended to keep the oop-python-nycu docker as lightweight as possible, 
so the hvplot() function is not supported here.

```
$ docker pull argnctu/oop
```

Get started with the jupyter.
```
$ cd ~/oop-python-nycu
$ source docker_run.sh
# source colab_jupyter.sh
```

## Use PyIvP Docker

We have a fully installed docker for movingpandas in the pyivp docker (13 GB).
Make sure you have enough disk space.
```
$ docker pull argnctu/pyivp
```

Clone the repo if you do not have:
```
$ git clone git@github.com:ARG-NCTU/pyivp.git
```

Get started with the docker:
```
$ cd ~/pyivp
$ source docker_run.sh
# source colab_jupyter.sh
```
