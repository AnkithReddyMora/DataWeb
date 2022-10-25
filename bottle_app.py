
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'ANkith loves NASA gang'
@route('/bye')
def bye_world():
    return 'ankith loves kavsssss'

application = default_app()

