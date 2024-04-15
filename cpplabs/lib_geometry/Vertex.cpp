/*----------------------------------------------------------------------*/
/*  FILE:  Vertex.cpp                                                   */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/Vertex.cpp               */
/*----------------------------------------------------------------------*/

#include <sstream>
#include "Vertex.h"

using namespace std;

//-----------------------------------------------------------------------
// Procedure: getSpec()

string Vertex::getSpec() const
{
  stringstream ss;
  ss << "x=" << m_x << ",y=" << m_y;
  return(ss.str());
}

//-----------------------------------------------------------------------
// Procedure: setRandom()

void Vertex::setRandom(int min, int max) 
{
  setRandom(min, max, min, max);
}

//-----------------------------------------------------------------------
// Procedure: setRandom()

void Vertex::setRandom(int xmin, int xmax, int ymin, int ymax) 
{
  if((xmin >= xmax) || (ymin >= ymax))
    return;

  int xrange = xmax - xmin;
  m_x = (rand() % xrange) + xmin;

  int yrange = ymax - ymin;
  m_y = (rand() % yrange) + ymin;
}
