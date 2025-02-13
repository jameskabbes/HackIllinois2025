# The Boombox

## Prompt

Build an autonomous vehicle utilizing at least the following components:

- Camera
- Speaker

## Vehicle

|                       |                                                             |
| --------------------- | ----------------------------------------------------------- |
| Name                  | Sunfounder PiCar-X                                          |
| Product Link          | https://www.sunfounder.com/products/picar-x                 |
| Assembly Instructions | https://docs.sunfounder.com/projects/picar-x-v20/en/latest/ |

### Components

| Item              | Quantity | Description                                                               |
| ----------------- | -------- | ------------------------------------------------------------------------- |
| Motor             | 2        | polarity and speed control, rear-wheel drive                              |
| Camera            | 1        | 5mp camera                                                                |
| Servo motors      | 3        | move a gear to a certain angle (2 for camera orientation, 1 for steering) |
| Ultrasonic sensor | 1        | detect the distance of an item                                            |
| Line follower     | 3        | basic sensors to detect black tape on white floor (boolean)               |
| Battery           | 1        | 1.5 hour lifetime battery, rechargable via USB-C connnector on pi hat     |
| Speaker           | 1        |                                                                           |

### Source Code

Setup instructions for the source code

| Package   | Link                                               |
| --------- | -------------------------------------------------- |
| robot-hat | https://github.com/sunfounder/robot-hat/tree/v2.0  |
| vilib     | https://github.com/sunfounder/vilib/tree/picamera2 |
| picar-x   | https://github.com/sunfounder/picar-x/tree/v2.0    |

### Getting Started

Complete all the instructions from the following sections on the assembly documentation website:

- Assemble the PiCar-X
- Play with Python (Quick Guide on Python through at least 3. Text to Speech and Sound Effect)
