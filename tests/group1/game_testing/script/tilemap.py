import pygame

NEIGHBORS = [(0,0),(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
HAVE_COLLISION = {'stone', 'grass'}

class small_tile:
    def __init__(self, type, variant, pos=(0,0)):
        self.type = type
        self.variant = variant
        self.pos = pos
class Tilemap:
    def __init__(self, game, size=16):
        self.game = game
        self.tile_size = size
        self.tilemap = {} #floor that has collision
        self.offgrid_tiles = [] #decorative tiles   

        for i in range(10):
            #setup floor
            self.tilemap[str(3+i) + ";10"] = small_tile('grass', 1, (3+i,10))
            self.tilemap["10;" + str(i+5)] = small_tile('stone', 1, (10,i+5))

        for i in range(10):
            #setup offgrid tiles
            self.offgrid_tiles.append(small_tile('decor', 0, (i*16, 0)))
            self.offgrid_tiles.append(small_tile('decor', 1, (i*16, 16)))
            self.offgrid_tiles.append(small_tile('decor', 2, (i*16, 32)))
            self.offgrid_tiles.append(small_tile('decor', 3, (i*16, 48)))

    def render(self, surface, offset = [0,0]):

        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile.type][tile.variant], (tile.pos[0]-offset[0], tile.pos[1]-offset[1]))

        for location in self.tilemap:
            tile = self.tilemap[location]
            surface.blit(self.game.assets[tile.type][tile.variant], (tile.pos[0]*self.tile_size - offset[0], tile.pos[1]*self.tile_size-offset[1]))

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0]//self.tile_size), int(pos[1]//self.tile_size)) #convert pixel position to tile position, which is bigger
        for offset in NEIGHBORS:
            check = str(tile_loc[0] + offset[0]) + ";" + str(tile_loc[1] + offset[1])
            if check in self.tilemap:
                tiles.append(self.tilemap[check])
        return tiles
    
    def tile_collision(self, pos):
        rects = []  
        for tile in self.tiles_around(pos):
            if tile.type in HAVE_COLLISION:
                rects.append(pygame.Rect(tile.pos[0]*self.tile_size, tile.pos[1]*self.tile_size, self.tile_size, self.tile_size))
        return rects