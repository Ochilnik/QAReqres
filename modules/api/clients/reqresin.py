import requests


class Reqres:
    def list_users(self):
        r = requests.get('https://reqres.in/api/users?page=2')
        body = r.json()
        return body
    
    def list_user(self, user_number):
        r = requests.get(f'https://reqres.in/api/users/{user_number}')
        body = r.json()
        return body

    def list_resources(self):
        r = requests.get('https://reqres.in/api/unknown')
        body = r.json()
        return body

    def list_resource(self, res_number):
        r = requests.get(f'https://reqres.in/api/unknown/{res_number}')
        body = r.json()
        return body    