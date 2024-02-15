import random
import string


def gen_paths(num_paths: int):
    """
    Generate a list of proceduraly-generated paths of length num_paths

    Each path obeys the following constraints:
        * /api/ followed by 1 to 6 path segments
        * Each path segment is a random string pulled from a pool of 3 random strings used by a single test run
        * Example of URLs in a single test run:
          * /api/xyz/ (Valid: 1 path segment, 1 random string used so far)
          * /api/xyz/abc/def/ (Valid: 3 path segments, 3 random strings used so far)
          * /api/xyz/abc/ghi/ (Invalid: 4 different random strings were used for path segments in this test run)
          * /api/xyz/xyz/xyz/xyz/xyz/xyz/xyz/ (Invalid: 7 path segments)
    """

    string_pool = [
        "".join(random.choices(string.ascii_lowercase, k=5)) for _ in range(3)
    ]

    paths = []
    for _ in range(num_paths):
        num_segments = random.randint(1, 6)
        path = "/".join(random.choices(string_pool, k=num_segments))
        paths.append(path)
    return paths
