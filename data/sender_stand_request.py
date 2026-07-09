import requests
from data import data, configuration


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers.copy())
def get_new_user_token():
    response = post_new_user(data.user_body)
    auth_token = response.json()["authToken"]
    return {"Authorization": f"Bearer {auth_token}"}
def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)