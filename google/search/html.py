HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

PARAMS= {
    "credentials": "include",
    "referrer": "https://www.google.com/",
    "method": "GET",
    "mode": "cors"
}

#@SEARCH_RESULTS_ELEMENT_ID , all the search results element.
ALL_SEARCH_RESULTS_ELEMENTS_ID="search"
#@SEARCH_RESULT_ELEMENT_CLASS_NAME , single search result element class name. 
SINGLE_SEARCH_RESULT_ELEMENT_CLASS_NAME="MjjYud"

#@GOOGLE_API google api used for web search
GOOGLE_API="https://www.google.com/search?q="
#@NO_FILTER parameter
NO_FILTER="&filter=0"
#@START_FROM_PAGE start search from a page ex:10
START_FROM_PAGE="&start="
#@COUNTRY find results for target country
COUNTRY_IS="&cr="#countryDZ
#@SEARCH_STATUS_TEXT_ID , the google search result status text html element id.
SEARCH_STATUS_TEXT_ID="result-stats"
#@SEARCH_SNIPPET_CLASS_NAME
SEARCH_SNIPPET_CLASS_NAME="kb0PBd cvP2Ce"