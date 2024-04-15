/*----------------------------------------------------------------------*/
/*  FILE:  rand_seglist.cpp (Fifth C++ Lab Exercise 4)                  */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_seglist.cpp         */
/*  BUILD: g++ -o rand_seglist Vertex.cpp SegList.cpp rand_seglist.cpp  */
/*  RUN:   rand_seglist --filename=vertices.txt --amt=100               */
/*----------------------------------------------------------------------*/

#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the atoi function
#include <cstdio>        // For use of the fopen, fclose, fprintf functions
#include "SegList.h"

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
    cout << "Usage: rand_seglist --filename=FILE --amt=AMT" << endl;
    return(1);
  }

  // Part 2: Build the SegList with randomly generated vertices
  SegList seglist;
  for(int i=0; i<amount; i++) {
    Vertex vertex;
    vertex.setRandom(-100, 100);
    seglist.addVertex(vertex);
  }

  // Part 3: Open the output file and write the vector of vertices
  FILE *f = fopen(filename.c_str(), "w");
  if(!f) {
    cout << "Unable to open file: " << filename << endl;
    return(1);
  }

  string seglist_spec = seglist.getSpec();
  fprintf(f, "%s\n", seglist_spec.c_str());

  fclose(f);
  return(0);
}
