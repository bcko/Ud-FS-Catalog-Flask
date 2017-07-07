from catalog_app import app

@app.route('/')
def hello_world():
    return 'Hello, World!'