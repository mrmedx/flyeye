
#@funciton get query results, a list of all the titles and links in google search reusult pages from 0..N, based on the the queries 
def get_query_results(queries):
    from google.search.scraper import get_all_titles_and_links_list
    qreults= get_all_titles_and_links_list(queries)
    return qreults