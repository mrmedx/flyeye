from app.utility import log
#@function
def get_search_count(soup):
    from google.search.html import SEARCH_STATUS_TEXT_ID
    search_status = soup.find(id=SEARCH_STATUS_TEXT_ID)
    if search_status:
        return search_status.text
    return None

#@print search count
def print_search_count(search_status):
    if search_status:
        from platform import system as checksys
        if checksys() == 'Windows':
            log(search_status)            
        else:
            log(f"\033[38;2;0;128;0m{search_status}\033[0m")#gren color

#function extract a list of titles, and links from html elements in @html return the final list.
def extract_titles_and_links(elements):
    qresult=[]
    for element in elements:
        try:
            title_text_elem = element.find('h3')
            title_text=None
            if title_text_elem:
                title_text =title_text_elem.text.strip()

            link_elem = element.find('a')
            link=None
            if link_elem:
                link=link_elem['href'].strip()
                if link[0]=='/':# ignore links start with /
                    continue

            from google.search.html import SEARCH_SNIPPET_CLASS_NAME
            snippet_elem= element.find(class_=SEARCH_SNIPPET_CLASS_NAME)
            snippet=None
            if snippet_elem:
                snippet=snippet_elem.get_text()

            if title_text!=None and link!=None and snippet!=None:
                qresult.append({"title":title_text, "link":link,"snippet":snippet})

        except Exception as ex:
            print("failed to extract the current search result :" + str(ex)+"\nContinue...")
    return qresult
    
#@function returns teh extracted titles and links list from @html
def get_titles_and_links_list(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    search_status = get_search_count(soup)
    print_search_count(search_status)
    from google.search.html import ALL_SEARCH_RESULTS_ELEMENTS_ID as ALL_SEARCH_RESULTS_ID
    search_element = soup.find(id=ALL_SEARCH_RESULTS_ID)
    elements=[]
    if search_element:
        from google.search.html import SINGLE_SEARCH_RESULT_ELEMENT_CLASS_NAME as SSEARCH_RESUTL
        elements = search_element.find_all('div', class_=SSEARCH_RESUTL)
        log(len(elements))
    return extract_titles_and_links(elements)

#@function @analysis_callback on each @titles_and_links_list item.
def scan_link(analysis_callback,titles_and_links_list):
    for item in titles_and_links_list:
        #analysis_callback(item["title"])
        from urllib.parse import unquote
        analysis_callback(unquote(item["link"]))
        #analysis_callback(item["snippet"])
        

#@fucntion to research after wait 30s if no response is comes from the prev request.
def wait_for_search_results(session,query):
    from google.search.search import get_search_results
    search_results = get_search_results(session,query) # get the google search results using @query page 0.
    while not search_results:
        print("No search results using the current query, try again after 30 seconds..")
        from app.utility import sleep_for
        sleep_for(30)
        from google.search.session import restart_session
        session=restart_session(session)
        search_results = get_search_results(session,query)
    return search_results

#@function detect digital flies said a keyword in the target keywords extracted from said param.
def detect_said_flies(titles_and_links_list,kwds_list):
    if len(kwds_list)==0:
        return
    from google.data.analysis import detect_digital_flies_said
    for target_keyword in kwds_list:
        if len(target_keyword)==0:
            continue
        log("detect digital flies talking about: "+target_keyword+"...")
        detect_digital_flies_said(titles_and_links_list, target_keyword)


#@function gets all titles and links from all availables search results pages not just the first page.
#@param search_results that contains all the search result pages.
#@param all_titles_and_links_list , a list to append the titles and links in each search result page.
#@param session, the current session
#@param query, the current gogole search query
def scan_titles_and_links_from_all_pages(search_results,all_titles_and_links_list,session,query):
    titles_and_links_list = get_titles_and_links_list(search_results) # the titles and links in the first page.
    while len(titles_and_links_list)>0:
        all_titles_and_links_list.extend(titles_and_links_list)
        from time import time
        start_print_time = time()#start time

        from google.data.analysis import color_interested_data
        scan_link(color_interested_data,titles_and_links_list)#callback for titles_and_links_list in the current page. 
        
        #detect digital flies said a keyword in the target keywords extracted from said param.
        detect_said_flies(titles_and_links_list,query["kwds"])
          
        end_print_time = time()#end time
        time_taken =end_print_time-start_print_time
        print("time taken in the current page: ", end_print_time-start_print_time)
        if time_taken<30:
            log("Waiting for 30 seconds before continue...")
            from app.utility import sleep_for
            sleep_for(30)
        else:
            log(f"Waiting for 3 seconds before continue...")
            from app.utility import sleep_for
            sleep_for(3)

        from google.search.pages_counter import VISITED_PAGES
        VISITED_PAGES.next() # move to the next page.
        search_results = wait_for_search_results(session,query) # get the search_results of the current page.
        titles_and_links_list = get_titles_and_links_list(search_results) # get titles and links of the curr page.


#@function get query result
#@param queries , a list of google queries 
def get_all_titles_and_links_list(queries):
    all_titles_and_links_list=[]
    from google.search.session import get_new_session
    for query in queries:
        session = get_new_session()
        search_results = wait_for_search_results(session,query) # get the google search results using @query page 0.
        scan_titles_and_links_from_all_pages(search_results,all_titles_and_links_list,session,query)
        from google.search.pages_counter import VISITED_PAGES
        VISITED_PAGES.back_to_zero() #set the visited page to 0 because we finish with the curr query.
        session.close()
        from app.utility import sleep_for
        sleep_for(3)
    return all_titles_and_links_list

