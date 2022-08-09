#
# @login.py Copyright (c) 2022 Jalasoft
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

import requests
from decouple import config


class Login:

    def login(self, url, user, password):
        _url = url
        headers = {}
        params = {
            "mo_rest_api_test_config": "jwt_auth"
        }
        payload = {
            'username': user,
            'password': password
        }

        response = requests.post(url, data=payload, headers=headers, params=params)

        return response

    def get_token(self):

        URI_TOKEN = config('URI_TOKEN')
        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

        response_login = self.login(URI_TOKEN, USER_NAME, PASSWORD).json()

        TOKEN = response_login['token_type'] + ' ' + response_login['jwt_token']

        return TOKEN