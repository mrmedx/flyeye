"""
============================
Description: each flyeye keyword like who ,said passed by the user is encapsulated into a class derived from Parameter abstract class
each derived class stores the keyword like said and the translate of said to a dork like 'intext:' and the value passes by the user for example:
who said "wellcome" , the class Who derived from Parameter saves the keyword 'who' and no google dork value and no value passed to 'who', but it added into a list member in the Dork class
so the next flyeye paramter said can access the previous parameter in the Dork class and apply its rules if it compatible with the previous parameter or not by overridding the 
virtual method is_rules_passed from the parent Parameter class.

if you want to add a new keyword to flyeye just add a new child class derived from the Parameter class with the new parameter name
and implement the needed functions, if your new parameter is not compatible with other flyeye parameters you will see an error message with the exact prameter 
failed to integrate with your new parameter because of its rules implemented in is_rules_passed function, so just add your parameter to its rules in order for it to recognize your new parameter and accept it
for eaxample in parameter x:
is_rule_passed=last_param.text in [YOUR_NEW_PARAMETER, WHO, AND, NOT,OR]

by adding your YOUR_NEW_PARAMETER to the x parameters list defined in its is_rules_passed function 
the x parameter will not generate an error when it comes after your new parameter in the user passed commands.

The Dork class fire 2 events for each parameter object passed to add_param function , if the passed parameter object is_rules_passed function returns true :

1-fire_before_add()
2-fire_after_add()

this 2 fucnitons implemented by parameter objects if the parameter needs to manipumate the dork value added by the previous parameter
becasue each parameter object owns dork object for example:

class Said(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork

the Said parameter can access the dork.text before its translatred value , and value passed by the user added to the dork text 
or after the value added to the dork text using this 2 overrided funcitons from the Parameter class. 

see the Dork class  #@fucntion add a parameter if its rules passed  
for more info.

Author: Mohamed Naamane
Email:mrnmnwork@gmail.com
README:https://github.com/mrmedx/web_forensics

============================

"""

from google.dork.parameter import Parameter
from app.constants import *
#@class Dork ============================================
class Dork:
    def __init__(self):
        self.prrams=[]
        self.text=""
        self.targeted_keywords=[] #to save keywords after said param
        self.save_path="wf_results.json"
        self.valid=True
    
    #@function
    def set_save_path(self, save_path):
        self.save_path=save_path
   
    def get_save_path(self):
        return self.save_path
    
    #@fucntion
    def get_targeted_keywords(self):
        return self.targeted_keywords
    
    #@fucntion
    def add_target_keyword(self, kwd):
        self.targeted_keywords.append(kwd)

    #@fucntion get the value of a param by its name
    def get_value_of(self,param_name):
        for elem in self.prrams:
            if  elem.text == param_name:
               return elem.value
        return ""
    
    #@fucntion
    def length(self):
        return len(self.prrams)-1
    
    #@fucntion
    def get_param_by_index(self,index):
        if (index > self.length()) or index<0:
            return None
        return self.prrams[index]
    
    #@fucntion
    def append_text(self, text):
        self.text+=text
    
    #@fucntion
    def get_text(self):
        return self.text.rstrip()
    
    #@fucntion add a parameter if its rules passed 
    def add_param(self,param:Parameter):
        if not param:
            return
        if param.is_rules_passed():
            param.fire_before_add()
            self.prrams.append(param)
            info =param.translate() + param.get_value()
            self.append_text(info)
            param.fire_after_add()
        else:
            self.valid=False

    #@fucntion check if all params ruels passed.       
    def is_valid(self):
        return self.valid

#said ============================================
class Said(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="said"
        self.translate_text="intext:"
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param = self.dork.get_param_by_index(params_len)
        #it should not be the first arg and the prev prams shoud be who, and , or , not
        is_rule_passed=params_len>=0 
        if is_rule_passed:
            is_rule_passed=last_param.text in [WHO, AND, NOT,OR]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of said after "+last_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        params_len = self.dork.length()
        prev_param = self.dork.get_param_by_index(params_len)
        try:
            if prev_param.text ==NOT:
                self.dork.text=self.dork.text.rstrip()#remove any spces at the end of dork val to ensure correct handling of '-'.
        except:
            pass

    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value
        self.dork.add_target_keyword(self.value)

#who ============================================
class Who(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="who"
        self.translate_text=""
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        #it should bne the first arg or after who or load
        is_rule_passed=params_len<0
        if params_len>=0:
            prev_param=self.dork.get_param_by_index(params_len)
            is_rule_passed=prev_param.text in [LOAD,SAVE_TO]
        if not is_rule_passed:
            from app.utility import print_red
            prev_param = self.dork.get_param_by_index(params_len)
            print_red("Invalid use of who after "+prev_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    def fire_before_add(self):
        pass

    def fire_after_add(self):
        pass

#@class email ============================================
class Email(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text=EMAIL
        self.translate_text=""
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud be who , and, or
        is_rule_passed=params_len>0 and last_param.text == LEAKED
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        #get the prev-1 param index
        target_index = self.dork.length()
        target_param=self.dork.get_param_by_index(target_index)
        #if 'OR', 'AND' not found, add 'OR' before self.value
        email_dork='( inurl:"*email=" OR inurl:"*contact=" OR inurl:"*address=" OR inurl:"*contact_point=" )'
        try:
            if target_param.text != OR and target_param.text != AND and target_param.text !=WHO:
                self.value="OR "+email_dork
            else:
                self.value=email_dork
        except:
            pass 

    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value
    

#@class AccessToken ============================================
class AccessToken(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text=ACCESS_TOKEN
        self.translate_text=""
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud be who , and, or
        is_rule_passed=params_len>0 and last_param.text == LEAKED
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        #get the prev-1 param index
        target_index = self.dork.length()
        target_param=self.dork.get_param_by_index(target_index)
        #if 'OR', 'AND' not found, add 'OR' before self.value
        token_dork='inurl:"*access_token=" OR inurl:"*token="'
        try:
            if target_param.text != OR and target_param.text != AND and target_param.text !=WHO:
                self.value="OR "+token_dork
            else:
                self.value=token_dork
        except:
            pass 

    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value
    

#@class Phone ============================================
class Phone(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="phone"
        self.translate_text=""
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud be who , and, or
        is_rule_passed=params_len>0 and last_param.text == LEAKED
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        #get the prev-1 param index
        target_index = self.dork.length()
        target_param=self.dork.get_param_by_index(target_index)
        #if 'OR', 'AND' not found, add 'OR' before self.value
        phone_dork='( inurl:"*sms=" OR inurl:"*phone=" OR inurl:"*mobile=" OR inurl:"*medium=sms" OR inurl:"*contact_point=" OR inurl:"*contact=" )'
        try:
            if target_param.text != OR and target_param.text != AND and target_param.text !=WHO:
                self.value="OR "+phone_dork
            else:
                self.value=phone_dork
        except:
            pass 

    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value

#@class leaked ============================================
class Leaked(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text=LEAKED
        self.translate_text=""
        self.value=None
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud be who , and, or
        is_rule_passed=params_len>=0 and last_param.text in [WHO,AND,OR]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        if self.value:
            return self.value.get_value()
        return ""
    
    #@override
    def fire_before_add(self):
        if self.value:
            self.value.fire_before_add()
    
    #@override
    def fire_after_add(self):
        #dont add a space it the prev param is who
        params_len = self.dork.length()-1
        prev_param=self.dork.get_param_by_index(params_len)
        try:
            if prev_param.text !=WHO:
                self.dork.append_text(" ") #add a space before the next value
        except:
            pass
    
#and ============================================
class And(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="and"
        self.translate_text="AND"
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        if params_len<0:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" as the first command.")
            return False
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud not in the keyword list
        is_rule_passed=params_len>0 and last_param.text not in [IN,WHO,OR,AND,FLY,LOAD,SAVE_TO,ANY]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value

#or ============================================
class Or(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="or"#wf keyword
        self.translate_text="OR" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        if params_len<0:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" as the first command.")
            return False
        last_param=self.dork.get_param_by_index(params_len)
        #the prev prams shoud be not in the keywords list
        is_rule_passed=params_len>0 and last_param.text not in [IN,WHO,OR,AND,FLY,LOAD,SAVE_TO,ANY]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value
                

#not ============================================
class Not(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="not"#wf keyword
        self.translate_text="-" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        #not keyword is not at the start and the prev shoud be in this list
        is_rule_passed=False
        if last_param:
            is_rule_passed= params_len>=0 and last_param.text in [AND, OR, WHO]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        pass




#from ============================================
class From(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="from"#wf keyword
        self.translate_text="inurl:" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound be fly , and at least 2 keywords are written before.
        if last_param:
            is_rule_passed= params_len>0 and last_param.text ==FLY
        from app.utility import print_red
        if not is_rule_passed:      
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        #validate the url dork value
        if self.value=="":
            #passed to any
            return is_rule_passed
        from app.utility import is_valid_url
        url_valid = is_valid_url(self.value)
        if not url_valid:
            print_red(INVALID_URL+self.value)
        return is_rule_passed and url_valid
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value
        #if the prev param is fly and the current value is fb or instagram, add dorks for fb&insta
        #(inurl:"*fbclid=")
        params_len = self.dork.length()-1
        prev_param=self.dork.get_param_by_index(params_len)
        try:
            if prev_param.text == FLY:
                if FACEBOOK in self.value:
                    #add fb dork
                    self.dork.text+='OR inurl:"*fbclid=" '
                elif INSTAGRAM in self.value:
                    self.dork.text+='OR inurl:"*e=" OR site:l.instagram.* '
        except:
            pass

#to ============================================
class To(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="to"#wf keyword
        self.translate_text="site:" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound be fly ,or any other text not in the keywords list
        if last_param:
            is_rule_passed= params_len>0 and last_param.text in [FLY,FROM,SITE]
        from app.utility import print_red
        if not is_rule_passed:
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        #validate the url dork value
        if self.value=="":
            #passed to any
            return is_rule_passed
        from app.utility import is_valid_url
        url_valid = is_valid_url(self.value)
        if not url_valid:
            print_red(INVALID_URL+self.value)
        return is_rule_passed and url_valid
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        params_len = self.dork.length()
        prev_param=self.dork.get_param_by_index(params_len)
        try:
            if FACEBOOK in self.value:
                #add fb dork
                self.value+=' OR inurl:"*fbclid=" OR site:*.facebook.* '
            elif INSTAGRAM in self.value:
                self.value+=' OR inurl:"*e=" OR site:l.instagram.* '
            if prev_param.text==FROM or prev_param.text==SITE:
                self.dork.append_text("AND ") #add 'AND' to the dork ex: inurl:fb.com AND site:insta.com
        except:
            pass
       
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value



#exact ============================================
class Exact(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="exact"#wf keyword
        self.translate_text="\"" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound be said or  from, or any other text not in the keywords list
        if last_param:
            is_rule_passed= params_len>0 and last_param.text in [SAID, FROM]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        self.dork.text=self.dork.text.rstrip()#ensure here is no spaces at the end
    
    #@override
    def fire_after_add(self):
        #close the "\""   
        self.dork.append_text("\" ")




#before ============================================
class Before(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="before"#wf keyword
        self.translate_text="before:" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in the keywdors list except and , or
        if last_param:
            is_rule_passed= params_len>=0 and last_param.text not in [LOAD, SAVE_TO, AFTER, BEFORE]
        from app.utility import print_red
        if not is_rule_passed:        
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        #validate the date (self.value)
        from app.utility import is_valid_date
        date_is_valid = is_valid_date(self.value)
        if not date_is_valid:
            print_red(INVALID_DATE+self.value+VALID_DATE_EXAMPLE)
        return is_rule_passed and date_is_valid
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value


#after ============================================
class After(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="after"#wf keyword
        self.translate_text="after:" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in the keywdors list except and , or
        if last_param:
            is_rule_passed= params_len>=0 and last_param.text not in [LOAD, SAVE_TO, AFTER, BEFORE]
        from app.utility import print_red
        if not is_rule_passed:
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        #validate the date (self.value)
        from app.utility import is_valid_date
        date_is_valid = is_valid_date(self.value)
        if not date_is_valid:
            print_red(INVALID_DATE+self.value+VALID_DATE_EXAMPLE)
        return is_rule_passed and date_is_valid
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value



#fly ============================================
class Fly(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="fly"#wf keyword
        self.translate_text="" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound be who, and fly not the first arg
        if last_param:
            is_rule_passed= params_len>=0 and last_param.text ==WHO
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        pass

#saveto ============================================
class SaveTo(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="saveto"#wf keyword
        self.translate_text="" #dork value
        self.value=""
        self.file_name=""

    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=params_len<0
        #the prev value shound be in the keywdors list or 'saveto' is the first keyword
        if last_param and not is_rule_passed:
            is_rule_passed=last_param.text in KEYWORDS 
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        self.file_name=self.value
        self.value=""
    
    #@override
    def fire_after_add(self):
        params_len = self.dork.length()-1
        if params_len>=0:
            self.dork.append_text(" ") #add a space before the next value
        if self.file_name!="":
            self.dork.set_save_path(self.file_name)
#load ============================================
class Load(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="load"#wf keyword
        self.translate_text="" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=params_len<0
        #the prev value shound not be in the keywdors list or it is the first keyword
        if last_param and not is_rule_passed:
            is_rule_passed=last_param.text not in KEYWORDS
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value


#in ============================================
class In(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="in" #wf keyword
        self.translate_text="" #dork value
        self.value=""
        self.country=""

    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in the keywdors list and "in" is not the first arg
        if last_param:
            is_rule_passed= params_len>0
        from app.utility import print_red
        if not is_rule_passed:
            print_red("Invalid use of "+self.text +" after " + last_param.text)
            return False
        #validate the country
        from app.utility import is_valid_country_code
        cuntry_valid = is_valid_country_code(self.value)
        if not cuntry_valid:
            print_red(INVALD_COUNTRY_CODE+ self.value+COUNTRY_CODE_EXAMPLE)
        return is_rule_passed and cuntry_valid
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        self.country=self.value.upper()
        self.value=""
    
    #@override
    def fire_after_add(self):
        self.value="country"+self.country
        pass
        #self.dork.append_text(" ") #add a space before the next value


#on ============================================
class On(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="on"#wf keyword
        self.translate_text="site:" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in and, or, not, who, email , phone , access_token, said
        if last_param:
            is_rule_passed= params_len>=0 and last_param.text in [EXACT,AND, OR, NOT, WHO, EMAIL, PHONE_NUMBER, ACCESS_TOKEN, SAID, LEAKED,IN] 
        from app.utility import print_red
        if not is_rule_passed:  
            print_red("Invalid use of "+self.text +" after " + last_param.text)
            return False
        #validate the url dork value
        if self.value!="":
            from app.utility import is_valid_url
            url_valid = is_valid_url(self.value)
            if not url_valid:
                print_red(INVALID_URL+self.value)
                return is_rule_passed and url_valid
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        params_len = self.dork.length()
        prev_param=self.dork.get_param_by_index(params_len)
        curr_dork = self.dork.text
        #if there is no space at the end + the prev param is not 'not' add one
        if curr_dork[len(curr_dork)-1]!=' ' and prev_param.text !=NOT:
           self.dork.text+=' '
        #if the prev param is 'leaked' add 'AND'
        params_len = self.dork.length()
        prev_param=self.dork.get_param_by_index(params_len)
        try:
            if prev_param.text==LEAKED:
                #if fb or insta add its leakdorks.
                if FACEBOOK in self.value and prev_param.value.text==ACCESS_TOKEN:
                    self.translate_text=""
                    self.value=""
                    self.dork.text='inurl:"*access_token=" site:graph.facebook.com '
                elif INSTAGRAM in self.value and prev_param.value.text==ACCESS_TOKEN:
                    self.translate_text=""
                    self.value=""
                    self.dork.text='inurl:"*access_token=" AND inurl:"*graph.instagram.com" site:*.instagram.com '
                    #inurl:"*access_token=" site:graph.instagram.com
                else:
                    self.dork.text+="OR "
        except:
            pass
    
    #@override
    def fire_after_add(self):
        self.dork.append_text(" ") #add a space before the next value

#any ============================================
class Any(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="any"#wf keyword
        self.translate_text="" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text

    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in the keywdors list except and , or
        if last_param:
            is_rule_passed= params_len>0 and last_param.text in [FROM,TO,ON]
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        self.dork.text=self.dork.text.rstrip()#ensure there is no spaces at the end of the dork.
       
    #@override
    def fire_after_add(self):
        pass

#site ============================================
class Site(Parameter):
    def __init__(self,dork:Dork):
        self.dork=dork
        self.text="site"#wf keyword
        self.translate_text="*.*" #dork value
        self.value=""
        
    #@override
    def translate(self):
        return self.translate_text
    
    #@override
    def is_rules_passed(self):
        params_len = self.dork.length()
        last_param=self.dork.get_param_by_index(params_len)
        is_rule_passed=False
        #the prev value shound not be in the keywdors list except and , or
        if last_param:
            is_rule_passed= params_len>1 and last_param.text == ANY
        if not is_rule_passed:
            from app.utility import print_red
            print_red("Invalid use of "+self.text +" with " + last_param.text)
            return False
        return is_rule_passed
    
    #@override
    def set_value(self,value):
        self.value=value

    #@override
    def get_value(self):
        return self.value
    
    #@override
    def fire_before_add(self):
        params_len = self.dork.length()-1
        #get the param at prev-1
        target_param=self.dork.get_param_by_index(params_len)
        try:
            if target_param.text ==FROM:
                self.translate_text='"*"'
        except:
            pass

    #@override
    def fire_after_add(self):
        self.dork.text+=" " #add a space to teh dork site 