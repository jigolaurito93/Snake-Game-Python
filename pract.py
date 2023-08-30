class Animal:

    def __init__(self):
        print("I am an Animal")
    
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()
        
    
    def breathe(self):
        print("doing this underwater")





nemo = Fish()
nemo.breathe()
   

