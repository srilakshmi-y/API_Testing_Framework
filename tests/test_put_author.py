import pytest
from utils.API import API
from utils.config import ID_PARAM
from utils.endpoints import ENDPOINTS
from utils.data_loader import load_json_file


# Fixture to provide a valid payload for PUT requests
@pytest.fixture
def put_payload_valid_author():
    json_payload = load_json_file("data/request_payloads/put_author_valid.json")
    return json_payload


# Fixture to provide a invalid payload for PUT requests
@pytest.fixture
def put_payload_invalid_author():
    json_payload = load_json_file("data/request_payloads/put_author_invalid.json")
    return json_payload


def test_put_author_by_id_200(put_payload_valid_author):
    """
     Test Case: Update an existing author by ID with a valid payload (Status 200)

     Objective:
     - Verify the API successfully updates an existing author when provided with a valid payload.

     Steps:
     1. Send a PUT request to the valid 'authors' endpoint with a valid ID and payload.
     2. Assert the status code is 200 (OK).
     3. Validate the response contains the updated 'firstName' and 'lastName' fields.

     Parameters:
         put_payload_valid_author (fixture): A valid payload for updating an author.
     """
    put_response = API.put(ENDPOINTS['authors'], ID_PARAM['ID_PARAM_Valid'], put_payload_valid_author)
    print(put_response.status_code)
    assert put_response.status_code == 200
    author_details = put_response.json()
    print(author_details)
    assert author_details['firstName'] == put_payload_valid_author['firstName']
    assert author_details['lastName'] == put_payload_valid_author['lastName']


def test_put_author_invalid_404(put_payload_valid_author):
    """
    Test Case: Attempt to update an author using an invalid endpoint (Status 404)

    Objective:
    - Verify the API returns a 404 status code when a PUT request is sent to an incorrect endpoint.

    Steps:
    1. Send a PUT request to the 'authors_invalid_put' endpoint with a valid payload.
    2. Assert the status code is 404 (Not Found).

    Parameters:
        put_payload_valid_author (fixture): A valid payload for updating an author.
    """
    put_response = API.post(ENDPOINTS['authors_invalid_put'], put_payload_valid_author)
    print(put_response.status_code)
    assert put_response.status_code == 404


def test_put_author_invalid_payload_400(put_payload_invalid_author):
    """
    Test Case: Attempt to update an author using an invalid payload (Status 400)

    Objective:
    - Verify the API returns a 400 status code when provided with an invalid payload for the update.

    Steps:
    1. Send a PUT request to the valid 'authors' endpoint with a valid ID and an invalid payload.
    2. Assert the status code is 400 (Bad Request).

    Parameters:
        put_payload_invalid_author (fixture): An invalid payload for updating an author.
    """
    put_response = API.put(ENDPOINTS['authors'], ID_PARAM['ID_PARAM_Valid'], put_payload_invalid_author)
    print(put_response.status_code)
    assert put_response.status_code == 400
