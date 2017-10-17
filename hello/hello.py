from flask import (Flask, render_template)


app = Flask(__name__)


# Views
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
