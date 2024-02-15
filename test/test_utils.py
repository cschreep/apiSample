from api_counter.utils import gen_paths


def test_gen_paths():
    num_paths = 100
    paths = gen_paths(num_paths)
    assert num_paths == len(paths)
    for path in paths:
        path = path.lstrip("/api/")
        assert len(path.split("/")) <= 6, path
