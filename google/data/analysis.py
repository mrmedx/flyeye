#@function
def color_interested_data(text:str):
    from google.data.highlight import detect_emails
    emails_detected=detect_emails(text)
    from google.data.highlight import detect_phone_numbers
    phones_detected=detect_phone_numbers(emails_detected)
    from google.data.highlight import detect_code_param
    code_detected= detect_code_param(phones_detected)
    from google.data.highlight import detect_facebook_fbclid
    fb_clid_detcted=detect_facebook_fbclid(code_detected)
    from google.data.highlight import detect_acess_tokens
    tokens_detected=detect_acess_tokens(fb_clid_detcted)
    from google.data.highlight import detect_this_keyword
    and_signs_detected = detect_this_keyword(tokens_detected,"&")
    from app.utility import log
    log(and_signs_detected)

#@function get page html source
def get_html_src(url):
    try:
        from google.search.session import get_new_session
        session = get_new_session()
        response = session.get(url, cookies={})
        html=""
        if response.status_code==200:
            html=response.text
        session.close()
        return html 
    except Exception as why:
        from app.utility import log
        log("Failed to look inside: "+url)
        log("Reason: "+str(why))
    return ""

#@function detectes digital files
def detect_digital_flies_said(search_results, keyword):
    from google.data.cache import MATCHED_WORDS
    from google.data.highlight import record_keyword_freq
    from app.utility import print_red
    for sresult in search_results:
        if not MATCHED_WORDS.get(keyword):
            #freq = record_keyword_freq(search_result["link"],keyword)
            #msg = str(freq)+keyword+"detected " + search_result["link"]
            #print_red(msg)
            freq = record_keyword_freq(sresult["snippet"],keyword)
            msg = str(freq)+" digital flies detected in " + sresult["link"]+" snippet."
            print_red(msg)

        gmsg ="Looking inside " + sresult["link"]+" ..."
        from app.utility import print_green
        print_green(gmsg)
        src=get_html_src(sresult["link"])
        freq= record_keyword_freq(src,keyword)
        rmsg = str(freq) +" digital flies detected in " + sresult["link"]
        print_red(rmsg)
        
    #get the freq if it not None, else freq_val will be 0.
    freq_val = int(MATCHED_WORDS.get(keyword)) \
    if MATCHED_WORDS.get(keyword) else 0

    total_msg= str(freq_val) +" total flies detected."
    print_red(total_msg)

#function analyse wf json file
def analyse_from_local_file(loaded_dict,dork):
    for elem in loaded_dict:
        try:
            color_interested_data(elem["link"])
        except:
            pass

    if len(dork["kwds"])>0:
        for said in dork["kwds"]:#scan for keywords if the keyword list is not empty. 
            detect_digital_flies_said(loaded_dict,said)