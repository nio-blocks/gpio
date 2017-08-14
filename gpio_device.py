from threading import Lock

try:
    import RPi.GPIO as GPIO
except:
    # Let the block code load anyway so that som unit tests can run.
    pass


class GPIODevice():

    """Communicate with a device over GPIO."""

    def __init__(self, logger):
        self.logger = logger
        GPIO.setmode(GPIO.BCM)
        self._gpio_lock = Lock()

    def read(self, pin, pull_up_down=None):
        """Read bool value from a pin.

        Args:
            pin (int): the pin to read from

        Return:
            bool: value of digital pin reading

        """
        with self._gpio_lock:
            # TODO: don't call this every time
            if pull_up_down is not None:
                if pull_up_down:
                    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                else:
                    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            else:
                GPIO.setup(pin, GPIO.IN)
            value = GPIO.input(pin)
            self.logger.debug(
                "Read value from GPIO pin {}: {}".format(pin, value))
        return bool(value)

    def write(self, pin, value):
        """Write bool value to a pin.

        Args:
            pin (int): the pin to write to
            value (bool): boolean value to write to pin

        """
        with self._gpio_lock:
            # TODO: don't call this every time
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, value)
            self.logger.debug(
                "Wrote value to GPIO pin {}: {}".format(pin, value))

    def interrupt(self, callback, pin, pull_up_down=None, bouncetime=200):
        """Init interrupt callback function for pin.

        Args:
            callback (function): function to call on interrupt
            pin (int): the pin to monitor for interrupts

        """
        with self._gpio_lock:
            if pull_up_down is not None:
                if pull_up_down:
                    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                    # Use falling detection since we are pulled up
                    GPIO.add_event_detect(
                        pin, GPIO.FALLING, bouncetime=bouncetime)
                else:
                    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                    # Use rising detection since we are pulled down
                    GPIO.add_event_detect(
                        pin, GPIO.RISING, bouncetime=bouncetime)
            else:
                GPIO.setup(pin, GPIO.IN)
                GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=bouncetime)
            GPIO.add_event_callback(pin, callback)
            self.logger.debug(
                "Set interrupt callback of GPIO pin {}".format(pin))

    def close(self):
        try:
            GPIO.cleanup()
        except:
            self.logger.warning("Failed to close GPIO", exc_info=True)
