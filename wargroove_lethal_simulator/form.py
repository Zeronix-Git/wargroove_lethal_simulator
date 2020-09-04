# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:42:22 2020
"""


from wtforms import Form, BooleanField, StringField, validators
from src.unit import UnitDataProvider



class CalculateForm(Form):
    unit_name = SelectField('Unit name', choices = [unit_name for ])