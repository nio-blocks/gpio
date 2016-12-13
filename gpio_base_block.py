from enum import Enum

from nio.block.base import Block
from nio.properties import (IntProperty, VersionProperty, SelectProperty,
                            ObjectProperty, PropertyHolder)
from nio.util.discovery import not_discoverable

from .gpio_device import GPIODevice, GPIOMode

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


@not_discoverable
class GPIOBase(Block):

    pin = IntProperty(default=0, title="Pin Number")
    version = VersionProperty('0.1.0')
    pull_up_down = ObjectProperty(PullUpDown,
                                  title="Pull Resistor Up/Down",
                                  default=PullUpDown())
    gpio_mode = SelectProperty(GPIOMode, title='GPIO mode', default='BCM')

    def __init__(self):
        super().__init__()
        self._gpio = None

    def configure(self, context):
        super().configure(context)
        self._gpio = GPIODevice(self.logger, gpio_mode=self.gpio_mode())

    def stop(self):
        self._gpio.close()
        super().stop()
