from wargroove_lethal_simulator.combat_simulator import CombatSimulator
from wargroove_lethal_simulator.unit import Unit, UnitDataProvider

def simulate_combat_example():
    print("Simulating combat between a Mage on flagstone and Soldier on plains")
    provider = UnitDataProvider.load("wargroove_lethal_simulator/assets/unitdata_2.0.json")
    
    atk_mage = Unit.from_name('mage', provider)
    def_sword = Unit.from_name('soldier', provider)
    atk_terrain_defense = 0.2
    def_terrain_defense = 0.1
    
    results = CombatSimulator.simulate_combat(atk_mage, 0.2, False,
                                              def_sword, 0.1, False)
    
    for (final_atk_health, final_def_health), prob in results.items():
        print(f"Attacker {final_atk_health}, defender {final_def_health}: probability {100 * prob}%")      

def simulate_combat_sequence_example():
    # This example shows how to use the CombatSimulator.simulate_combat_sequence function
    print("Simulating attacks on Commander by a variety of units")
    provider = UnitDataProvider.load("wargroove_lethal_simulator/assets/unitdata_2.0.json")
    

    # First, we tell the program what unit is being attacked.
    # This information is encapsulated in a defense instance. 
    
    # A defense instance is defined as a tuple of (Unit, terrainDefense, isCrit).
    # @param  Unit:  A Unit instance. Units are created by name and a reference to a UnitDataProvider.
    #               Optionally, the starting health can be modified. 
    # @param  terrainDefense: A floating number. E.g. for plains, terrainDefense = 0.1
    # @param  isCrit: A boolean. True if the unit has crit active and False otherwise. 
    
    
    
    #######################################
    #### START OF MODIFIABLE SECTION 1 ####
    #######################################
    
    defend_instance = (Unit.from_name('commander', provider, health=100), 0.3, False)
    
    #####################################
    #### END OF MODIFIABLE SECTION 1 ####
    #####################################
    
    
    # Next, we tell the program what units are attacking, and in what order. 
    
    # An attack instance is is defined as a tuple of (Unit, terrainDefense, isCrit, requiresSuicide).
    # The first three arguments are the same as a defense instance, but requiresSuicide can be provided
    # to indicate whether the unit must die in order for the attack sequence to succeed. 
    
    # An attack instance can also be a single string, "hex", in which case the program will simulate hexing. 

    
    #######################################
    #### START OF MODIFIABLE SECTION 2 ####
    #######################################
    
    attack_instances = [
        "hex",
        (Unit.from_name('soldier', provider, health=34), 0, False, True),
        (Unit.from_name('dog', provider, health=9), 0, False, True),
        (Unit.from_name('cavalry', provider, health=100), 0, True, False),
        (Unit.from_name('dragon', provider, health=100), 0, False, False),
        (Unit.from_name('dog', provider, health=100), 0, True, False)
    ]
    #####################################
    #### END OF MODIFIABLE SECTION 2 ####
    #####################################
    
    print("Combat sequence:")
    print(f"Defender is a {defend_instance[0].name} at {defend_instance[0].health} health " 
        "with terrain defense {defend_instance[1]}")
    for i, attack_instance in enumerate(attack_instances):
        if (type(attack_instance) == str):
            print(f"Attacker {i+1} is a {attack_instance}")
        else:
            print(f"Attacker {i+1} is a {attack_instance[0].name} at {attack_instance[0].health} health "
                 f"with terrain defense {defend_instance[1]} {'and must suicide' if attack_instance[3] else ''}")
    
    # The work is done! Now we just simulate the combat sequence: 
    # BzZzZt! Program is performing calculations... 
    
    state_dist_history = CombatSimulator.simulate_combat_sequence(defend_instance, attack_instances)
    final_state_dist = state_dist_history[-1]
    prob_def_death = final_state_dist[0]
    percentiles = {}
    expected_final_health = 0
    states = sorted(final_state_dist.keys())
    
    cum_prob = 0
    for state in states:
        if state < 0:
            continue
        prob = final_state_dist[state]
        cum_prob += prob
        expected_final_health += state * prob
        
    # At the end, the program prints the probability of lethal
    
    print(f"Probability of lethal: {(prob_def_death * 100):.2f}%")
    print(f"Expected final health: {expected_final_health}")

    
if __name__ == "__main__":
    simulate_combat_sequence_example()