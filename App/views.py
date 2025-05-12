from flask import request, jsonify
from flask.views import MethodView
from .service import validate, store_reading, find_closest_reading
from datetime import datetime

class ReadingAPI(MethodView):
    def post(self):
        try:
            data = request.json
            reading = validate(data)
            store_reading(reading)
            return jsonify({"status": "ok"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

class NearestReadingAPI(MethodView):
    def get(self):
        ts_str = request.args.get("timestamp")
        try:
            target = datetime.fromisoformat(ts_str)
            closest = find_closest_reading(target)
            return jsonify(closest.__dict__), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400