[assembly_instructions]: https://github.com/Freenove/Freenove_Three-wheeled_Smart_Car_Kit_for_Raspberry_Pi/blob/master/Tutorial.pdf

# The Trike

## Prompt

Build an autonomous vehicle utilizing at least the following components:

- Camera
- All servo motors

## Vehicle

|                       |                                                                                   |
| --------------------- | --------------------------------------------------------------------------------- |
| Name                  | Freenove Three-Wheeled Smart Cat Kit                                              |
| Starter Code          | https://github.com/Freenove/Freenove_Three-wheeled_Smart_Car_Kit_for_Raspberry_Pi |
| Assembly Instructions | [assembly_instructions]                                                           |

## Setup Instructions

Follow along with the assembly / setup instructions [here][assembly_instructions]. Make note of the following additions / changes:

- After Step 0.3-2 on Tutorial Page 41 (PDF file page 45) run the following: `sudo apt-get install cmake`
- do not install the ultrasonic sensor, unless you wish to make a custom add on later!
- whenever you wish to power the raspberry pi utilizing the battery power (instead of a USB-C power supply), read [Powering Raspberry Pi via GPIO](#powering-raspberry-pi-via-gpio)

### Powering Raspberry Pi via GPIO

- reference the following article on powering the Raspberry Pi 4B: https://thepihut.com/blogs/raspberry-pi-tutorials/how-do-i-power-my-raspberry-pi
- **Seek help from a mentor before attempting the below steps**. Failure to properly connect can result in a fried raspberry pi
- Connect female jumper wires to 5V and GND on the Shield (blue). Use _any_ of the available 5V pins (red) and GND pins (black) on the diagram
  ![Shield 5V-GND pinout](<static/images/Shield 5V-GND pinout.png>)
- **CAREFULLY** connect the GND wire from the shield to the GND pin on the Raspberry Pi (green board)
- **CAREFULLY** connect the 5V wire from the shield to the 5V pin on the Raspberry Pi (green board)
  ![Rasperry Pi GPIO 5V-GND pinout](<static/images/Raspberry Pi GPIO 5V-GND pinout.jpg>)
- if you smell anything burning, or notce the pi or shield getting hot, turn off all power supplies immediately
- in the images below, the brown wire is connected to 5V on both the shield and the pi, whereas the black wire is connected to GND on both

![Shield 5V-GND assembly](<static/images/Shield 5V-GND assembly.jpg>)
![Raspberry Pi GPIO 5V-GND assembly](<static/images/Raspberry Pi GPIO 5V-GND assembly.jpg>)
