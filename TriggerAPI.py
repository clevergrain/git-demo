"""
[Documentation] Code to call APIs on reqres server for the demo purpose
"""

import requests


class UserManagement():

    # email
    # password -
    # uid -

    def __init__(self, uid, email='', password=''):
        # initialize Email and Password
        self.uid = uid
        self.email = email
        self.password = password

    def get_user_from_uid(self):
        api_url = 'https://reqres.in/api/user/' + str(self.uid)
        response = requests.get(api_url)
        print (response.json())
        print (response.status_code)


if __name__ == '__main__':
    user_object = UserManagement(2)
    user_object.get_user_from_uid()