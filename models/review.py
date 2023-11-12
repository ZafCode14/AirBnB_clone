#!/usr/bin/env python3
"""

    Review that inherits from BaseModel

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
