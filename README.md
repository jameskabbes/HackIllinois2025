# The Claw

<img
    src="./static/images/assembled_kits/the_claw.jpg"
    alt="All car kits"
    width="1000"
/>

## Prompt

Build an autonomous vehicle utilizing at least the following components:

- Camera
- The Claw (ability to pick up and release an object of your choice)
  - utilizing both servo motors

## Vehicle

|                       |                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------- |
| Name                  | Freenove Tank Robot for Raspberry Pi                                                        |
| GitHub Repo           | https://github.com/Freenove/Freenove_Tank_Robot_Kit_for_Raspberry_Pi                        |
| Assembly Instructions | https://github.com/Freenove/Freenove_Tank_Robot_Kit_for_Raspberry_Pi/blob/main/Tutorial.pdf |

### Assembly Instructions

Complete all the instructions from the assembly instructions tutorial.<br>
Note the following tips:

- Chapter 1 Step 2-3 (page 42 of tutorial, page 46 of PDF)

  - If `pi-hardware-pwm` is not installed properly following `sudo python setup.py`, execute the following
  - Make the `./Libs/pi-hardware-pwm/setup_pwm_overlay.sh` file executable:
    - Run `chmod +x setup_pwm_overlay.sh`
  - Run the executable
    - Run `sudo setup_pwm_overlay.sh`

- be sure to enable SPI interface on raspi-config
- **triple check your ultrasonic sensor wiring**, they are known to burn up!
