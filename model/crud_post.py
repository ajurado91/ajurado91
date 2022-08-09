#
# @crud_post.py Copyright (c) 2022 Jalasoft
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

from utils.api_request import APIRequest


class CrudPost:

    def __init__(self, token):
        self.headers = {
            'Authorization': token
        }
        self.params = {
            'mo_rest_api_test_config': 'jwt_auth'
        }

    def create_post(self, url, payload):

        response = APIRequest().post(url, payload, self.headers, self.params)
        return response

    def delete_post(self, URL, id_post):
        url = "{}/{}".format(URL, id_post)

        response = APIRequest().delete(url, self.headers, self.params)

        return response

    def retrieve_post(self, url, id_post):

        new_url = "{}/{}".format(url, id_post)

        response = APIRequest().get(new_url, self.headers, self.params)
        return response

    def update_post(self, url, id, payload):
        new_url = "{}/{}".format(url, id)
        response = APIRequest().post(new_url, payload, self.headers, self.params)
        return response
