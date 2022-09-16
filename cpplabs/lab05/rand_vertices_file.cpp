/*----------------------------------------------------------------------*/
/*  FILE:  rand_vertices_file.cpp (Fifth C++ Lab Exercise 2)            */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_vertices_file.cpp   */
/*  BUILD: g++ -std=c++0x -o rand_vertices_file rand_vertices_file.cpp  */
/*  RUN:   rand_vertices_file --filename=vertices.txt --amt=5           */
/*----------------------------------------------------------------------*/

#include <vector>   
#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the atoi function
#include <cstdio>        // For use of the fopen, fclose, fprintf functions

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
    cout << "Usage: rand_vertices --filename=FILE --amt=AMT" << endl;
    return(1);
  }

  // Part 2: Define the C-style structure and create N instances into a vector
  struct Vertex {
    int x;
    int y;
  };

  vector<Vertex> vertices;

  for(int i=0; i<amount; i++) {
    Vertex vertex;
    vertex.x = (rand() % 201) + -100;
    vertex.y = (rand() % 201) + -100;
    vertices.push_back(vertex);
  }

  // Part 3: Open the output file and write the vector of vertices
  FILE *f = fopen(filename.c_str(), "w");
  if(!f) {
    cout << "Unable to open file: " << filename << endl;
    return(1);
  }

  for(int i=0; i<vertices.size(); i++) {
    fprintf(f, "x=%d,", vertices[i].x);
    fprintf(f, "y=%d\n", vertices[i].y);
  }

  fclose(f);
  return(0);
}
