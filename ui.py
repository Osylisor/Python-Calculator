
import pygame


pygame.font.init()

font = pygame.font.SysFont("cosmicsans",  29)


#Defination for the Component Ui class
class Component:

    def __init__(self):
        self.text = ""
        self.type = "None"
        self.color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.rect = None
        self.pressed = False

    def set_color(self,color):
        self.color = color

    def set_text_color(self, color):
        self.text_color = color

    def handle_input(self, event):
        pass

    def draw(self, surf):
        pass


class UI_Manger:

    def __init__(self):
        self.ui_components = []

    #Hanle input for all UI compoents
    def handle_input(self, event):
        for component in self.ui_components:
            component.handle_input(event)

    #Draw all the components
    def draw(self, surf):
        for component in self.ui_components:
            component.draw(surf)

    #Add a component
    def add_component(self,comp):
        self.ui_components.append(comp)

    #remove a component 
    def remove_component(self, comp):
        self.ui_components.remove(comp)

#Defination for the button class

class Button(Component):
    def __init__(self, x,  y, width, height, text, type):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.type = type
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def set_color(self, color):
        self.color = color


    def handle_input(self, event):
        mx, my = pygame.mouse.get_pos()

        mouse_rect = pygame.Rect(mx,  my, 2, 2)

        if(self.rect.colliderect(mouse_rect)):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.pressed = True
                self.set_color((15, 15, 15))
            elif(event.type == pygame.MOUSEBUTTONUP):
                self.pressed = False
                pygame.time.delay(250)
                self.set_color((29, 29, 29))
            else:
                self.set_color((29, 29, 29))

            


        

            

    def draw(self, surf):

        #create surface to draw on 
        s = pygame.Surface((self.rect.width, self.height))
        s.fill(self.color)

        #draw the text on the button
        text_surf = font.render(self.text, True, self.text_color)

        #draw the created surface to the screen
        surf.blit(s, (self.rect.x, self.rect.y))

        #text rendering on the button
        surf.blit(
            text_surf,
            (self.x + (self.width/2 - text_surf.get_width()/2), 
            self.y  + (self.height/2 - text_surf.get_height()/2))
        )
       

#Defination for the Edit box class

class Edit_Box(Component):

    def __init__(self, x,  y, width, height, text):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.type = "EditBox"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    


    def handle_input(self, event):
        return super().handle_input(event)
    
    def draw(self, surf):
        #create surface to draw on 
        s = pygame.Surface((self.rect.width, self.height))
        s.fill(self.color)
        #draw the text on the edit box
        text_surf = font.render(self.text, True, self.text_color)

        #draw the created surface to the screen
        surf.blit(s, (self.rect.x, self.rect.y))

        #text rendering on the edit box if the text's width is less than the width of the screnn
        if(text_surf.get_width() < 256):
            surf.blit(text_surf,(self.x , 
            self.y + (self.height /2 - text_surf.get_height()/2))
            )
        else:
            self.text = ""