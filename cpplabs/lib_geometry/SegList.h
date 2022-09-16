/*----------------------------------------------------------------------*/
/*  FILE:  SegList.h                                                    */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/SegList.h                */
/*----------------------------------------------------------------------*/

#ifndef SEGLIST_HEADER
#define SEGLIST_HEADER

#include <string>
#include <vector>
#include "Vertex.h"

class SegList {
 public:
  SegList() {};
  ~SegList() {};

  void addVertex(double x, double y);
  void addVertex(Vertex vertex) {m_vertices.push_back(vertex);};

  unsigned int size() {return(m_vertices.size());};
  double totalEdgeLength() const;
  std::string getSpec() const;

 protected:

  std::vector<Vertex> m_vertices;
  std::string         m_label;
};

#endif
