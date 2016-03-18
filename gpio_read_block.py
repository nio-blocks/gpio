from nio.block.base import Block
from nio.util.discovery import discoverable
from nio.properties import BoolProperty, VersionProperty


class GPIODevice():

    """Communicate with a device over GPIO."""

    def __init__(self, logger):
        import RPi.GPIO as GPIO
        self.logger = logger
        GPIO.setmode(GPIO.BCM)
        self._gpio_lock = Lock()

    def read(self, pin):
        """Read bool value from a pin.

        Args:
            pin (int): the pin to read from

        Return:
            bool: value of digital pin reading

        """
        with self._gpio_lock:
            GPIO.setup(pin, GPIO.IN) # TODO: don't call this every time
            value = GPIO.input(pin)
            self.logger.debug("Value of GPIO pin {}: {}".format(pint, value))
        return value

    def close(self):
        try:
            GPIO.cleanup()
        except:
            self.logger.warning("Failed to close GPIO", exc_info=True)


@discoverable
class GPIORead(Block):

    pin = BoolProperty(default=0)
    version = VersionProperty('0.1.0')

    def __init__(self):
        super().__init__()
        self._gpio = None

    def configure(self, context):
        super().configure(context)
        self._gpio = GPIODevice(self.logger)

    def stop(self):
        super().stop()
        self._gpio.close()

    def process_signals(self, signals):
        for signal in signals:
            signal.value = self._read_gpio_pin(self.pin(signal))
        self.notify_signals(signals)

    def _read_gpio_pin(self, pin):
        try:
            return self._gpio.read(pin)
        except:
            self.logger.warning("Failed to read gpio pin: {}".format(pin),
                                exc_info=True)
