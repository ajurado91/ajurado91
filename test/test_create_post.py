#
# @test_create_post.py Copyright (c) 2022 Jalasoft
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

import http
import json
import allure
import pytest
from assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
from model.login import Login


def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    TOKEN = Login().get_token()


@pytest.fixture
def teardown_delete_test():
    global ID_POST
    pass
    yield
    URL = config("URL")
    crud_post = CrudPost(TOKEN)
    crud_post.delete_post(URL, ID_POST)


@pytest.mark.acceptance_testing
@pytest.mark.smoke_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
def test_create_post():

    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post.json")
    response = crud_post.create_post(url, payload)
    response_dict = json.loads(response.response.text)
    allure.attach(json.dumps(response_dict, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)
    id_post = response_dict['id']
    crud_post.delete_post(url, id_post)



@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@pytest.mark.sanity_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
def test_create_post_with_a_valid_id():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_valid_id.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text['id']).is_instance_of(int)
    allure.attach(str(response_text['id']), 'Post id:', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.severity("trivial")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
def test_create_post_with_a_publish_status():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_publish_status.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response_text['status']).is_equal_to("publish")
    allure.attach(str(response_text['status']), 'Status post by default', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_create_post_with_standard_format_by_default():

    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_default_standard_format.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response_text['format']).is_equal_to("standard")
    allure.attach(str(response_text['format']), 'format post by default', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_create_post_with_void_title():

    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_void_title.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)

@pytest.mark.negative_testing
@pytest.mark.regression_testing
@pytest.mark.sanity_testing
@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
def test_create_post_with_void_status():
    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_void_status.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['data']['details']['status']['code']).is_equal_to('rest_not_in_enum')
    allure.attach(str(response_text['data']['details']['status']['code']), 'Code to void status', allure.attachment_type.TEXT)
    assert_that(response_text['data']['details']['status']['data']).is_equal_to(None)
    allure.attach(str(response_text['data']['details']['status']['data']), 'Null status', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)

@pytest.mark.negative_testing
@pytest.mark.regression_testing
@pytest.mark.sanity_testing
@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
def test_create_post_with_invalid_author_id():

    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_invalid_author_id.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['code']).is_equal_to('rest_invalid_author')
    allure.attach(str(response_text['code']), 'Code to invalid author', allure.attachment_type.TEXT)
    assert_that(response_text['message']).is_equal_to('Invalid author ID.')
    allure.attach(str(response_text['message']), 'Message to invalid author', allure.attachment_type.TEXT)
    allure.attach(str(response.request.url), 'URL', allure.attachment_type.TEXT)
    allure.attach(str(response.request.method), 'Method', allure.attachment_type.TEXT)

