from unittest import skip
from unittest.mock import patch

from nio.testing.block_test_case import NIOBlockTestCase

from ..gpio_device import GPIODevice


class TestGPIODevice(NIOBlockTestCase):

    @skip("Only run on a raspbeery pi")
    def test_read(self):
        """Test that gpio read returns a value dict."""
        with patch('RPi.GPIO.setmode') as mock_setmode:
            gpio = GPIODevice()
        with patch('RPi.GPIO.setup') as mock_setup:
            with patch('RPi.GPIO.input') as mock_input:
                mock_input.return_value = True
                value = gpio.read(0)
        with patch('RPi.GPIO.cleanup') as mock_cleanup:
            gpio.close()
        self.assertDictEqual(value, {"value": True})

    @skip("Only run on a raspbeery pi")
    def test_write(self):
        """Test that gpio write calls output with the specified value."""
        with patch('RPi.GPIO.setmode') as mock_setmode:
            gpio = GPIODevice()
        with patch('RPi.GPIO.setup') as mock_setup:
            with patch('RPi.GPIO.output') as mock_output:
                value = gpio.write(0, False)
                mock_output.called_once_with(0, False)
        with patch('RPi.GPIO.cleanup') as mock_cleanup:
            gpio.close()

    def _callback(self, pin):
        pass

    @skip("Only run on a raspbeery pi")
    def test_interrupt(self):
        """Test that gpio interrupts can be set."""
        with patch('RPi.GPIO.setmode') as mock_setmode:
            gpio = GPIODevice()
        with patch('RPi.GPIO.setup') as mock_setup:
            with patch('RPi.GPIO.add_event_detection') as mock_detection:
                with patch('RPi.GPIO.add_event_callback') as mock_callback:
                    gpio.interrupt(self._callback, 0)
        with patch('RPi.GPIO.cleanup') as mock_cleanup:
            gpio.close()
        mock_detection.called_once_with(0, GPIO.BOTH)
        mock_callback.called_once_with(0, self._callback)
