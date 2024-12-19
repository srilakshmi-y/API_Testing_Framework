import pytest
from utils.API import API
from utils.endpoints import ENDPOINTS
from utils.data_loader import load_json_file


# Fixture to provide a valid payload for POST requests
@pytest.fixture
def post_payload_valid_author():
    json_payload = load_json_file("data/request_payloads/post_author_valid.json")
    return json_payload


# Fixture to provide a invalid payload for POST requests
@pytest.fixture
def post_payload_invalid_author():
    json_payload = load_json_file("data/request_payloads/post_author_invalid.json")
    return json_payload


def test_post_author_200(post_payload_valid_author):
    """
    Test Case: Create a new author with valid payload (Status 200)

    Objective:
    - Verify the API successfully creates a new author when provided with a valid payload.

    Steps:
    1. Send a POST request to the valid 'authors' endpoint with a valid payload.
    2. Assert the status code is 200 (OK).
    3. Validate the response contains the same 'firstName' and 'lastName' as in the payload.

    Parameters:
        post_payload_valid_author (fixture): A valid payload for creating an author.
    """
    post_response = API.post(ENDPOINTS['authors'], post_payload_valid_author)
    print(post_response.status_code)
    assert post_response.status_code == 200
    author_details = post_response.json()
    print(author_details)
    assert author_details['firstName'] == post_payload_valid_author['firstName']
    assert author_details['lastName'] == post_payload_valid_author['lastName']


def test_post_author_invalid_404(post_payload_valid_author):
    """
        Test Case: Attempt to create an author using an invalid endpoint (Status 404)

        Objective:
        - Verify the API returns a 404 status code when a POST request is sent to an incorrect endpoint.

        Steps:
        1. Send a POST request to the 'authors_invalid' endpoint with a valid payload.
        2. Assert the status code is 404 (Not Found).

        Parameters:
            post_payload_valid_author (fixture): A valid payload for creating an author.
        """
    post_response = API.post(ENDPOINTS['authors_invalid'], post_payload_valid_author)
    print(post_response.status_code)
    assert post_response.status_code == 404


def test_post_author_invalid_payload_400(post_payload_invalid_author):
    """
    Test Case: Attempt to create an author using an invalid payload (Status 400)

    Objective:
    - Verify the API returns a 400 status code when provided with an invalid payload.

    Steps:
    1. Send a POST request to the valid 'authors' endpoint with an invalid payload.
    2. Assert the status code is 400 (Bad Request).

    Parameters:
        post_payload_invalid_author (fixture): An invalid payload for creating an author.
    """
    post_response = API.post(ENDPOINTS['authors'], post_payload_invalid_author)
    print(post_response.status_code)
    assert post_response.status_code == 400










