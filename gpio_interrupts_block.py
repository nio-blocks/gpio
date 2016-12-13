from nio.signal.base import Signal
from nio.util.discovery import discoverable

from .gpio_base_block import GPIOBase



@discoverable
class GPIOInterrupts(GPIOBase):

    def start(self):
        # TODO: allow more than one pin to be configured per block
        self._gpio.interrupt(
            self._callback, self.pin(), self.pull_up_down().default().value)
        super().start()

    def _callback(self, channel):
        self.logger.debug(
            "Interrupt callback invoked by pin: {}".format(channel))
        self.notify_signals(Signal({"pin": channel}))
