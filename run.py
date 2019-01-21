from datetime import datetime
users_list = [
    {
        "userid": 0,
        "username": 'admin',
        "password": 'admin',
        "role": 'admin'
    }
]
comments = [
    {

    }
]
logged_in_users = []


class Auth():
    def __init__(self):
        pass

    def signup(self):
        """user register

        Keyword Arguments:
            role {user} -- [all users registereing will automatically be users] (default: {'user'})

        Returns:
            [message] -- [successful registered]
        """

        print('Enter your username')
        username = input()
        self.username = username
        name = [name for name in users_list if name['username'] == self.username]
        if name:
            return 'User already exist'
        print('Enter your password')
        password = input()
        self.password = password
        print('Please enter your password again')
        confirm = input()
        self.confirm = confirm
        if self.password != self.confirm:
            print('Passwords should match')
            print("PLease try agAIN")
            return self.signup()
        self.role = 'user'
        user_dict = {
            "userid": len(users_list) + 1,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

        users_list.append(user_dict)
        print("Successfully registered")

        return True

    def login(self):
        """user login"""

        print('Enter your username')
        username = input()
        self.username = username
        print('Enter your password')
        password = input()
        self.password = password
        self.timestamp = datetime.now()
        password = [password for password in users_list if password['password'] == self.password
                                          and password['username'] == self.username]
        if not password:
            print( 'Invalid password or username')
            return self.login()
        self.logged_in = True
        logged_in_users.append(self.username)
        print("logged in at {}".format(self.timestamp))
        return True


registration = Auth()
registration.signup()
registration.login()
