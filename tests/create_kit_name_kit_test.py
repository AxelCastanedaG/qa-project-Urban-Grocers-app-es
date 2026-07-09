from data import data, sender_stand_request


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
def check_positive_kit_response(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]
def check_negative_kit_response(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
    assert kit_response.json() == {"error": "Invalid parameters"}
def test_create_kit_1_character_name_allowed():
    kit_body = get_kit_body("a")
    check_positive_kit_response(kit_body)
def test_create_kit_511_character_name_allowed():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    check_positive_kit_response(kit_body)
def test_create_kit_empty_character_name_not_allowed():
    kit_body = get_kit_body("")
    check_negative_kit_response(kit_body)
def test_create_kit_512_character_name_not_allowed():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    check_negative_kit_response(kit_body)
def test_create_kit_special_character_name_allowed():
    kit_body = get_kit_body("№%@")
    check_positive_kit_response(kit_body)
def test_create_kit_space_character_name_allowed():
    kit_body = get_kit_body("A Aaa")
    check_positive_kit_response(kit_body)
def test_create_kit_number_character_name_allowed():
    kit_body = get_kit_body("123")
    check_positive_kit_response(kit_body)
def test_create_kit_no_name_parameter_not_allowed():
    kit_body = {}
    check_negative_kit_response(kit_body)
def test_create_kit_no_string_character_name_not_allowed():
    kit_body = get_kit_body(123)
    check_negative_kit_response(kit_body)