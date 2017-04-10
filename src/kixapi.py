import urllib.request
import json

from user import User
from game import Game

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
        if( len(resp_list) == 1):
            new_user = User(resp_list[0])
            return new_user
        else:
            raise KeyError
        return None

    def GetGames(self):
        """Get A list of all the available games"""
        request = "games?limit=100"
        resp_list = self.MakeRequest(request)
        unknown = resp_list[0]
        game_list = []
        for game_dict in resp_list[1:]:
            new_game = Game(game_dict)
            game_list.append(new_game)
        return game_list



api = KixAPI()
api.GetUser("Kinokoio")
api.GetGames()
