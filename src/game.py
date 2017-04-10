class Game:
    """Games released and in development by Kixeye"""
    def __init__(self, gd):
        self.id = gd.get("id")
        self.host = gd.get("host")
        self.name = gd.get("name")
        self.shortName = gd.get("shortName")
        self.urlName = gd.get("urlName")
        self.path = gd.get("path")
        self.platform = gd.get("platform")
        self.display = gd.get("display")
        self.userAnalyticsShortName = gd.get("userAnalyticsShortName")
        self.inviteOnly = gd.get("inviteOnly")
        self.comingSoon = gd.get("comingSoon")
        self.metaDescription = gd.get("metaDescription")
        self.videoURL = gd.get("videoURL")
        self.metaTitle = gd.get("metaTitle")
        self.metaKeywords = gd.get("metaKeywords")
        self.forceSidebarPin = gd.get("forceSidebarPin")
        self.youTubeVideoId = gd.get("youTubeVideoId")
        self.titleId = gd.get("titleId")
        self.deviceFingerPrinting = gd.get("deviceFingerPrinting")
        self.applicationInstanceName = gd.get("applicationInstanceName")
        self.seGameId = gd.get("seGameId")
        self.paymentStartUrl = gd.get("paymentStartUrl")
        self.paymentCompleteUrl = gd.get("paymentCompleteUrl")
        print(self.__str__())

    def __str__(self):
        return self.name
