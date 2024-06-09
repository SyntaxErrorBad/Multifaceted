import sys
import os
import unittest
from unittest.mock import patch, Mock

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import change_window


class TestChangeWindow(unittest.TestCase):

    @patch('functions.change_window.speak')
    @patch('functions.change_window.gw.getAllWindows')
    def test_change_current_window(self, mock_getAllWindows, mock_speak):
        mock_window = Mock()
        mock_getAllWindows.return_value = [mock_window]
        with patch('functions.change_window.get_window_process_name', return_value='test.exe'):
            change_window.change_current_window('test.exe')
            mock_window.restore.assert_called_once()
            mock_window.activate.assert_called_once()
            mock_speak.assert_called_once_with("Ваше вікно відкрите")

if __name__ == '__main__':
    unittest.main()
