from InstagramAPI import InstagramAPI

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers_ = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers_.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers_

def getTotalFollowing(api, user_id):
    API.getUsernameInfo(user_id)
    API.LastJson
    following_ = []
    next_max_id = True
    while next_max_id:
        print next_max_id
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = API.getUserFollowings(user_id, maxid=next_max_id)
        following_.extend(API.LastJson.get('users', []))
        next_max_id = API.LastJson.get('next_max_id', '')
        return following_

def getUsernames(initial):
    usernames = []

    for obj in initial:
        usernames.append(obj["username"]);
    return usernames


if __name__ == "__main__":
	f = open('user.txt', 'r')
	user = ["username", "password"]

	i = 0
	for line in f:
		user[i] = line[:-1]
		i += 1

	print(user)

	API = InstagramAPI(user[0], user[1])
	API.login()
	
	user_id = API.username_id

	followers = getUsernames(getTotalFollowers(API, user_id))
	following = getUsernames(getTotalFollowing(API, user_id))

	nonmutuals = [x for x in following if x not in followers]

	print(nonmutuals)

	f = open('nonmutuals.txt', 'w')

	for username in nonmutuals:
  		f.write("%s\n" % username)
