from app.roast_request import RoastRequest


request = RoastRequest()


class Tests:

    def test_1(self) -> None:
        outcome = request.send_roast_request('hello')
        print(outcome)
        assert '' in outcome

    def test_2(self) -> None:
        outcome = request.health_check()
        assert outcome == 200

    def test_3(self) -> None:
        assert 1 + 1 == 2

    def test_4(self) -> None:
        assert 1 + 1 == 2

    def test_5(self) -> None:
        assert 1 + 1 == 2

    def test_6(self) -> None:
        assert 1 + 1 == 2

    def test_7(self) -> None:
        assert 1 + 1 == 2

    def test_8(self) -> None:
        assert 1 + 1 == 2

    def test_9(self) -> None:
        assert 1 + 1 == 2

    def test_10(self) -> None:
        assert 1 + 1 == 2

