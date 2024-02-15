import os
from typing import Tuple, List

import redis


def get_redis_conn():
    return redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=os.getenv("REDIS_PORT"),
        db=os.getenv("REDIS_DB"),
    )


def increment_cache(route: str):
    r = get_redis_conn()
    r.hincrby("routes", route)


def get_route_statistics() -> List[Tuple[str, int]]:
    r = get_redis_conn()
    route_map = r.hgetall("routes")
    results = [(k.decode(), int(v)) for k, v in route_map.items()]
    results.sort(key=lambda row: row[1], reverse=True)
    return results
