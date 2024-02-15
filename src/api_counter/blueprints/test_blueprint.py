from flask import Blueprint, jsonify, url_for

from api_counter.services import increment_cache
from api_counter.utils import gen_paths

test = Blueprint("test", __name__)


@test.route("/<int:num_requests>", methods=["POST"])
def create_tests(num_requests):
    paths = gen_paths(num_requests)
    urls = []
    for path in paths:
        url = url_for("api.get_api_endpoint", route=path)
        increment_cache(url)
        urls.append(url)

    return jsonify({"results": urls}), 201
