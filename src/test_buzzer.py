from rover import constants
import time
import signal
import gpiozero

if __name__ == '__main__':

    buzzer = gpiozero.Buzzer(constants.BUZZER_PIN)

    def signal_handler(sig, frame):
        buzzer.off()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    buzzer.on()
    time.sleep(1)
    buzzer.off()
