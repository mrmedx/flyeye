#@function save to matched words
def save_matched_words(matched_words):
    if len(matched_words)>0:
        from google.data.cache import MATCHED_WORDS
        #from google.utility import log, text_to_green
        for i in range(0, len(matched_words)):
            if not MATCHED_WORDS.get(matched_words[i]):
                MATCHED_WORDS[matched_words[i]]=1
            else:
                MATCHED_WORDS[matched_words[i]]+=1
            #line = text_to_green("+ ")+matched_words[i]
            #log(line)

#@fucntion record text contains a given keyword
def record_keyword_freq(text,keyword):
    tkn_pattern = f'{keyword}'
    from re import findall , IGNORECASE
    matched_keywords = findall(tkn_pattern, text,IGNORECASE)
    save_matched_words(matched_keywords)
    return len(matched_keywords)

#@function
def detect_emails(text:str):
    from re import sub
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    record_keyword_freq(text,email_pattern)
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(email_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(email_pattern, lambda match: f"\033[33m{match.group(0)}\033[0m", text)
    return colored_text

#@funciton 
def detect_acess_tokens(text:str):
    tkn_pattern = r'(access_token=[^&]*)'
    #save th url to the cash after remove any params
    record_keyword_freq(text,tkn_pattern)
    from re import sub
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(tkn_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(tkn_pattern, lambda match: f"\033[91m{match.group(0)}\033[0m", text)
    return colored_text

#@funciton 
def detect_code_param(text:str):
    tkn_pattern = r'code=([^&]+)'
    from re import sub
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(tkn_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(tkn_pattern, lambda match: f"\033[32m{match.group(0)}\033[0m", text)
    return colored_text

#@funciton 
def detect_facebook_fbclid(text:str):
    tkn_pattern = r'fbclid=([^&]+)'
    record_keyword_freq(text,tkn_pattern)
    from re import sub
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(tkn_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(tkn_pattern, lambda match: f"\033[94m{match.group(0)}\033[0m", text)
    return colored_text

#@funciton 
def detect_this_keyword(text:str, keyword):
    tkn_pattern = f'{keyword}'
    from re import sub
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(tkn_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(tkn_pattern, lambda match: f"\033[96m{match.group(0)}\033[0m", text)
    return colored_text

#@function
def detect_phone_numbers(text:str):
    #phone_pattern = r'\b(?:\+?\d{1,3}[-.●]?)?\(?\d{1,4}\)?[-.●]?\d{1,4}[-.●]?\d{1,9}\b'
    #phone_pattern="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    phone_pattern=r'(?:(?:\+?\d{1,4}[ \-]?)?(?:\(\d{1,}\)[ \-]?)?[\d\- \.]{7,})'
    record_keyword_freq(text,phone_pattern)
    from re import sub
    from platform import system as checksys
    if checksys() == 'Windows':
        colored_text = sub(phone_pattern, lambda match: f"{match.group(0)}", text)
        return colored_text
    colored_text = sub(phone_pattern, lambda match: f"\033[93m{match.group(0)}\033[0m", text)
    return colored_text