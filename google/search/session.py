#@function 
def get_new_session():
    import requests
    SESSION = requests.Session()
    from google.search.html import HEADERS
    SESSION.headers=HEADERS
    from google.search.html import PARAMS
    SESSION.params=PARAMS
    return SESSION


#@funciton , close the current session and get a new one.
def restart_session(session):
    try:
        session.close()
    except:
        pass
    return get_new_session()