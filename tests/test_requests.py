from app.roast_request import RoastRequest


def test() -> None:
    request = RoastRequest()
    outcome = request.send_roast_request('hello')
    assert '' in outcome


def test_ai_server_health() -> None:
    request = RoastRequest()
    outcome = request.health_check()
    assert outcome == 200

