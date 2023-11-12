#!/usr/bin/env python3
"""

    City that inherits from BaseModel

"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City that inherits from BaseModel """
    state_id = ""
    name = ""
