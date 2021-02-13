import SMS
from xbox.webapi.scripts import friends, authenticate

# for first time authentication (paste credential information into __init__.py)
# if token expires you must delete the tokens.json file to request a new one
# then run xbox-authenticate --client-id <client-id> --client-secret <client-secret>

# gamertags of friends you'd like to be notified if they are online
bois = ['gamertag1','gamertag2','gamertag3']

def online_friends(mydict):
    
    # parse online friends from the resp dictionary
    online_friends_list = []
    online_games_list = []

    for friend in mydict['people']:
        if friend['presence_state'] == 'Online':
            online_friends_list.append(friend['gamertag'])
            online_games_list.append(friend['presence_text'])
    # print(online_friends_list)
    # print(online_games_list)

    return online_friends_list, online_games_list

def online_bois(online_friends_list):
    # compare online friends with specified friends list
    online_bois_list = []
    online_bois_games = []

    i = 0
    for friend in online_friends_list:
        if friend in bois:
            online_bois_list.append(friend)
            online_bois_games.append(online_games_list[i])
        i = i+1

    # print(online_bois_list)
    return online_bois_list, online_bois_games

def notify(online_bois_list, online_bois_games):
    # use SMS module to send text to yourself with a list of active friends
    if not online_bois_list:
        message = 'No bois are online.'
    else:
        message = 'The following bois are online.'
        i = 0
        for friend in online_bois_list:
            message = message + '\n' + friend + ' - ' + online_bois_games[i]
        i = i + 1
    print(message)
    SMS.send(message)

# retrieve xbl friends information from server, parse the dictionary, and send a message
mydict = friends.main()
online_friends_list, online_games_list = online_friends(mydict)
online_bois_list, online_bois_games = online_bois(online_friends_list)
notify(online_bois_list, online_bois_games)
