/*----------------------------------------------------------------------*/
/*  FILE:  rand_vertices_sleep.cpp (Fifth C++ Lab Exercise 5)           */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_vertices_sleep.cpp  */
/*  BUILD: g++ -o rand_vertices_sleep rand_vertices_sleep.cpp           */
/*  RUN:   ./rand_vertices_sleep                                        */
/*----------------------------------------------------------------------*/

#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the rand function
#include <unistd.h>      // For use of the sleep function

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

  sleep(30);
  return(0);
}
