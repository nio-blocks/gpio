from nio.util.discovery import discoverable
from .gpio_base_block import GPIOBase


@discoverable
class GPIORead(GPIOBase):

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
