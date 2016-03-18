from unittest import skip
from unittest.mock import MagicMock, patch
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..gpio_read_block import GPIORead, GPIODevice


class TestGPIORead(NIOBlockTestCase):

    @patch(GPIODevice.__module__ + ".GPIODevice", spec=GPIODevice)
    def test_process_signals(self, mock_gpio):
        """Signals pass through block unmodified."""
        blk = GPIORead()
        self.configure_block(blk, {})
        blk._gpio.read.return_value = True
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        blk._gpio.read.assert_called_once_with(0)
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"value": True})

    @skip("Only run on a raspbeery pi")
    def test_raspberry_pi(self):
        """Raspberry pi uses RPi.GPIO library."""
        blk = GPIORead()
        with patch('RPi.GPIO.setmode') as mock_setmode:
            self.configure_block(blk, {})
        blk.start()
        with patch('RPi.GPIO.setup') as mock_setup:
            with patch('RPi.GPIO.input') as mock_input:
                mock_input.return_value = True
                blk.process_signals([Signal()])
        with patch('RPi.GPIO.cleanup') as mock_cleanup:
            blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"value": True})
        mock_input.assert_called_once_with(0)
