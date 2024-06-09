import sys
import os
import unittest
from unittest.mock import patch, Mock

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import change_volume


class TestChangeVolume(unittest.TestCase):

    @patch('functions.change_volume.speak')
    @patch('functions.change_volume.basic_setting_to_change')
    def test_add_volume(self, mock_basic_setting, mock_speak):
        mock_device_volume = Mock()
        mock_basic_setting.return_value = mock_device_volume
        mock_device_volume.GetMasterVolumeLevelScalar.return_value = 0.5
        change_volume.add_volume(10)
        mock_device_volume.SetMasterVolumeLevelScalar.assert_called_once_with(0.6, None)
        mock_speak.assert_called_once_with("Я збільшив гучність")

    @patch('functions.change_volume.speak')
    @patch('functions.change_volume.basic_setting_to_change')
    def test_reduce_volume(self, mock_basic_setting, mock_speak):
        mock_device_volume = Mock()
        mock_basic_setting.return_value = mock_device_volume
        mock_device_volume.GetMasterVolumeLevelScalar.return_value = 0.5
        change_volume.reduce_volume(10)
        mock_device_volume.SetMasterVolumeLevelScalar.assert_called_once_with(0.4, None)
        mock_speak.assert_called_once_with("Я зменьшив гучність")


if __name__ == '__main__':
    unittest.main()
