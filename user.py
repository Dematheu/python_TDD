import requests


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.obtained_data = False

    def get_all_data(self):
        response = requests.get('')

        if response.ok:
            self.obtained_data = True
            return 'Connected'

        else:
            self.obtained_data = False
            return ('Error 404')
