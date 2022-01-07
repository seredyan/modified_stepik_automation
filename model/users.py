


class User:

    def __init__(self, email=None, password=None):

        self.email = email
        self.password = password



    def __repr__(self):
        return "%s:%s:" % (self.email, self.password)


    def __eq__(self, other):
        return self.email == other.username



