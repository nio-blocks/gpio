from enum import Enum

from nio.block.base import Block
from nio.properties import IntProperty, VersionProperty, SelectProperty, \
    ObjectProperty, PropertyHolder

from .gpio_device import GPIODevice

try:
    import RPi.GPIO as GPIO
except:
    # Let the block code load anyway so that som unit tests can run.
    pass


class PullUpDownOptions(Enum):
    PUD_UP = True
    PUD_DOWN = False
    PUD_OFF = None


class PullUpDown(PropertyHolder):
    default = SelectProperty(PullUpDownOptions,
                             title="Default Pull Resistor",
                             default=PullUpDownOptions.PUD_OFF)
    # TODO: add ability to select base on pin number


class GPIORead(Block):

    pin = IntProperty(default=0, title="Pin Number")
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
        self._gpio.close()
        super().stop()

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
