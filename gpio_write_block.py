from .gpio_base_block import GPIOBase
from nio.util.discovery import discoverable


@discoverable
class GPIOWrite(GPIOBase):

    def process_signals(self, signals):
        for signal in signals:
            self._write_gpio_pin(self.pin(signal), self.value(signal))
        self.notify_signals(signals)

    def _write_gpio_pin(self, pin, value):
        try:
            return self._gpio.write(pin, value)
        except:
            self.logger.warning(
                "Failed to write value {} to gpio pin: {}".format(value, pin),
                exc_info=True)
