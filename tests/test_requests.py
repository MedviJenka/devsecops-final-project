import requests
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

    def test_nginx_is_up(self) -> None:
        url = "http://localhost:89/health"  # Replace with your Nginx URL
        response = requests.get(url)
        assert response.status_code == 200

    def test_nginx_serving_static_files(self) -> None:
        url = "http://localhost:88/static/images/roasted.gif"
        response = requests.get(url)
        assert response.status_code == 200
