import sys
import os
import unittest
from unittest.mock import patch
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import open_file


class TestOpenFile(unittest.TestCase):

    @patch('functions.open_file.speak')
    @patch('functions.open_file.os.startfile')
    def test_open_file_by_path(self, mock_startfile, mock_speak):
        open_file.open_file_by_path('test_path')
        mock_startfile.assert_called_once_with('test_path')
        mock_speak.assert_called_once_with("Ваша папка відкрита")


if __name__ == '__main__':
    unittest.main()
