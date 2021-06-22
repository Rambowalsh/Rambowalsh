# Third-party imports...
from nose.tools import assert_true
import requests


def test_request_response():
    # Send a request to the API server and store the response.
    url = f"https://063qqrtqth.execute-api.eu-west-2.amazonaws.com/v1/weather?location=<designArea>"
    header={"x-api-key": "f661f74e-20a7-4e9f-acfc-041cfb846505"}
    response = requests.get(url,headers=header)
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)