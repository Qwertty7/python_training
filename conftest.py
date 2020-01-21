

import pytest
from fixture.application import Application

# 1 fixture for all session (scope="session")
@pytest.fixture(scope ="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture