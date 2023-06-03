from flask import Flask
from website.views import views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')
    return app

app = create_app()

if __name__ == '__main__':
    app.run()