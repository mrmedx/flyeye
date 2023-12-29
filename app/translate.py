from google.dork.factory import ParameterFactory 
from google.dork.params import Dork

class ArgTranslator:
    def __init__(self):
        pass

    #@function converts the dork obj to a dict
    def dork_to_dict(self,dork:Dork):
        response={}
        dork_text = dork.get_text()
        response["dork"]=dork_text #add the dork text
        from app.constants import IN
        country = dork.get_value_of(IN)
        if country:
            response["cr"]=country #add the dork saved country
        else:
            response["cr"]=""
        target_keywords_list = dork.get_targeted_keywords()
        response["kwds"]=target_keywords_list #add the dork saved keyword list after 'said' command
        save_path = dork.get_save_path()
        response["sp"]=save_path #add the save file path
        return response

    #@function converts flyeye argv to a google dork
    def translate(self,argv):
        if len(argv)<=2:
            return {}
        dork = Dork()
        parameterFactory=ParameterFactory(dork)
        from app.constants import KEYWORDS, LEAKED, NOT, AND,OR
        from app.utility import get_value_at
        parsed ={}
        for i in range(0, len(argv)):
            #detect unsupported commands
            if argv[i] not in KEYWORDS and get_value_at(argv,i+1):
                if get_value_at(argv,i+1) not in KEYWORDS:
                    from app.utility import print_red
                    print_red("Unsupported command: " + argv[i]+" "+ get_value_at(argv,i+1))
                    return {}
                
            #invalid input after logical keywords
            if argv[i] ==AND or argv[i] ==OR or  argv[i] ==NOT and get_value_at(argv,i+1):
                if get_value_at(argv,i+1) not in KEYWORDS:
                    from app.utility import print_red
                    print_red("Unsupported command: "+argv[i]+" "+get_value_at(argv,i+1))
                    return {}
                
            if get_value_at(argv,i+1):
                if parsed.get(argv[i]+get_value_at(argv,i+1)):
                    continue

            if argv[i]==LEAKED:
                param = parameterFactory.build(argv[i], get_value_at(argv,i+1))
                dork.add_param(param)
                parsed[argv[i]+get_value_at(argv,i+1)]=True
            elif argv[i] in KEYWORDS and get_value_at(argv,i+1) not in KEYWORDS:
                param = parameterFactory.build(argv[i], get_value_at(argv,i+1))
                dork.add_param(param)
                parsed[argv[i]+get_value_at(argv,i+1)]=True
            elif argv[i] in KEYWORDS and get_value_at(argv,i+1):
                if get_value_at(argv,i+1) in KEYWORDS:
                    param = parameterFactory.build(argv[i], "")
                    dork.add_param(param)

        if dork.is_valid():
            return self.dork_to_dict(dork)
        return {}
        

