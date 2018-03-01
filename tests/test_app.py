import unittest
from click.testing import CliRunner
from mock import patch
from app import entry_point

class TestApp(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_app_output(self):
        result = self.runner.invoke(entry_point, ['--opt1', 'Hi', '--opt2', 'You', 'cmd'])
        self.assertEqual(result.output, 'Options are: Hi and You\n')

    def test_app_raise(self):
        self.assertRaises(RuntimeError, self.runner.invoke, entry_point, ['--opt1', 'Hi', '--opt2', 'You', 'cmd'], None, None, False)

    def test_app_should_not_raise(self):
        with patch('commands.cmd.do_something_useful', return_value = None):
            result = self.runner.invoke(entry_point, ['--opt1', 'Hi', '--opt2', 'You', 'cmd'], None, None, False)
            self.assertIn("Options are: Hi and You", result.output)
