# test_tidesway.py
"""
Tests for TideSway module.
"""

import unittest
from tidesway import TideSway

class TestTideSway(unittest.TestCase):
    """Test cases for TideSway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TideSway()
        self.assertIsInstance(instance, TideSway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TideSway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
