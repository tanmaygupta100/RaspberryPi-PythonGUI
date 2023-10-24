/*Steps for creating/running Java file using Pi terminal:
	Installing pi4j for GPIO pins: 'curl -sSL https://pi4j.com/install | sudo bash'
		Checking if installed properly: 'dpkg -l | grep pi4j'
	Create file by typing 'nano  /home/tanmay/Desktop/lab9_ist402.java'
		Write file: Ctrl+O
		Confirm file name: Enter
		Exit Nano: Ctrl+X
	Compile code: 'javac -cp .:/opt/pi4j/lib/'*' lab9_ist402.java'
	Run program: 'java lab9_ist402' */
	
/* Name: Tanmay Gupta
 * Lab 9: Java Traffic Light
 * Description:
 * 	Simulate a traffic light chaning using LEDs and an audio-indicator.
 * 	Done using states for each light. State-loop initiates with button-press.
 * VoiceThread: https://psu.voicethread.com/share/25140398/
*/

import com.pi4j.io.gpio.*;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;


public class lab9_ist402
{
    public static void main(String[] args) throws InterruptedException
    {
        final GpioController gpio = GpioFactory.getInstance();

        // Initializing components connected to GPIO pins.
        final GpioPinDigitalOutput redLED = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_13, "Red LED", PinState.LOW);
        final GpioPinDigitalOutput greenLED = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_26, "Green LED", PinState.LOW);
        final GpioPinDigitalOutput yellowLED = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_19, "Yellow LED", PinState.LOW);
        final GpioPinDigitalInput button = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02, PinPullResistance.PULL_DOWN);
        final GpioPinDigitalOutput buzzer = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_03, "Buzzer", PinState.LOW);

        // Initialize the state to start at the first step.
        int state = 1;

        // Main loop:
        while (true)
        {
            switch (state)
            {
                case 1:
					//Step 1: Red LED is ON by default:
                    redLED.high();
                    greenLED.low();
                    yellowLED.low();
                    buzzer.low();
					//Step 2: If button is pressed, turn ON Green LED:
                    if (button.isHigh())
                    {
                        state = 2;
                    }
                    break;
                case 2:
                    greenLED.high();
					//Step 3: While Green LED is ON, sound buzzer in quarter-sec increments:
                    for (int i = 0; i < 8; i++)
                    {
                        buzzer.high();
                        Thread.sleep(250);
                        buzzer.low();
                        Thread.sleep(250);
                    }
                    state = 3;
                    break;
                case 3:
                    //Step 4: After 2 seconds (from the for-loop), turn OFF Green and ON Yellow LEDs:
                    greenLED.low();
                    yellowLED.high();
                    //Step 5: After 1 second, turn OFF Yellow LED and return to Step 1.
                    Thread.sleep(1000);
                    yellowLED.low();
                    state = 1;
                    break;
                default:
                    state = 1;
                    break;
            }
            Thread.sleep(10);
        }
    }
}
