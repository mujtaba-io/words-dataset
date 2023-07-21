
# Author: Mujtaba
# Date: July 21, 2023

# Module that scrapes data from the web and adds to dataset


from architecture import Module


class WebScrap(Module):
    def __init__(self):
        Module.modules.append(self)
    
    def render(self):
        print("WebScrap")
