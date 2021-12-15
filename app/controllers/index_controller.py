# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    """Controller class"""
    @staticmethod
    def get():
        return render_template('index.html')
