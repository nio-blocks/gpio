from enum import Enum
from threading import Lock
from nio.block.base import Block
from nio.util.discovery import discoverable
from nio.properties import IntProperty, VersionProperty, SelectProperty, \
    ObjectProperty, PropertyHolder


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
            self.logger.debug("Value of GPIO pin {}: {}".format(pin, value))
        return bool(value)

    def close(self):
        try:
            GPIO.cleanup()
        except:
            self.logger.warning("Failed to close GPIO", exc_info=True)


class PullUpDownOptions(Enum):
    PUD_UP = True
    PUD_DOWN = False
    PUD_OFF = None


class PullUpDown(PropertyHolder):
    default = SelectProperty(PullUpDownOptions,
                             title="Default Pull Resistor",
                             default=PullUpDownOptions.PUD_OFF)
    # TODO: add ability to select base on pin number


@discoverable
class GPIORead(Block):

    pin = IntProperty(default=0)
    version = VersionProperty('0.1.0')
    pull_up_down = ObjectProperty(PullUpDown,
                                  title="Pull Resistor Up/Down",
                                  default=PullUpDown())

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
            return self._gpio.read(pin, self.pull_up_down().default().value)
        except:
            self.logger.warning("Failed to read gpio pin: {}".format(pin),
                                exc_info=True)
