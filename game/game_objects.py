import pygame

class Square:
    """
    Base class
    All squares on monopoly board will inherit from this.
    """
    def __init__(self, x, y, w, h, square_id):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = square_id
        self.hover = False
        self.is_clicked = False

    def check_if_hover(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h:
            self.hover = True
            
        else:
            self.hover = False
            
            
    def is_clicked():
        # i think this shoud be doone in the event loop / find ut later..
        # will need to create a funcetio that loops through the squuares and checks if they are clicked.
        pass


class MonopolyProperty(Square):
    """
    square_id: unique id for that square
    rent_x: cost of rent with x houses
   
    """
    
    def __init__(self, x, y, w, h, square_id, property_name, property_value, rent, rent_1, rent_2, rent_3, rent_4, rent_with_hotel):
        super().__init__(x, y, w, h, square_id)
        
        self.property_name = property_name
        self.property_value = property_value
        self.mortage_value = self.property_value/2
        self.rent = rent 
        self.rent_with_set = self.rent*2
        self.rent_1 = rent_1
        self.rent_2 = rent_2
        self.rent_3 = rent_3 
        self.rent_4 = rent_4 
        self.rent_with_hotel = rent_with_hotel
      
       

    def test(self):
        #print(self.rent_data[self.property_name]["rent_with_set"])
        if self.hover:
            print(self.property_name)



