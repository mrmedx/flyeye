#@fucntion 
def log(txt):
    print(txt, flush=True)

#funciton saves the final result dict to  a json file
def save_as_json(results, file_path):
    try:
        with open(file_path, 'w') as json_file:
            import json
            json.dump(results, json_file, indent=2)
            log(file_path +" saved.")
    except Exception as why:
        log("Failed to save " + file_path + ".\nReason: "+str(why))


#@function loads the saved json file.
def load(file_path):
    try:
        with open(file_path, 'r') as json_file:
            import json
            loaded_data = json.load(json_file)
            return loaded_data
    except Exception as why:
        log(str(why))
    return None

#@function gets the value by index , returs None if the index is out of range.
def get_value_at(arr, i):
    try:
        val = arr[i]
        return val
    except:
        pass
    return None

#@fucntion get green text
def text_to_green(text):
    from platform import system as checksys
    if checksys() == 'Windows':
        return text
    return "\033[32m{}\033[0m".format(text)
 
#@fucntion gets red text
def text_to_red(text):
    from platform import system as checksys
    if checksys() == 'Windows':
        return text
    return "\033[31m{}\033[0m".format(text)

#@fucntion prints text with reds color
def print_red(msg):
    log(text_to_red(msg))
      
#function print green text
def print_green(msg):
    log(text_to_green(msg))

#@function
def sleep_for(duration):
    import time
    time.sleep(duration)

#@function return true for any form of url
def is_valid_url(url_text:str):
    dots=0
    notdots=0
    slashes=0
    try:
        for i in range(0,len(url_text)):
            if url_text[i]=='.' and url_text[i+1]=='.':
                return False
            if url_text[i]=='.':
                dots+=1
            if url_text[i]!='.' and url_text[i]!='/':
                notdots+=1
            if url_text[i]=='/':
               slashes+=1
        return dots <= (notdots/2) and slashes < (notdots/2)
    except:
        pass
    return False

#@function validates the date string.
def is_valid_date(date_str):
    from re import compile, match
    try:
        pattern = compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(match(pattern, date_str))
    except:
        pass
    return False

#@function checks arg if it a valid country code
def is_valid_country_code(param:str):
    return len(param)==2 and not param[0].isdigit() \
    and not param[1].isdigit()

#@funciton prints flyeye version
def print_version():
    from app.constants import VERSION
    log(VERSION)

#@function print flyeye description
def print_flyeye_desc():
    from app.constants import VERSION, DESCRIPTION
    log(VERSION+" - "+DESCRIPTION)

#@funciton prints the help menu
def print_help_menu():
    print_flyeye_desc()
    from app.constants import HELP_MENU
    for kwd,info in HELP_MENU.items():
        print_green(kwd+":")
        log(f"  {info['description']}")
        log(f"  Example: {info['example']}")

#def get help about target command
def get_help_about(target_kwd):
    print_flyeye_desc()
    from app.constants import HELP_MENU
    is_kwd_found=False
    for kwd,info in HELP_MENU.items():
        if kwd==target_kwd:
            print_green(kwd+":")
            log(f"  {info['description']}")
            log(f"  Example: {info['example']}")
            is_kwd_found=True
            break
    if not is_kwd_found:
        log(target_kwd+" is not supported.")
    
    
#fucntion filter first args to find help or version commands
def is_work_commands(argv):
    from app.constants import VERSION_COMMANDS , HELP_COMMANDS
    if len(argv)<=4 and len(argv)>=2:
        if argv[1] in VERSION_COMMANDS:#version cmd
            print_version()
            return False
        elif argv[1] in HELP_COMMANDS and not get_value_at(argv, 2):# no target keyword for help
            print_help_menu()
            return False
        elif argv[1] in HELP_COMMANDS and get_value_at(argv, 2): #help about target command
            get_help_about(argv[2])
            return False
    from app.constants import LOAD , SAVE_TO
    if len(argv) <=4 and LOAD not in argv and SAVE_TO not in argv:#invalid params
        print_help_menu()
        return False
    return True # a work command


#@function loads and analyse a local flyeye json file.
def flyeye_laod(argv):
    wf_results = load(argv[2])
    if not wf_results:
        print_red("invalid flyeye file.")
        return
    if len(wf_results)==0:
        print_red("empty file.")
        return
    #translate the argv to dork
    from app.translate import ArgTranslator
    arg_translator = ArgTranslator()
    dork=arg_translator.translate(argv)
    if not dork:
        return
    if len(dork)>0:
        print(dork)
        from google.data.analysis import analyse_from_local_file
        analyse_from_local_file(wf_results,dork)


#@function flyeye app
def app(argv):
    if not is_work_commands(argv):
        return
    from app.constants import LOAD
    if argv[1]==LOAD and get_value_at(argv, 2):#load from local wf file
        flyeye_laod(argv)
    elif argv[1]==LOAD and not get_value_at(argv, 2):
        log("Enter the json file path.")
    else:
        #translate the argv to dork
        from app.translate import ArgTranslator
        arg_translator = ArgTranslator()
        dork=arg_translator.translate(argv[1:])
        if not dork:
            return
        if len(dork)>0:
            print(dork)
            from google.search.query import get_query_results
            query_results = get_query_results([dork])
            save_as_json(query_results,dork["sp"])#save the @query_results into @dork["sp"] save path.

#function to start flyeye app           
def launch_flyeye(argv):
    try:
        app(argv)
    except Exception as why:
        log("flyeye unexpected termination. : " + str(why))