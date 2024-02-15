from flask import Blueprint, jsonify, request

from api_counter.services import increment_cache

api = Blueprint("api", __name__)


@api.route("/<path:route>", methods=["GET"])
def get_api_endpoint(route):
    return jsonify({"status": "ok"})


@api.before_request
def count_visits():
    try:
        increment_cache(request.path)
    except Exception as e:
        print(e)
