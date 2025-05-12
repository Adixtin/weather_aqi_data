from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import ReadingAPI, NearestReadingAPI
    from flask.views import MethodView

    app.add_url_rule('/readings', view_func=ReadingAPI.as_view('readings'))
    app.add_url_rule('/readings/nearest', view_func=NearestReadingAPI.as_view('nearest_reading'))

    return app
