import time

class User:
    """Holds information about a Kixeye user"""
    def __init__(self, user_dict):
        """Obtains information from a dictionary"""
        self.id = user_dict["id"]
        self.username = user_dict["username"]
        self.googleId = user_dict.get("googleId")
        self.steamId = user_dict.get("steamId")
        self.FbTKFB = user_dict.get("facebookTokenForBusiness")
        self.facebookId = user_dict.get("facebookId")
        self.lastSeen = user_dict["lastSeen"]
        self.created = user_dict["created"]
        print(self.__repr__())

    def __repr__(self):
        rstr =  "ID: " + str(self.id) + "\n"
        rstr += "User Name: " + str(self.username) + "\n"
        rstr += "Google ID: " + str(self.googleId) + "\n"
        rstr += "Steam ID: " + str(self.steamId) + "\n"
        ls_time = time.ctime(self.lastSeen)
        rstr += "Last Seen: " + str(ls_time) + "\n"
        cr_time = time.ctime(self.created)
        rstr += "Created: " + str(cr_time) + "\n"
        return rstr
