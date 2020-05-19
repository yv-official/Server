class Error(Exception):
   """ Base class for other exceptions """
   pass
class UsernameAlreadyExist(Error):
    """ Raised When User Already exist """
    pass
class EmailAlreadyExist(Error):
    """ Raised When User Email already Exist """
    pass
class SomethingWentWrong(Error):
    """ Raised When Something Went Wrong """
    pass
class AuthenticationFailed(Error):
    """ Raised When Authentication Failed """
    pass
class UserDoesNotExist(Error):
    """ Raised When User Does not exist """
    pass