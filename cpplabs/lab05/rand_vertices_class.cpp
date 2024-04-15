/*----------------------------------------------------------------------*/
/*  FILE:  rand_vertices_class.cpp (Fifth C++ Lab Exercise 3)           */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_vertices_class.cpp  */
/*  BUILD: g++ -o rand_vertices_class   \                               */ 
/*         VertexSimple.cpp rand_vertices_class.cpp                     */
/*  RUN:   rand_vertices_class --filename=vertices.txt 100              */
/*----------------------------------------------------------------------*/

#include <vector>   
#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the atoi function
#include <cstdio>        // For use of the fopen, fclose, fprintf functions
#include "VertexSimple.h"

using namespace std;

int main(int argc, char **argv)
{
  // Part 1: Handle and check command line arguments
  string filename;
  int    amount = 0;
  for(int i=1; i<argc; i++) {
    string argi = argv[i];
    if(argi.find("--filename=") == 0)
      filename = argi.substr(11);
    else if(argi.find("--amt=") == 0) {
      string str_amt = argi.substr(6);
      amount = atoi(str_amt.c_str());
    }
  }

  if((filename=="") || (amount<=0)) {
    cout << "Usage: rand_vertices_class --filename=FILE --amt=AMT" << endl;
    return(1);
  }

  vector<VertexSimple> vertices;
  for(int i=0; i<amount; i++) {
    VertexSimple vertex;
    vertex.setRandom(-100, 100);
    vertices.push_back(vertex);
  }

  // Part 3: Open the output file and write the vector of vertices
  FILE *f = fopen(filename.c_str(), "w");
  if(!f) {
    cout << "Unable to open file: " << filename << endl;
    return(1);
  }

  for(int i=0; i<vertices.size(); i++) {
    string vertex_spec = vertices[i].getSpec();
    fprintf(f, "%s\n", vertex_spec.c_str());
  }

  fclose(f);
  return(0);
}
