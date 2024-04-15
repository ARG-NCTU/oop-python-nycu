/*----------------------------------------------------------------------*/
/*  FILE:  rand_vertices_seed.cpp (Fifth C++ Lab Exercise 6)            */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/rand_vertices_seed.cpp   */
/*  BUILD: g++ -o rand_vertices_seed rand_vertices_seed.cpp             */
/*  RUN:   ./rand_vertices_seed                                         */
/*----------------------------------------------------------------------*/

#include <iostream>      // For use of the cout function
#include <cstdlib>       // For use of the rand function
#include <ctime>         // For use of the time function
#include <unistd.h>      // For use of the getpid function

using namespace std;

int main()
{
  struct Vertex {
    int x;
    int y;
  };

  unsigned long int tseed = time(NULL);
  unsigned long int pseed = getpid() + 1;

  unsigned int rseed = (tseed*pseed) % 50000;

  cout << "time_seed: " << tseed << endl;
  cout << "pid_seed:  " << pseed << endl;
  cout << "rand_seed: " << rseed << endl;

  srand(rseed);

  for(int i=0; i<5; i++) {
    Vertex vertex;
    vertex.x = (rand() % 201) + -100;
    vertex.y = (rand() % 201) + -100;
    cout << "x=" << vertex.x << ",y=" << vertex.y << endl;
  }

  return(0);
}
