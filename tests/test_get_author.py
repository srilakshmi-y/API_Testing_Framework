from utils.API import API
from utils.endpoints import ENDPOINTS


def test_get_author_all_details_200():
    """
    Test Case: Retrieve all authors (Valid Request)

    Objective:
    - Verify the API returns a 200 status code for a valid GET request to the "authors" endpoint.
    - Validate that the response is a list containing the required fields for each author.

    Steps:
    1. Send a GET request to the valid 'authors' endpoint.
    2. Assert the status code is 200 (OK).
    3. Verify the response is a list.
    4. Check each author entry contains the following fields:
       - 'id'
       - 'idBook'
       - 'firstName'
       - 'lastName'
    """
    get_response = API.get(ENDPOINTS['authors'])
    print(get_response.status_code)
    assert get_response.status_code == 200
    all_author_details = get_response.json()
    assert type(all_author_details) == list
    for author in all_author_details:
        assert "id" in author
        assert "idBook" in author
        assert "firstName" in author
        assert "lastName" in author


def test_get_author_invalid_endpoint_404():
    """
    Test Case: Retrieve authors from an invalid endpoint (Invalid Path)

    Objective:
    - Verify the API returns a 404 status code for a GET request to an incorrect endpoint.

    Steps:
    1. Send a GET request to the 'authors_invalid_get' endpoint.
    2. Assert the status code is 404 (Not Found).
    """
    get_response = API.get(ENDPOINTS['authors_invalid_get'])
    print(get_response.status_code)
    assert get_response.status_code == 404


def test_get_author_invalid_request_400():
    """
       Test Case: Retrieve author with an invalid request (Invalid ID)

       Objective:
       - Verify the API returns a 400 status code for a GET request with an invalid resource identifier.
       - Validate the response contains the correct error message and status code.

       Steps:
       1. Send a GET request to the 'authors_invalid_get1' endpoint with an invalid ID.
       2. Assert the status code is 400 (Bad Request).
       3. Validate the error details in the response, specifically:
          - 'status' field should be 400.
       """
    get_response = API.get(ENDPOINTS['authors_invalid_get1'])
    error_details = get_response.json()
    print(get_response.status_code)
    assert get_response.status_code == 400
    assert error_details['status'] == 400




