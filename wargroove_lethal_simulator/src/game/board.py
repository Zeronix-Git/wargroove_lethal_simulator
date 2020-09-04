import numpy as np
import sqlite3 as sql
from Collections import namedtuple

class Board:
    def __init__(self, players, terrain, units):
        """
        Terrain: np.ndarray of size (height, width)
        units: List of Unit instances
        """
        self.players = players
        self.terrain = terrain
        self.units = units
        

        


    
class Game:
    def __init__(self, board, game_id):
        self.board = board
        self.db = sql.connect(f"data/game_{game_id}")
        
    def move_unit(self, unit_id, new_pos):
        pass
    
    def create_unit(self, unit_id, pos):
        pass
    
    def save(self):
        """
        Save to a SQLite instance
        """
        pass