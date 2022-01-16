# Wargroove Lethal Simulator
A tool to simulate the combat results between a defending unit, and any sequence of attackers, including hexes. 

## How does it work?
- The script re-implements the exact damage calculation logic used by the game to accurately simulate the results of any combat between an attacker and defender. 
- RNG is accounted for by maintaining a probability distribution over the attacker and defender's health.  
- Damage probabilities are (by default) calculated to 4 significant figures; however the program can easily be modified to work with a higher number of significant figures. 
- Modify the `combat_simulator_example.py` file in order to use the script.

## Getting started
Currently, the program is implemented as a Python script. You will need to have Python 3 installed on your device in order to be able to use this tool. The ultimate goal is to move to a more user-friendly interface, such as a web app frontend. 

1. Make sure you have Python 3 installed. 
2. Make sure NumPy is installed: 
```
python3 -m pip install numpy
```
3. Install the repository by cloning it or downloading the source as a zip.
4. See `combat_simulator_example.py` for examples of how to use. 

## Current Features:
- Any unit (including buildings) as a defender
- Any unit (excluding buildings) or a hex as an attacker

## Feature Wishlist

1. TODO: Add support for commander grooves. E.g. Ryota dash, Koji bomb, Ragna jump, Wulfar golf, Sedge groove. 
2. TODO: Implement a function that takes a given set of attackers and calculates the optimal attacking sequence by brute-force search. 
3. TODO: Implement the ability to simulate damage with no RNG (e.g. for puzzles). 
4. TODO: Implement the project as a web app with a Javascript interface. (Under construction!) 

## Contributing

Bug reports can be raised as Github Issues. 
Urgent inquiries can be directed to Zeronix#2793 on Discord. 

I welcome any help with the above feature wishlist! Please message Zeronix#2793 on Discord if you'd like to help out in any way. 



