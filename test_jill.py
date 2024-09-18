import unittest
import subprocess
from unittest.mock import patch

class TestJillScript(unittest.TestCase):
    def test_average_output(self):
        # Run the script with the sample.txt file
        result = subprocess.run(['python3', 'jill.py', 'wordlist.txt', 'passwords.txt'], capture_output=True, text=True)

        # Expected output (replace with the actual expected output)
        expected_output = "tom:maverick\n"
        expected_output += "luke:starwars\n"
        expected_output += "mike:jordan\n"

        # Check if the output matches the expected output
        self.assertEqual(result.stdout, expected_output)

if __name__ == '__main__':
    unittest.main()