# 2.680 C++ Labs

This is adapted from the 
[Ten C++ Labs](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Lab.HomePageCPP) used in the MIT 2.680 course.

## [lab05](https://oceanai.mit.edu/ivpman/pmwiki/pmwiki.php?n=Lab.CPPClasses#section3.2)

## cpplabs examples

This is an example based on 2.680 CPP Labs (lab05 and lab06)

### Compile and Install Library

In Docker,
```
cd ~/pyivp/examples/cpplabs
make
```

Note that 
* We will compile the lib_geometry and install it to /usr/local/lib, which is inside container. (so no worries to mess up your own system)
* We also run a python code to test the installed library in python (pytest/test_plus.py)

<img width="599" alt="image" src="https://user-images.githubusercontent.com/16217256/175802286-c1e5174b-0f45-4eed-98bb-eaafcca12bb7.png">

## pybind11 example

```
source docker_run.sh
cd example
make
python3 pytest/test.py
```

You should see:

```
Made a bike called: Yamaha
Zoom Zoom on road: mullholland
```
without import errors or assert fails

<img width="699" alt="image" src="https://user-images.githubusercontent.com/16217256/172060720-61cdd29c-e1f8-4990-84fa-5f274e1ad31e.png">

