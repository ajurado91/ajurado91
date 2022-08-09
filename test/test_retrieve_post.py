#
# @test_retrieve_post.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import allure
import pytest
from http import HTTPStatus
from assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
import json
from model.login import Login
from utils.schema_validator import SchemaValidator

TOKEN = None


def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_retrieve_test/payload_create_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).response.text)
    ID_POST = api_request_response['id']
    yield
    crud_post.delete_post(URL, ID_POST)


@pytest.mark.sanity_testing
@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@pytest.mark.smoke_testing
@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.epic("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
def test_retrieve_an_existing_post():
    URL = config('URL')

    crud_post = CrudPost(TOKEN)
    api = crud_post.retrieve_post(URL, ID_POST)
    response_text = json.loads(api.response.text)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('id')
    assert_that(response_text['id']).is_instance_of(int)
    assert_that(response_text['id']).is_equal_to(ID_POST)


@pytest.mark.security_testing
@pytest.mark.sanity_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("security_testing")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.epic("security_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
def test_retrieve_a_post_with_a_bad_token():
    URL = config('URL')
    TOKEN = "Bearer abc12345"
    crud_post = CrudPost(TOKEN)

    api = crud_post.retrieve_post(URL, ID_POST)
    response_text = json.loads(api.response.text)

    assert_that(api.response.status_code).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('401')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("blackbox_testing")
@allure.epic("regression_testing")
def test_retrieve_a_post_with_a_bad_id():
    URL = config('URL')
    ID_POST = 900

    crud_post = CrudPost(TOKEN)

    api_request_response = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api_request_response.response.text)

    assert_that(api_request_response.response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('rest_post_invalid_id')
    assert_that(response_text).contains('message')
    assert_that(response_text['message']).is_equal_to('Invalid post ID.')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("blackbox_testing")
@allure.epic("regression_testing")
def test_retrieve_a_post_with_a_bad_route():
    URL = '{}/bad_route'.format(config('URL'))

    crud_post = CrudPost(TOKEN)

    api = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api.response.text)

    assert_that(api.response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('rest_no_route')
    assert_that(response_text).contains('message')
    assert_that(response_text['message']).is_equal_to('No route was found matching the URL and request method.')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.severity("normal")
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("blackbox_testing")
@allure.epic("regression_testing")
def test_retrieve_schema_validator():
    URL = config('URL')

    crud_post = CrudPost(TOKEN)
    api = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api.response.text)

    expected_schema = load_json_expected_result("resources/resource_retrieve_test/schema_retrieve_post.json")

    validator = SchemaValidator(expected_schema, True)

    is_validate = validator.validate(response_text)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(is_validate).is_true()
