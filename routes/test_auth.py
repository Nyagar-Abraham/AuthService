# from helpers.config_test_client import test_client
#
#
#
#
# from datetime import datetime
#
# def test_signup_user():
#     response = test_client.post(
#         '/auth/signup',
#         json={
#             'username': 'test_user_1',
#             'password': 'PASSWORD',
#             'email': 'john_2@example.com',
#         }
#     )
#
#     assert response.status_code == 200
#     assert 'password' not in response.json()
#     assert response.json()['username'] == 'test_user_1'
#     assert response.json()['email'] == 'john_2@example.com'
#     assert response.json()['active'] is True
#     assert response.json()['role'] == 'user'
#     parsed_datetime = datetime.fromisoformat(response.json()['created_at'])
#     assert  isinstance(parsed_datetime,datetime)
#
# def test_signup_user_invalid_email():
#     response = test_client.post(
#         '/auth/signup',
#         json={
#             'username': 'test_user_1',
#             'password': 'PASSWORD',
#             'email': "john_2@example.com",
#         }
#     )
#     assert response.status_code == 400
#     assert response.json()['detail'][0]["msg"] ==  "value is not a valid email address: An email address must have an @-sign."
#
# def test_signup_user_email_already_registered():
#     response = test_client.post(
#         '/auth/signup',
#         json={
#             'username': 'test_user_1',
#             'password': 'PASSWORD',
#             'email': "john_3@example.com",
#         }
#     )
#
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Email already registered"