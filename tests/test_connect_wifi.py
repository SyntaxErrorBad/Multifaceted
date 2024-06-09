import sys
import os
import unittest
from unittest.mock import patch

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import connect_wifi


class TestConnectWifi(unittest.TestCase):

    @patch('functions.connect_wifi.speak')
    @patch('functions.connect_wifi.subprocess.check_output')
    def test_connect_to_wifi_success(self, mock_check_output, mock_speak):
        mock_check_output.return_value = "Connected"
        connect_wifi.connect_to_wifi('test_ssid')
        mock_speak.assert_called_once_with("Я успішно вас підключив")

    @patch('functions.connect_wifi.speak')
    @patch('functions.connect_wifi.subprocess.check_output', side_effect=subprocess.CalledProcessError(1, 'cmd', 'Error'))
    def test_connect_to_wifi_failure(self, mock_check_output, mock_speak):
        connect_wifi.connect_to_wifi('test_ssid')
        mock_speak.assert_called_once_with("Нажаль виникла помилка підчас підключення")


if __name__ == '__main__':
    unittest.main()
