from flask import Blueprint, jsonify

from api_counter.services import get_route_statistics

stats = Blueprint("stats", __name__)


@stats.route("/", methods=["GET"])
def get_stats():

    results = get_route_statistics()

    return jsonify({"results": results})
