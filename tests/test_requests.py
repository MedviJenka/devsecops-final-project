from app.roast_request import RoastRequest


request = RoastRequest()


def test() -> None:
    outcome = request.send_roast_request('hello')
    print(outcome)
    assert '' in outcome


def test_ai_server_health() -> None:
    outcome = request.health_check()
    assert outcome == 200

