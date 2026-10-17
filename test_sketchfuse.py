# test_sketchfuse.py
"""
Tests for SketchFuse module.
"""

import unittest
from sketchfuse import SketchFuse

class TestSketchFuse(unittest.TestCase):
    """Test cases for SketchFuse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchFuse()
        self.assertIsInstance(instance, SketchFuse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchFuse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
