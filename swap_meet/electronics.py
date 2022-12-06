from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown"):
        super().__init__(id)
        self.type = type
    
    def __str__(self):
        init_str = super().__str__()
        return init_str + f". This is a {self.type} device."
