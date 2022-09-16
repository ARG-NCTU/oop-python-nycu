/*----------------------------------------------------------------------*/
/*  FILE:  VertexSimple.h                                               */
/*  WGET:  wget http://oceanai.mit.edu/cpplabs/VertexSimple.h           */
/*----------------------------------------------------------------------*/

#ifndef VERTEX_SIMPLE_HEADER
#define VERTEX_SIMPLE_HEADER

#include <string>

class VertexSimple {
 public:
  VertexSimple() {m_x=0; m_y=0;};
  ~VertexSimple() {};

  void setRandom(int min, int max);

  std::string getSpec() const;

 protected:  
  int m_x;
  int m_y;
};
#endif
