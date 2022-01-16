import numpy as np
import collections
from dataclasses import dataclass

@dataclass
class Unit:
    """
    Unit info data class.
    
    All unit-specific information given by UnitDataProvider
    """
    
    unit_type:  int
    unit_data_provider: object
    health: int = 100
    unit_id: int = None
    owner: int = None
    
    # The UnitDataProvider doesn't distinguish different buildings
    # Hacky way to handle that for now. 
    # The ideal fix is to update the UnitDataProvider to track this
    is_barracks: bool = False
    is_tower: bool = False
    is_port: bool = False
    is_village: bool = False
        
    @staticmethod
    def from_name(unit_name, unit_data_provider, position_x: int = None,
                  position_y: int = None, health=100, unit_id = None, 
                  owner = None):
        unit_type = unit_data_provider.unit_index.get_index(unit_name)
        return Unit(unit_type=unit_type, 
                    unit_data_provider=unit_data_provider, 
                    health=health, 
                    unit_id=unit_id,
                    owner = owner)
    
    @property
    def name(self):
        return self.unit_data_provider.unit_index.get_value(self.unit_type)
    
    """
    Unit-specific information is provided by the UnitDataProvider
    """
        
    @property
    def crit_multiplier(self):
        return self.unit_data_provider.get_crit_multiplier(self.unit_type)
    
    @property
    def can_counter(self):
        return self.unit_data_provider.can_counter(self.unit_type)
    
    def get_base_damage(self, other_unit):
        return self.unit_data_provider.get_base_damage(self.unit_type, other_unit.unit_type)
    
    @property
    def movement_range(self):
        return self.unit_data_provider.get_movement_range(self.unit_type)
    
    @property
    def can_move(self):
        """Structures have 0 movement range"""
        return self.movement_range > 0    

    @property
    def movement_type(self):
        return self.unit_data_provider.get_movement_type(self.unit_type)
    

    