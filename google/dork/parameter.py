from abc import ABC, abstractmethod
#@class Parameter, new parameters inherit from this class
class Parameter:
    @abstractmethod
    def translate():
        pass

    @abstractmethod
    def is_rules_passed():#the rules to add this parameter
        pass

    @abstractmethod
    def set_value(value):
        pass

    @abstractmethod
    def get_value():
        pass

    @abstractmethod
    def fire_before_add():
        pass

    @abstractmethod
    def fire_after_add():
        pass
