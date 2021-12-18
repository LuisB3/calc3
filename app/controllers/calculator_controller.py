# pylint: disable=import-error
# pylint: disable=invalid-name
# pylint: disable=no-name-in-module
# pylint: disable=no-member
# pylint: disable=unused-import
# pylint: disable=wrong-import-order
import pandas as pd
from calc.calculator import Calculator
from calc.history.calculator_result import CalculatorResult
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Please enter your values below...'
            return render_template(href = url_for('calculator.html') , error=error)
        else:
            flash('Congratulations on your calculation.')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_result_of_last_calculation_added_to_history())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('home.html', error=error)

    @staticmethod
    def get():
        return render_template('home.html')
        return render_template('result.html', results=calculation_results)
