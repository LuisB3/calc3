"""Flask web app"""
#pylint : disable=import-error
#pylint : disable=no-name-in-module
#pylint : disable=unused-import
from flask import Flask, render_template
from controllers.index_controller import IndexController
from controllers.calculator_controller import CalculatorController
from controllers.article1_controller import Article1Controller
from controllers.article2_controller import Article2Controller
from controllers.article3_controller import Article3Controller
from controllers.article4_controller import Article4Controller
from controllers.glossary_controller import GlossaryController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

#app = Flask(__name__)
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#app.wsgi_app = DebuggedApplication(app.wsgi_app)

@app.route("/", methods=['GET'])
def index_get():
    """Index page"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """Calculator page"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """Calculator pos"""
    return CalculatorController.post()

@app.route("/result", methods=['GET'])
def calculator_get_result():
    return CalculatorController.get_result()

@app.route("/article1", methods=['GET'])
def article1_get():
    return Article1Controller.get()

@app.route("/article2", methods=['GET'])
def article2_get():
    return Article2Controller.get()

@app.route("/article3", methods=['GET'])
def article3_get():
    return Article3Controller.get()

@app.route("/article4", methods=['GET'])
def article4_get():
    return Article4Controller.get()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    return GlossaryController.get()
