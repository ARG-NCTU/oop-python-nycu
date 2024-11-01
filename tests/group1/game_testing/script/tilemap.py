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

    def render(self, surface):

        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile.type][tile.variant], (tile.pos[0], tile.pos[1]))

        for location in self.tilemap:
            tile = self.tilemap[location]
            surface.blit(self.game.assets[tile.type][tile.variant], (tile.pos[0]*self.tile_size, tile.pos[1]*self.tile_size))

        