#include <stdio.h>

class Shape {
public:
	virtual ~Shape();
	virtual void draw() = 0;
};

class Circle : public Shape {
public:
	virtual ~Circle();
	virtual void draw();
};

Shape::~Shape() {
	printf("shape destructor\n");
}

// void Shape::draw() {
//	printf("Shape::draw\n");
// }

Circle::~Circle() {
	printf("circle destructor\n");
}

void Circle::draw() {
	printf("Circle::draw\n");
}

int main() {
	Shape *shape = new Circle;
	shape->draw();
	delete shape;

	return 0;
}
