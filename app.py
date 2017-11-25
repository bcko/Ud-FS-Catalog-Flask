from flask import Flask, render_template
from sqlalchemy import create_engine


engine = create_engine('sqlite:///catalog.db')


app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('base.html')

@app.route('/catalog')
def catalog_json():
	return 'hello json endpoint'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
