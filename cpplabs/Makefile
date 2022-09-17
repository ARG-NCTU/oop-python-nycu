 # Top-Level Make Directory for programs through Lab 06                                                    
 # wget http://oceanai.mit.edu/cpplabs/Makefile                                                            

all: build tests


build:
	make -C lib_geometry
	make -C lab05
	make -C pybind11

tests:
	python3 pytest/test_cpplabs_pybind11.py

clean:
	make -C lib_geometry clean
	make -C lab05 clean
	make -C pybind11 clean
