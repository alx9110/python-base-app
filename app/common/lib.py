""" Common lib """
def get_message():
    """ Print message """
    return 'Hello World!'

def get_json():
    """ get json """
    return {'key': 'value'}

def auth(login):
    """ Auth """
    if login.isdigit():
        return None
    return login
