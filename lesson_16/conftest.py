import pytest


@pytest.fixture(scope="function", autouse=True)
def after_fail_action(request):
    yield
    if request.node.session.testsfailed:
        print(f"Tests failed: {request.node.session.testsfailed}")

