
# Author: Mujtaba
# Date: July 21, 2023


from abc import abstractmethod


class Module:
    modules = []

    @abstractmethod
    def render(self):
        pass


# Visit register_module.py to initialize modules as they are initialized there
from register_module import *

def program():
    for module in Module.modules:
        module.render()
