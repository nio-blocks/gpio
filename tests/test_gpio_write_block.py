from unittest import skip
from unittest.mock import MagicMock, patch
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..gpio_write_block import GPIOWrite
from ..gpio_device import GPIODevice


class TestGPIOWrite(NIOBlockTestCase):

    @patch(GPIOWrite.__module__ + ".GPIODevice", spec=GPIODevice)
    def test_process_signals(self, mock_gpio):
        """Signals pass through block unmodified."""
        blk = GPIOWrite()
        self.configure_block(blk, {})
        blk._gpio.write.return_value = True
        blk.start()
        blk.process_signals([Signal({"my": "signal"})])
        blk.stop()
        blk._gpio.write.assert_called_once_with(0, False)
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"my": "signal"})
