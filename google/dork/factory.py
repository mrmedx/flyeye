from google.dork.params import *
#ParameterFactory=================================================
#build obkect based on the param
class ParameterFactory:
    def __init__(self, dork):
        self.dork=dork

    def build(self, param, param_value):
        if param==WHO:
            obj = Who(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==FLY:
            obj = Fly(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==FROM:
            obj = From(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==TO:
            obj =  To(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==AND:
            obj =  And(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==OR:
            obj =  Or(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==NOT:
            obj =  Not(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==SAVE_TO:
            obj =  SaveTo(self.dork)
            obj.set_value(param_value)
            return obj 
        elif param==LOAD:
            obj =  Load(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==AFTER:
            obj =  After(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==BEFORE:
            obj =  Before(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==EXACT:
            obj =  Exact(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==SAID:
            obj =  Said(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==ON:
            obj =  On(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==IN:
            obj =  In(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==ANY:
            obj =  Any(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==SITE:
            obj =  Site(self.dork)
            obj.set_value(param_value)
            return obj
        elif param==LEAKED:
            obj =  Leaked(self.dork)
            if param_value==EMAIL:
                obj.set_value(Email(self.dork))
            elif param_value==PHONE_NUMBER:
                obj.set_value(Phone(self.dork))
            elif param_value==ACCESS_TOKEN:
                obj.set_value(AccessToken(self.dork))
            else:
                obj.set_value(None)
            return obj 
        else:
            return None



