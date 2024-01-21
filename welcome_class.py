
class Welcome:
    
    def __init__(self, *args, **kwargs):
        
        # this really isn't doing anything right now.
        self.name = "";
        
    def getName(self):
        
        print("\n")
        self.name = str(input('\tWhat is your name? '))
        print("\n")
       
    def greet(self):
        
        print("\tHello {}, let's get started.".format(self.name))    
        print("\n")
