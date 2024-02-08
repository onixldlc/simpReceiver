
class MouseData(object): 
    velX=None
    velY=None
    m1=None
    m2=None
    
    def __init__(self, my_dict): 
        for key in my_dict: 
            setattr(self, key, my_dict[key])

    