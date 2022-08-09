#
# @api_request.py Copyright (c) 2022 Jalasoft
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

from dataclasses import dataclass
import requests

import requests
from requests import Request


@dataclass
class RequestApi:
    url: str
    method: str
    as_dict: dict
    headers: dict


@dataclass
class ResponseApi:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    url: str


@dataclass
class Api:
    request: RequestApi
    response: ResponseApi


class APIRequest:

    def get(self, url, headers, params):
        request = requests.Request(method="GET", url=url, headers=headers, params=params)
        request_prepared = request.prepare()

        request_api = self.get_requests(request_prepared)
        response = requests.Session().send(request_prepared)
        response_api = self.__get_responses(response)
        return self.__get_apis(request_api, response_api)

    def post(self, url, payload, headers, params):
        request = requests.Request(method="POST", url=url, data=payload,
                                   headers=headers, params=params)
        request_prepared = request.prepare()

        request_api = self.get_requests(request_prepared)
        response = requests.Session().send(request_prepared)
        response_api = self.__get_responses(response)
        return self.__get_apis(request_api, response_api)

    def delete(self, url, headers, params):
        request = requests.Request(method="DELETE", url=url, headers=headers, params=params)
        request_prepared = request.prepare()

        request_api = self.get_requests(request_prepared)
        response = requests.Session().send(request_prepared)
        response_api = self.__get_responses(response)
        return self.__get_apis(request_api, response_api)

    def __get_responses(self, response):
        url_response = response.url
        status_code = response.status_code
        text_response = response.text
        try:
            as_dict_response = response.json()
        except Exception:
            as_dict_response = {}
        headers_response = response.headers
        return ResponseApi(status_code, text_response, as_dict_response,
                                   headers_response, url_response)


    def get_requests(self, request_prepared):

        url_request = request_prepared.url
        method_request = request_prepared.method
        headers_request = request_prepared.headers
        try:
            as_dict_request = request_prepared.json()
        except Exception:
            as_dict_request = {}

        return RequestApi(url_request, method_request, as_dict_request,
                                 headers_request)

    def __get_apis(self, request_api, response_api):
        return Api(request_api, response_api)
