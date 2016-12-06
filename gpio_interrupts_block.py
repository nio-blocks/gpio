from enum import Enum
from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
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


class GPIOMode(Enum):
    BCM = GPIO.BCM
    BOARD = GPIO.BOARD


class PullUpDown(PropertyHolder):
    default = SelectProperty(PullUpDownOptions,
                             title="Default Pull Resistor",
                             default=PullUpDownOptions.PUD_OFF)
    # TODO: add ability to select base on pin number


@discoverable
class GPIOInterrupts(Block):

    pin = IntProperty(default=0, title="Pin Number")
    version = VersionProperty('0.1.0')
    pull_up_down = ObjectProperty(PullUpDown,
                                  title="Pull Resistor Up/Down",
                                  default=PullUpDown())
    gpio_mode = SelectProperty(GPIOMode, title='GPIO mode', default='BCM')

    def __init__(self):
        super().__init__()
        self._gpio = None

    def start(self):
        # TODO: allow more than one pin to be configured per block
        self._gpio.interrupt(
            self._callback, self.pin(), self.pull_up_down().default().value)
        super().start()

    def configure(self, context):
        super().configure(context)
        self._gpio = GPIODevice(self.logger, gpio_mode=self.gpio_mode())

    def stop(self):
        self._gpio.close()
        super().stop()

    def process_signals(self, signals):
        pass

    def _callback(self, channel):
        self.logger.debug(
            "Interrupt callback invoked by pin: {}".format(channel))
        self.notify_signals(Signal({"pin": channel}))
