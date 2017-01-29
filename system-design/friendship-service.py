class FriendshipService:

    def __init__(self):
        # initialize your data structure here.
        self.followers = {}
        self.followings = {}

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def get_followers(self, user_id):
        # Write your code here
        result = []
        if user_id in self.followers:
            result = list(self.followers[user_id])
        result.sort()
        return result

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def get_followings(self, user_id):
        # Write your code here
        result = []
        if user_id in self.followings:
            result = list(self.followings[user_id])
        result.sort()
        return result

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.followers:
            self.followers[from_user_id] = set()
        self.followers[from_user_id].add(to_user_id)
        if to_user_id not in self.followings:
            self.followings[to_user_id] = set()
        self.followings[to_user_id].add(from_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id in self.followers:
            self.followers[from_user_id].discard(to_user_id)
        if to_user_id in self.followings:
            self.followings[to_user_id].discard(from_user_id)

