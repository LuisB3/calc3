# pylint: disable=import-error
# pylint: disable=invalid-name
# pylint: disable=no-name-in-module
# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from app.controllers.controller import ControllerBase
from flask import Flask, render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('home.html')
