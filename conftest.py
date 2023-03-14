import pytest


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
