/*----------------------------------------------------------------------*/
/*  FILE:  SegList.cpp                                                  */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/SegList.cpp              */
/*----------------------------------------------------------------------*/

#include <cmath>           // For using the hypot function
#include "SegList.h"

using namespace std;

//-----------------------------------------------------------------------
// Procedure: addVertex()

void SegList::addVertex(double x, double y)
{
  Vertex vertex(x,y);
  m_vertices.push_back(vertex);
}

//-----------------------------------------------------------------------
// Procedure: totalEdgeLength

double SegList::totalEdgeLength() const
{
  double total = 0;
  for(unsigned int i=0; i<m_vertices.size(); i++) {
    if((i+1) < m_vertices.size()) {
      double xdelta = m_vertices[i].getX() - m_vertices[i+1].getX();
      double ydelta = m_vertices[i].getY() - m_vertices[i+1].getY();
      double dist = hypot(xdelta, ydelta);
      total += dist;
    }
  }

  return(total);
}

//-----------------------------------------------------------------------
// Procedure: getSpec

string SegList::getSpec() const
{
  string spec;
  for(unsigned int i=0; i<m_vertices.size(); i++) {
    if(i != 0)
      spec += ",";
    spec += m_vertices[i].getSpec();
  }

  return(spec);
}
