# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:28:03 2020
"""

from pathlib import Path
from flask import Flask
from wargroove_lethal_simulator.src.combat_simulator import CombatSimulator

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    path = Path(app.instance_path)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = path / 'wargroove_lethal_simulator.sqlite'
        )
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    path.touch(exist_ok=True)
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from wargroove_lethal_simulator import calc
    app.register_blueprint(calc.bp)
    
    return app