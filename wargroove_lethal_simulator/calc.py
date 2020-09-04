# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:28:46 2020
"""


import functools
from wtforms import Form, fields, validators
from wargroove_lethal_simulator.src.unit import UnitDataProvider

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('calc', __name__, url_prefix='/calculate')
provider = UnitDataProvider.load("wargroove_lethal_simulator/assets/unitdata_2.0.json")

class AttackInstanceForm(Form):
    unit_name = fields.SelectField('Unit name', choices = list(provider.unit_names))
    terrain_defense = fields.IntegerField('Terrain defense', validators=[
        validators.NumberRange(min = -2, max = 4, message="Terrain defense is an integer between -2 and 4")])
    is_crit = fields.BooleanField('Is it a critical?', default=False)
    requires_suicide = fields.BooleanField('Is this a suicide attacker?', default=False)

@bp.route("/calculate", methods=('GET', 'POST'))
def calculate():
    form = AttackInstanceForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('calc.html', form=form)