import onelogin
# specify user_name, user_secret, and shard (us or eu)
Remind_log = {'client_id':'',
     'user_secret':'',
     'shard':'US'}

token = onelogin.Token(**Remind_log)
# Create the user object with the token created
user = onelogin.User(token)

# define the user, or build the user object from a csv file,
# To create a user, include the firstname, lastname, email, and username
# attribute.
new_user = {
    'firstname':'Victoria',
    'lastname':'Wade',
    'email':'victoria.wade@gmail.local',
    'username':'victoria001'
}

# Search to see if the user exists based on email, if not, create a new user

if user.user_exists(new_user['email']):
    found_user = user.get_user_by_id(
        user.search_users(
            'email',new_user['email'])[0]['data'][0]['id']
    )
    print "Can not create user, already exists \r\n {0}".format(found_user)
else:
    Foo = user.create_user(**new_user)
    user_id = Foo['data'][0]['id']
    print 'Created User: {0}'.format(new_user)
