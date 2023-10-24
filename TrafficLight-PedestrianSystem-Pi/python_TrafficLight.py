#Name: Tanmay Gupta
#Lab 8: Python Traffic Light
#Description:
    # Simulate a traffic light changing using LEDs and an audio indicator.
    # Done using states for each light. State loop initiates with button press.

from gpiozero import LED, Button, Buzzer
from time import sleep

#Initializing which components are connected to which pins:
LEDRed = LED(13)
    # The red LED is connected to pin 13 through a resistor,
        # then connected to GROUND.
LEDGreen = LED(26)
LEDYellow = LED(19)
button = Button(2)
    # Button didn't need resistor.
    # Orientation of voltage/ground cables didn't make a difference.
buzzer = Buzzer(3)
    # An active buzzer doesn't need a resistor.

#Starting from state 1:
state = 1
    # States are the different steps of code to move onto when called.

#Main loop:
while True:

    #Initializing all components as OFF:
    LEDRed.off()
    LEDGreen.off()
    LEDYellow.off()
    buzzer.off()

    if state == 1:
        #Step 1: Red LED is ON by default:
        LEDRed.on()

        #Step 2: If button is pressed, turn ON Green LED:
        button.wait_for_press()
        LEDRed.off()
        LEDGreen.on()
        state = 2 # move onto state 2.
            
    if state == 2:
        #Step 3: While Green LED is ON, sound buzzer in quarter-sec increments:
        for i in range(8): # 8 for-loops of 0.25 is 2 seconds total.
            buzzer.on()
            sleep(0.25)
            buzzer.off()
            sleep(0.25)
        state = 3

    if state == 3:
        #Step 4: After 2 seconds (for loop), turn OFF Green and ON Yellow LEDs:
        LEDGreen.off()
        LEDYellow.on()
        
        #Step 5: After 1 second, turn OFF Yellow LED and return to Step 1:
        sleep(1)
        LEDYellow.off()
        state = 1
