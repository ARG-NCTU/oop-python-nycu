# Makefile for lib_geometry (Ten Short C++ Labs)                                                          
# wget http://oceanai.mit.edu/cpplabs/lib_geometry/Makefile                                               

libcpplabs_geometry.a : Vertex.cpp Vertex.h VertexSimple.cpp VertexSimple.h SegList.cpp SegList.h
	g++ -c Vertex.cpp VertexSimple.cpp SegList.cpp
	ar cr libcpplabs_geometry.a Vertex.o VertexSimple.o SegList.o

clean:
	rm -f Vertex.o VertexSimple.o SegList.o libcpplabs_geometry.a *~

install:
	cp libcpplabs_geometry.a /usr/local/lib/

uninstall:
	rm /usr/local/lib/libcpplabs_geometry.a
