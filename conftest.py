import pytest


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    """
       Fixture to perform setup and teardown actions for the test session.

       Features:
       - scope='session': This fixture runs once before any tests start and once after all tests complete.
       - autouse=True: This fixture is automatically applied to all tests without being explicitly requested.
       """
    print("First Test Execution Started ...")
    yield
    print("Last Test Execution Done !!!")