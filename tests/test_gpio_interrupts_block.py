from unittest.mock import patch

from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..gpio_interrupts_block import GPIOInterrupts
from ..gpio_device import GPIODevice


class TestGPIOInterrupts(NIOBlockTestCase):

    @patch(GPIOInterrupts.__module__ + ".GPIODevice", spec=GPIODevice)
    def test_process_signals(self, mock_gpio):
        """Input signals don't do anything."""
        blk = GPIOInterrupts()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(0)

    @patch(GPIOInterrupts.__module__ + ".GPIODevice", spec=GPIODevice)
    def test_interrupt_callback(self, mock_gpio):
        """Test that interrupt callback notifies a signal."""
        blk = GPIOInterrupts()
        self.configure_block(blk, {})
        blk._callback(0)
        self.assert_num_signals_notified(1)
