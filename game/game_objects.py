import pygame
import random
#need to somehow find out jhow a player will know where they afre on the board.. 
class Square:
    """
    Base class
    All squares on monopoly board will inherit from this.
    """
    def __init__(self, x, y, w, h, square_id, _property):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = square_id
        self.hover = False
        self.is_clicked = False
        self.property = _property #when creating the square objecs, in order to handle chaneg and communiuty chest. just pass _property as some sort of stryucture


    def check_if_hover(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + self.w and mouse_y > self.y and mouse_y < self.y + self.h:
            self.hover = True
            
        else:
            self.hover = False

class player:
    def __init__(self, piece):

        self.properties_owned = []
        self.get_out_of_jail_free = 0
        self.piece = piece
        self.wallet = 1500
        self.turn_is_over = True
        self.bankrupt = False
        self.in_jail = False
        self.doubles_rolled = 0 # use to check if they go to jail

    def check_if_bankrupt(self):
        pass

    def check_if_has_set(self):
        pass

    def roll_and_move(self):

        pass

    def mortage_property(self):
        pass

    def buy_property(self):
        pass

    def send_to_jail(self):
        pass


class Property:
    """
    Base class for monopoly properties
    """
    def __init__(self, name, value):

        self.name = name 
        self.value = value
        self.mortage_value = self.value/2
        self.is_owned = False
        self.property_owner = None

class UtilityProperty(Property):
    def __init__(self, type):
        super().__init__(name, value)

    pass

class StationProperty(Property):
    def __init__(self):
        super().__init__(name,value)
        pass
        
class MonopolyProperty(Property):
    def __init__(self, colour, rent, rent_1, rent_2, rent_3, rent_4):
        super().__init__(name, value)
        
        self.colour = colour
        self.number_of_houses = 0
        self.has_hotel = False
        self.rent = rent 
        self.rent_with_set = self.rent*2
        self.rent_1 = rent_1
        self.rent_2 = rent_2
        self.rent_3 = rent_3 
        self.rent_4 = rent_4 
        self.rent_with_hotel = rent_with_hotel




def roll_dice(player):
    number_1 = random.randint(1,6)
    number_2 = random.randint(1,6)
    if number_1 == number_2:
        player.doubles_rolled += 1
    return number_1 +number_2

    












