import pygame
import ui
import colors
import math

#Initailize pygame
pygame.init()


operator = "None"
first_value = 0 
second_value = 0
result = 0
is_error = False
func_value = 0.0
answer_displayed = False


#Setup the window

SCREEN_WIDTH,  SCREEN_HEIGHT = 256, 586

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Osy's Calculator")

#Managing UI elemets
element_manager = ui.UI_Manger()



#configure the buttons and edit boxes
def config_ui_elements():
    #Top edit box (0 index)
    element_manager.add_component(ui.Edit_Box(0, 0, SCREEN_WIDTH, 100, ""))
    #Top edit box (1 index)
    element_manager.add_component(ui.Edit_Box(0, 100, SCREEN_WIDTH, 100, "0"))

    #Adding the buttons

    #Row 1
    element_manager.add_component(ui.Button(0, 200, 64, 64, 'C', 'C'))
    element_manager.add_component(ui.Button(64, 200, 64, 64, 'sin', 'sin button'))
    element_manager.add_component(ui.Button(128, 200, 64, 64, 'cos', 'cos button'))
    element_manager.add_component(ui.Button(192, 200, 64, 64, 'tan', 'tan button'))
    #Row 2
    element_manager.add_component(ui.Button(0, 264, 64, 64, '7', 'number'))
    element_manager.add_component(ui.Button(64, 264, 64, 64, '8', 'number'))
    element_manager.add_component(ui.Button(128, 264, 64, 64, '9', 'number'))
    element_manager.add_component(ui.Button(192, 264, 64, 64, '+', 'operator'))

    #Row 3
    element_manager.add_component(ui.Button(0, 328, 64, 64, '4', 'number'))
    element_manager.add_component(ui.Button(64, 328, 64, 64, '5', 'number'))
    element_manager.add_component(ui.Button(128, 328, 64, 64, '6', 'number'))
    element_manager.add_component(ui.Button(192, 328, 64, 64, '-', 'operator'))

    #Row 4
    element_manager.add_component(ui.Button(0, 392, 64, 64, '1', 'number'))
    element_manager.add_component(ui.Button(64, 392, 64, 64, '2', 'number'))
    element_manager.add_component(ui.Button(128, 392, 64, 64, '3', 'number'))
    element_manager.add_component(ui.Button(192, 392, 64, 64, 'x', 'operator'))

    #Row 5
    element_manager.add_component(ui.Button(0, 456, 192, 64, '0', 'number'))
    element_manager.add_component(ui.Button(192, 456, 64, 64, '/', 'operator'))

    #Row 6
    element_manager.add_component(ui.Button(0, 520, 64, 64, '.', 'comma'))
    element_manager.add_component(ui.Button(64, 520, 64, 64, '^2', 'sqaure'))
    element_manager.add_component(ui.Button(128, 520, 64, 64, 'squrt', 'squrt'))
    element_manager.add_component(ui.Button(192, 520, 64, 64, '=', 'equals'))


    #Set colors
    for elemnet in element_manager.ui_components:

        #set the edit boxes to light grey
        if(elemnet.type == "EditBox"):
            elemnet.set_color(colors.LIGHT_GREY)
            elemnet.set_text_color(colors.WHITE)
        else:
        
            elemnet.set_color(colors.DARK_GREY)
            elemnet.set_text_color(colors.WHITE)
        

#draw all the UI elements on the screen
def draw_ui_elements():
    element_manager.draw(SCREEN)

#Handle processes for the UI elements
def handle_ui_elements():
    
    #Button interaction with the user
    for element in element_manager.ui_components:

        global operator, first_value, second_value, result, is_error, func_value, answer_displayed
       
        #Check each button that's a number
        if(element.type == 'number' or element.type == 'comma'):
           if(element.pressed):
               pygame.time.delay(250)
               if(not answer_displayed):
                    if(element_manager.ui_components[1].text != "0"):
                        element_manager.ui_components[1].text += element.text
                    else:
                        element_manager.ui_components[1].text = element.text

                    element_manager.ui_components[1].set_text_color(colors.WHITE)
                    #Clear the top edit box when there is an error
                    if(is_error):
                        element_manager.ui_components[0].text = ""
                        element_manager.ui_components[1].text = ""
                        is_error= False
               element.pressed = False       
        
        #Check each button that is an operator

        if(element.type == 'operator'):
           if(element.pressed):

               try:
                    pygame.time.delay(250)
                    operator = element.text
                    first_value = float(element_manager.ui_components[1].text) 
                    element_manager.ui_components[0].text += str(first_value) + " " + operator
                    #Clear both of the edit boxes
                    element_manager.ui_components[1].text = ""
                    element_manager.ui_components[0].set_text_color(colors.WHITE)
                    if(answer_displayed):answer_displayed = False
               except:
                    element_manager.ui_components[0].text = "Input error"
                    element_manager.ui_components[0].set_text_color(colors.RED)
                    is_error = True

               element.pressed = False
        #Check the equals button, then calculate the result of the inputs

        if(element.type == 'equals'):
            if(element.pressed):



                is_error = False
                pygame.time.delay(250)

                try:

                    if(not answer_displayed):
                        second_value = round(float(element_manager.ui_components[1].text))
                        
                        
                        if(operator == "+"): #Operation for addition
                            result = (first_value + second_value)
                            
                        elif(operator == "-"):#Operation for subtraction
                            result = (first_value - second_value)
                        
                        elif(operator == "x"):#Operation for multiplication
                            result = (first_value * second_value)
                            
                        elif(operator == "/"):#Operation for division
                            try:
                                result = (first_value / second_value)
                            except:
                                result = 0
                                element_manager.ui_components[0].text = "Can't divide by zero"
                                element_manager.ui_components[0].set_text_color(colors.RED)
                                is_error = True

                        elif(operator == 'squrt'):#Operation for squre root
                            func_value = float(element_manager.ui_components[1].text)

                            if(func_value >= 0):#Perform operation when the function value is not negative
                                result = math.sqrt(func_value)
                            else:
                                element_manager.ui_components[0].text = "Input error"
                                element_manager.ui_components[0].set_text_color(colors.RED)
                                is_error = True
                        elif(operator == 'sin'): #Operation for sine
                            func_value = float(element_manager.ui_components[1].text)
                            result = math.sin(math.radians(func_value))

                        elif(operator == 'cos'): #Operation for cosine
                            func_value = float(element_manager.ui_components[1].text)
                            result = math.cos(math.radians(func_value))


                        elif(operator == 'tan'): #Operation for tangent
                            func_value = float(element_manager.ui_components[1].text)
                            result = math.tan(math.radians(func_value))

                        else:#Operation for the square function
                            func_value = float(element_manager.ui_components[1].text)
                            result = (func_value * func_value)


                    
                                
                        if(not is_error): #Execute when there is not runtime errors
                            element_manager.ui_components[0].text = ""
                            element_manager.ui_components[1].text = str(result)
                            element_manager.ui_components[1].set_text_color(colors.YELLOW)
                            answer_displayed = True
                except:
                    element_manager.ui_components[0].text = "Operation Error"
                    element_manager.ui_components[0].set_text_color(colors.RED)
                    is_error = True

                element.pressed = False
               
        #Checking if the squre root button is pressed, then calculate the square root
        if(element.type == 'squrt'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = 'squrt'
                if(is_error): is_error = False
                element_manager.ui_components[0].text = "squrt("
                element_manager.ui_components[1].text = ""
                if(answer_displayed):answer_displayed = False
                element.pressed = False
               
        #Checking if the sin button is pressed, the calculate the sine of a value
        if(element.type == 'sin button'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = 'sin'
                if(is_error): 
                    is_error = False
                    element_manager.ui_components[0].set_text_color(colors.WHITE)

                element_manager.ui_components[0].text ="sin("
                element_manager.ui_components[1].text = ""
                if(answer_displayed):answer_displayed = False
                element.pressed = False

        #Checking if the cos button is pressed, the calculate the cosine of a value
        if(element.type == 'cos button'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = 'cos'
                if(is_error): 
                    is_error = False
                    element_manager.ui_components[0].set_text_color(colors.WHITE)
                element_manager.ui_components[0].text ="cos("
                element_manager.ui_components[1].text = ""
                if(answer_displayed):answer_displayed = False
                element.pressed = False

        #Checking if the tan button is pressed, the calculate the tangent of a value
        if(element.type == 'tan button'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = 'tan'
                if(is_error): 
                    is_error = False
                    element_manager.ui_components[0].set_text_color(colors.WHITE)
                element_manager.ui_components[0].text ="tan("
                element_manager.ui_components[1].text = ""
                if(answer_displayed):answer_displayed = False
                element.pressed = False

        #Clear everything on the calculator...
        if(element.type == 'C'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = "None"
                first_value = 0 
                second_value = 0
                element_manager.ui_components[0].text = ""
                element_manager.ui_components[0].set_text_color(colors.WHITE)
                element_manager.ui_components[1].text = ""
                element_manager.ui_components[1].set_text_color(colors.WHITE)
                result = 0
                is_error = False
                func_value = 0.0 
                element.pressed = False
                answer_displayed = False

        #Check the square button, then square a number
        if(element.type == 'sqaure'):
            if(element.pressed):
                pygame.time.delay(250)
                operator = 'sqaure'
                if(is_error): 
                    is_error = False
                    element_manager.ui_components[0].set_text_color(colors.WHITE)
                element_manager.ui_components[0].text ="square of("
                element_manager.ui_components[1].text = ""
                if(answer_displayed):answer_displayed = False

                element.pressed = False



def main():
    

    config_ui_elements()
    running = True
    clock = pygame.time.Clock()

    while(running):
        clock.tick(60)
        for event in pygame.event.get():
            if(event.type ==  pygame.QUIT):
                running = False
            #Handle the input for all the elements
            element_manager.handle_input(event) 

        handle_ui_elements()
        draw_ui_elements()
        pygame.display.update()
         

if(__name__ == "__main__"):
    main()

pygame.quit()