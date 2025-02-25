# The Rover

<img
    src="./static/images/assembled_kits/the_rover.jpg"
    alt="The Rover"
    width="1000"
/>

## Prompt

Build an autonomous vehicle utilizing at least the following components:

- Camera
- Both camera servos
- Ultrasonic
- Ultrasonic LEDs

## Vehicle

|                                       |                                                                                      |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| Name                                  | Hiwonder TurboPi                                                                     |
| Product Link                          | https://www.hiwonder.com/products/turbopi                                            |
| Assembly Instructions                 | https://drive.google.com/drive/folders/1gL7Cr4allhNadSSQw5e95lTrTqdYt46v?usp=sharing |
| Hiwonder Source Code and System Image | https://drive.google.com/drive/folders/1Y9FdmRe_h6JPQ0ggJe8bi1GDT4IsESSV?usp=sharing |

### Getting Started

Complete all the instructions from the assembly instructions tutorial.

#### Option 1. Manual Setup with James's source code **[recommended]**

_Note_: some of the functionality of the provided system image (servo zeroing, automatic startup, etc) is not available in the manual setup.

##### 1. Enable I2C Interface

- Open raspi-config: `sudo raspi-config`
- Enable I2C at `Interface Options` -> `I2C`.
- Reboot with: `sudo reboot`

##### 2. Repository setup

- Clone the repo
- Checkout branch `the_rover`

##### 3. Install raspberry pi libraries

- `sudo apt-get install libcap-dev`
- `sudo apt install -y python3-libcamera`

##### 4. Venv

- Create virtual environment with: `python -m venv venv --system-site-packages`
- Activate with: `source venv/bin/activate`
- Install the required libraries: `pip install -r src/requirements.txt`

##### 5. Run `test_<item>.py` scripts.

- Run each `src/test_<item>.py` script to make sure all systems are working as expected
- Template shown here: `sudo venv/bin/python src/test_battery.py`
  - `sudo` is needed due to root privleges being required for the PixelStrip `test_led.py` (if you don't want to use the shield's LED, feel free to use the default system python environment)
  - `venv/bin/python` is needed because `sudo` overwrites environment variables. No matter whether you are activiated in your venv or not, sudo makes it run the default python. Adding this relative path explicitly specifies the python env to use.

#### Option 2. Direct from Image with Hiwonder-provided source code

1. Load the provided Raspberry Pi system image onto the SD card, find the system image [here](https://drive.google.com/drive/folders/1Y9FdmRe_h6JPQ0ggJe8bi1GDT4IsESSV?usp=sharing)
2. Follow along with all the instructions in the assembly guide
