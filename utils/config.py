# Base URL for the API being tested
BASE_URL = "https://fakerestapi.azurewebsites.net"

# Default HTTP headers used for API requests
HEADERS = {
    "Content-Type": "application/json"
}

# Predefined ID parameters for testing different scenarios
# These IDs are used to test valid and invalid cases for CRUD operations.
ID_PARAM = {
    "ID_PARAM_Valid": 1001,
    "ID_PARAM_Valid1": 2,
    "ID_PARAM_Valid2": 590,
    "ID_PARAM_invalid": 999999,
    "ID_PARAM_invalid1": "f43E"

}
