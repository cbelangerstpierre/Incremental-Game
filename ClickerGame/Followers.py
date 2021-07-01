class Followers:
    def __init__(self):
        self.followers = 4
        self.followers_maker = 0

    def getFollowers(self):
        return self.followers

    def getFollowersMaker(self):
        return self.followers_maker

    def setFollowers(self, new_followers):
        self.followers = new_followers

    def setFollowersMaker(self, new_followers_maker):
        self.followers_maker = new_followers_maker
