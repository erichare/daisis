class MapStack:
    def __init__(self, nx, ny):
        self.nx = nx
        self.ny = ny
        self.nb_layers = None
        self.maps = []

    def add_layer(self, map):
        if len(map.shape) == 2 and map.shape[0] == self.ny and map.shape[1] == self.nx:
            self.maps.append(map)
            self.nb_layers = len(self.maps)
            return "Map sucessfully added."
        else:
            return "Could not add map. Incompatible dimensions."
