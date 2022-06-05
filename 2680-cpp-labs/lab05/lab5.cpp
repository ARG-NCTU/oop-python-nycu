#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class VertexSimple {
public:
    VertexSimple() {m_x=0; m_y=0;};
    VertexSimple(int x, int y) {m_x=x, m_y=y;};
    void setRandom(int min, int max) {
        int range = max - min;
        m_x = (rand() % range) + min;
        m_y = (rand() % range) + min;
    }
    void setRandom(int xmin, int xmax, int ymin, int ymax) {
        if((xmin >= xmax) || (ymin >= ymax))
            return;
        int xrange = xmax - xmin;
        m_x = (rand() % xrange) + xmin;

        int yrange = ymax - ymin;
        m_y = (rand() % yrange) + ymin;
    }
    string getSpec() {
        stringstream ss;
        ss << "x=" << m_x << ",y=" << m_y;
        return(ss.str());
    }
    
    void setXY(int x, int y) {m_x=x; m_y=y;};
    int  getX() const {return(m_x);};
    int  getY() const {return(m_y);};
protected:  
   int m_x;
   int m_y;
};

int main(){
    VertexSimple vertex(10,10);
    cout<<vertex.getSpec()<<endl;
    vertex.setRandom(0, 100);
    cout<<vertex.getSpec();
}