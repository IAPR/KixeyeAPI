import urllib.request
import json

from user import User

class KixAPI:
    """Class for comunicating with Kixeye REST API (api.kixeye.com)"""
    api_url = "https://api.kixeye.com:443/api/v2/"
    user_limit = 100

    def __init__(self):
        pass

    def MakeRequest(self, request):
        """Makes the requests to the api, returns list of items from response"""
        url = self.api_url + request

        # Make request to the API
        print("API REQUEST:", url)
        try:
            fd = urllib.request.urlopen(url)
            response_str = fd.read().decode("utf-8")
            return json.loads(response_str)
        except:
            print("There was an error making the request")
            exit()

    def GetUser(self, username):
        """Finds a user by its username"""
        request = "users?username=" + str(username) + "&limit=" + str(self.user_limit)
        resp_list = self.MakeRequest(request)

        user_list = []
        for resp in resp_list:
            new_user = User(resp)
            user_list.append(new_user)
        return user_list


api = KixAPI()
api.GetUser("TonyMai")
