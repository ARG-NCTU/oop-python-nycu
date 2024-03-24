# add mermaid cladd diagram for class Animal
```mermaid
classDiagram
    Animal <|-- Dog
    Animal <|-- Cat
    Animal <|-- Duck
    Animal : +int age
    Animal : +String name
    Animal: +void eat()
    Animal: +void sleep()
    Animal: +void makeSound()
    Dog : +void bark()
    Cat : +void meow()
    Duck : +void quack()
```
