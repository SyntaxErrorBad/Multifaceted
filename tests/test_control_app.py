import sys
import os
import unittest
from unittest.mock import patch, call
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import control_app


class TestControlApp(unittest.TestCase):

    @patch('functions.control_app.speak')
    @patch('functions.control_app.os.startfile')
    def test_start_application(self, mock_startfile, mock_speak):
        control_app.start_application('test_path')
        mock_startfile.assert_called_once_with('test_path')
        mock_speak.assert_called_once_with("Ваш додаток відкритий")


if __name__ == '__main__':
    unittest.main()
