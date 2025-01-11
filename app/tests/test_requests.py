import debugpy


class TestContainers:

    """
    for local tests change private ip config to http://localhost
    """

    def test_sanity(self) -> None:
        assert 1 + 1 == 2

    def test_network(self) -> None:
        debugpy.listen(('0.0.0.0', 89))
