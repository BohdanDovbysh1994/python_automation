# import pytest
#
#
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             print("executing test failed", request.node.nodeid)
