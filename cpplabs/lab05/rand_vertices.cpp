/*----------------------------------------------------------------------*/
/*  FILE:  rand_vertices.cpp (Fifth C++ Lab Exercise 1)                 */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_vertices.cpp        */
/*  BUILD: g++ -o rand_vertices rand_vertices.cpp                       */
/*  RUN:   ./rand_vertices                                              */
/*----------------------------------------------------------------------*/

#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the rand function

using namespace std;

int main()
{
  struct Vertex {
    int x;
    int y;
  };

  for(int i=0; i<5; i++) {
    Vertex vertex;
    vertex.x = (rand() % 201) + -100;
    vertex.y = (rand() % 201) + -100;
    cout << "x=" << vertex.x << ",y=" << vertex.y << endl;
  }

 return(0);
}
