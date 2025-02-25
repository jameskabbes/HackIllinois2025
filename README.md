# The Rover

<img
    src="./static/images/assembled_kits/the_rover.jpg"
    alt="The Rover"
    width="1000"
/>

## Prompt

Build an autonomous vehicle utilizing at least the following components:

- Camera
- Line-following sensors

## Vehicle

|                       |                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------ |
| Name                  | Hiwonder TurboPi                                                                     |
| Product Link          | https://www.hiwonder.com/products/turbopi                                            |
| Assembly Instructions | https://drive.google.com/drive/folders/1gL7Cr4allhNadSSQw5e95lTrTqdYt46v?usp=sharing |

### Getting Started

Complete all the instructions from the assembly instructions tutorial.

#### Option 1. Manual Setup with James's source code

1. Enable I2C using `sudo raspi-config` -> `Interface Options` -> `I2C`
1. Clone the repository to the raspberry pi, checkout branch `the_rover`
1. Install the `libcap` development headers: `sudo apt-get install libcap-dev.`
   `sudo apt install -y python3-libcamera`
1. Make a virtual enviroment: `python -m venv venv --system-site-packages`
1. Activate the `source venv/bin/activate`
1. Install the required libraries: `pip install -r src/requirements.txt`
1. Run the `test_<item>.py` scripts to make sure all systems are working as expected: `sudo venv/bin/python src/test_battery.py`

- `sudo` is needed due to root privleges being required for the PixelStrip `test_led.py` (if this is not used, feel free to use the default system python environment)
- `venv/bin/python` is needed because `sudo` overwrites environment variables, no matter whether you are activiated in your venv or not, sudo makes it run the default python. Adding this relative path explicitly specifies the python env to use.

#### Option 2. Direct from Image with Hiwonder-provided source code
