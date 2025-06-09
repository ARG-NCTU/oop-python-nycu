"""
Speed is the number of turns to reach most distant opponent.
Colour and explosion size are for the visualizer.
Reveal chance is not used.
"""


from enum import Enum, unique
from collections import namedtuple


Weapon = namedtuple("Weapon", ["COLOUR", "COST", "DAMAGE", "EXPLOSION_SIZE",
                               "SPEED", "REVEAL_CHANCE"])


Laser = Weapon(
    COLOUR = (255, 255, 0),
    COST = 10,
    DAMAGE = 0,
    EXPLOSION_SIZE = 3,
    SPEED = 0,
    REVEAL_CHANCE = 1,
)

Missile = Weapon(
    COLOUR = (0, 192, 0),
    COST = 10,
    DAMAGE = 0,
    EXPLOSION_SIZE = 5,
    SPEED = 2,
    REVEAL_CHANCE = 0.5,
)

Nuke = Weapon(
    COLOUR = (255, 0, 0),
    COST = 1,
    DAMAGE = 0,
    EXPLOSION_SIZE = 14,
    SPEED = 1,
    REVEAL_CHANCE = 1,
)

# You can define your own weapons here.
Cat = Weapon(
    COLOUR = (255, 255, 255),
    COST = 1,
    DAMAGE= 29,
    EXPLOSION_SIZE = 5,
    SPEED = 1,
    REVEAL_CHANCE = 1,
)
Dirt1 = Weapon(
    COLOUR = (255, 0, 255),
    COST = 1,
    DAMAGE= -5,
    EXPLOSION_SIZE = 5,
    SPEED = 3,
    REVEAL_CHANCE = 1,
)
Dirt2 = Weapon(
    COLOUR = (255, 0, 255),
    COST = 1,
    DAMAGE= -5,
    EXPLOSION_SIZE = 5,
    SPEED = 2,
    REVEAL_CHANCE = 1,
)
Dirt3 = Weapon(
    COLOUR = (255, 0, 255),
    COST = 1,
    DAMAGE= -5,
    EXPLOSION_SIZE = 5,
    SPEED = 1,
    REVEAL_CHANCE = 1,
)
Dirt4 = Weapon(
    COLOUR = (255, 0, 255),
    COST = 1,
    DAMAGE= -5,
    EXPLOSION_SIZE = 5,
    SPEED = 5,
    REVEAL_CHANCE = 1,
)
Dirt5 = Weapon(
    COLOUR = (255, 0, 255),
    COST = 1,
    DAMAGE= -5,
    EXPLOSION_SIZE = 5,
    SPEED = 0.5,
    REVEAL_CHANCE = 1,
)
@unique
class Weapons(Enum):
    LASER = Laser
    MISSILE = Missile
    NUKE = Nuke
    CAT = Cat
    DIRT1 = Dirt1
    DIRT2 = Dirt2
    DIRT3 = Dirt3
    DIRT4 = Dirt4
    DIRT5 = Dirt5
