from utils.API import API
from utils.config import ID_PARAM
from utils.endpoints import ENDPOINTS


def test_delete_author_by_id_200():
    """
     Test Case: Delete an existing author by a valid ID (Status 200)

     Objective:
     - Verify the API successfully deletes an author when a valid ID is provided.

     Steps:
     1. Send a DELETE request to the 'authors' endpoint with a valid ID.
     2. Assert the response status code is 200 (OK), indicating successful deletion.

     Parameters:
         ID_PARAM['ID_PARAM_Valid2']: A valid ID for an existing author.
     """
    delete_response = API.delete(ENDPOINTS['authors'], ID_PARAM['ID_PARAM_Valid2'])
    print("ID------>", ID_PARAM['ID_PARAM_Valid2'])
    print(delete_response.status_code)
    assert delete_response.status_code == 200


def test_delete_author_by_invalid_id_400():
    """
    Test Case: Attempt to delete an author using an invalid ID (Status 400)

    Objective:
    - Verify the API returns a 400 status code when a DELETE request is sent with an invalid ID format.

    Steps:
    1. Send a DELETE request to the 'authors' endpoint with an invalid ID (non-integer value).
    2. Assert the response status code is 400 (Bad Request).

    Parameters:
        ID_PARAM['ID_PARAM_invalid1']: An invalid ID in the form of a string.
    """
    delete_response = API.delete(ENDPOINTS['authors'], ID_PARAM['ID_PARAM_invalid1'])
    print(delete_response.status_code)
    assert delete_response.status_code == 400


def test_delete_author_by_missing_id_400():
    """
    Test Case: Attempt to delete an author without providing an ID (Status 400)

    Objective:
    - Verify the API returns a 400 status code when a DELETE request is sent with a missing ID.

    Steps:
    1. Send a DELETE request to the 'authors' endpoint without providing an ID.
    2. Assert the response status code is 400 (Bad Request).

    Parameters:
        None: No ID is provided for the DELETE request.
    """
    delete_response = API.delete(ENDPOINTS['authors'], None)
    print(delete_response.status_code)
    assert delete_response.status_code == 400


def test_delete_author_by_invalid_string_id_endpoint_404():
    """
    Test Case: Attempt to delete an author using an invalid endpoint (Status 404)

    Objective:
    - Verify the API returns a 404 status code when a DELETE request is sent to an incorrect endpoint.

    Steps:
    1. Send a DELETE request to the 'authors_invalid3' endpoint with an invalid ID.
    2. Assert the response status code is 404 (Not Found).

    Parameters:
        ENDPOINTS['authors_invalid3']: An invalid endpoint path.
        ID_PARAM['ID_PARAM_invalid1']: An invalid ID in the form of a string.
    """
    delete_response = API.delete(ENDPOINTS['authors_invalid3'], ID_PARAM['ID_PARAM_invalid1'])
    print(delete_response.status_code)
    assert delete_response.status_code == 404








