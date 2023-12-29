#@function build the google query api
def get_search_api(query):
    from google.search.html import GOOGLE_API, NO_FILTER,START_FROM_PAGE,COUNTRY_IS
    from google.search.pages_counter import VISITED_PAGES
    return GOOGLE_API+query["dork"]+NO_FILTER+START_FROM_PAGE+VISITED_PAGES.get_str()+COUNTRY_IS+query["cr"]

#@function do google search with query
def get_search_results(session, query):
    from app.utility import log
    try:
        GOOGLE_API=get_search_api(query)#"countryUS"
        query_response=session.get(GOOGLE_API,cookies={})
        if query_response.status_code==200:
            return query_response.text
        elif query_response.status_code==429:
            log("Too Many Requests: try to change you ip address periodically.")
            from google.search.session import restart_session
            session=restart_session(session)
        else:
            log("Warnning: Google responded with status code "+query_response.status_code+", conduct a search for more information.")
    except Exception as ex:
        log("The current query failed: " + str(ex))   
    return None




