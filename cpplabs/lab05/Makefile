# Makefile for Lab 05 (Ten short C++ Labs)                                                                
# wget http://oceanai.mit.edu/cpplabs/lab05/Makefile                                                      

all: rand_vertices rand_vertices_file \
	rand_vertices_sleep rand_vertices_seed \
	rand_vertices_class rand_seglist \

rand_vertices: rand_vertices.cpp
	g++ -o rand_vertices.out rand_vertices.cpp

rand_vertices_file: rand_vertices_file.cpp
	g++ -o rand_vertices_file.out rand_vertices_file.cpp

rand_vertices_sleep: rand_vertices_sleep.cpp
	g++ -o rand_vertices_sleep.out  \
		rand_vertices_sleep.cpp

rand_vertices_seed: rand_vertices_seed.cpp
	g++ -o rand_vertices_seed.out \
		rand_vertices_seed.cpp

rand_vertices_class: ../lib_geometry/libcpplabs_geometry.a rand_vertices_class.cpp
	g++ -I../lib_geometry -L../lib_geometry \
		-o rand_vertices_class.out \
		rand_vertices_class.cpp -lcpplabs_geometry

rand_seglist: ../lib_geometry/libcpplabs_geometry.a rand_seglist.cpp
	g++ -I../lib_geometry -L../lib_geometry -o rand_seglist.out \
		rand_seglist.cpp -lcpplabs_geometry

clean:
	rm -f rand_vertices.out rand_vertices_file.out rand_vertices_class.out 
	rm -f rand_seglist.out rand_vertices_sleep.out rand_vertices_seed.out *~


