import sys
import os
import unittest
from unittest.mock import patch, Mock, mock_open
from io import BytesIO

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from functions import do_screenshot


class TestDoScreenshot(unittest.TestCase):

    @patch('functions.do_screenshot.speak')
    @patch('functions.do_screenshot.pyautogui.screenshot')
    @patch('functions.do_screenshot.Image.open')
    @patch('functions.do_screenshot.open', new_callable = mock_open)
    @patch('functions.do_screenshot.os.remove')
    def test_screenshot(self, mock_os_remove, mock_file_open, mock_image_open, mock_screenshot, mock_speak):
        # Мок-об'єкт для зображення
        mock_image = Mock()
        mock_screenshot.return_value = mock_image
        mock_image_open.return_value = mock_image

        # Мок-об'єкт для файлу зображення
        mock_file_open.return_value = BytesIO()

        # Виклик функції скріншоту
        with patch('functions.do_screenshot.os.getenv', return_value = 'True,False'):
            do_screenshot.screenshot()
            mock_image.save.assert_called_once()
            mock_speak.assert_called_once_with("Скріншот зроблено")
            mock_os_remove.assert_called_once()


if __name__ == '__main__':
    unittest.main()
