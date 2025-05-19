```mermaid
classDiagram
    class Animal {
        - age: int
        - name: str
        + get_age(): int
        + get_name(): str
        + set_age(newage: int): void
        + set_name(newname: str = ""): void
        + __str__(): str
    }

    class Cat {
        + speak(): void
        + __str__(): str
    }

    class Person {
        - friends: List[str]
        + get_friends(): List[str]
        + speak(): void
        + add_friend(fname: str): void
        + age_diff(other: Person): void
        + __str__(): str
    }

    class Student {
        - major: str
        + change_major(major: str): void
        + speak(): void
        + __str__(): str
    }

    class Rabbit {
        - parent1: Rabbit
        - parent2: Rabbit
        - rid: int
        + get_rid(): str
        + get_parent1(): Rabbit
        + get_parent2(): Rabbit
        + __add__(other: Rabbit): Rabbit
        + __eq__(other: Rabbit): bool
        + __str__(): str
        classVar tag: int
    }

    Animal <|-- Cat
    Animal <|-- Person
    Person <|-- Student
    Animal <|-- Rabbit