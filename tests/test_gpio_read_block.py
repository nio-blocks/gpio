from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..gpio_read_block import GPIORead
from ..gpio_device import GPIODevice


class TestGPIORead(NIOBlockTestCase):

    @patch(GPIORead.__module__ + ".GPIODevice", spec=GPIODevice)
    def test_process_signals(self, mock_gpio):
        """Signals pass through block unmodified."""
        blk = GPIORead()
        self.configure_block(blk, {})
        blk._gpio.read.return_value = True
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        blk._gpio.read.assert_called_once_with(0, None)
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"value": True})
