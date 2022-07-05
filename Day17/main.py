class User:
    #pass    # can leave the class empty if you just want to declare it and not define it, use pass keyword
            # classes use PascalCase (EveryNewWord's starting letter should be Caps)
            # camelCase
            # snake_case
    #constructor: special function known by python and it is known because it has two underscores at the starting of it and the ending of it
        # def __init__(self):   self is the actual object that is being created or being initialized.
                            # in addition to self you can pass as many parameters as you want and that parameter is
                            # going to be passed in when an object gets constructed from this class.
                            # once you recieve this data you can use it to set the object's attributes
            #initialize attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user):   #unlike a function, a method always needs to have a self parameter as the first parameter
        user.followers += 1 #this means that when this method is called, it knows the object that called it.
        self.following += 1

user_1 = User("001", "tanish")
print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_2 = User("002", "muskan")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
