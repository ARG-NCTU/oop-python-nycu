# CPP Labs with Python Binding

Clone the repo
```
git clone git@github.com:ARG-NCTU/oop-python-nycu.git
```
or if you do not have ssh key yet
```
git clone https://github.com/ARG-NCTU/oop-python-nycu.git
```

Run docker 
```
source docker_run.sh
```

Compile and install library
```
cd ~/oop-python-nycu/cpplabs && make
```

After you compile and install the library, open jupyter notebook
```
source colab_jupyter.sh
```

Open a browser, and enter the following
```
http://127.0.0.1:8888/tree
```

Now you can use c++ library 'cpplabs' in Python.