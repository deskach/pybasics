class User(object):
    """description of class"""

    def __init__(self, firstname, lastname, **kwargs):
        super().__init__(**kwargs)
        self.firstname = firstname
        self.lastname = lastname

        return None

    def initials(self):
        return "{}, {}.".format(
            self.firstname[0], 
            self.lastname[0])
