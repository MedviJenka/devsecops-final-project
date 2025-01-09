class TestContainers:

    """
    for local tests change private ip config to http://localhost
    """

    def test_sanity(self) -> None:
        assert 1 + 1 == 2
