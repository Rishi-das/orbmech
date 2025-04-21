import unittest
from orbmech.core import simulate_orbit, classify_orbit

class TestOrbMechPackage(unittest.TestCase):
    """
    Unit tests to ensure the functionality of the `orbmech` package.
    """

    def test_simulate_orbit(self):
        """
        Test the `simulate_orbit` function to ensure it returns valid results.
        """
        initial_conditions = {'semi_major_axis': 1.0, 'eccentricity': 0.1}
        
        # Run the orbit simulation
        result = simulate_orbit(initial_conditions)
        
        # Ensure that the result is not empty and contains expected keys
        self.assertIn('position', result)
        self.assertIn('velocity', result)
        self.assertGreater(len(result['position']), 0)  # Check if there are positions in the result

    def test_classify_orbit(self):
        """
        Test the `classify_orbit` function to verify it classifies orbits correctly.
        """
        result = {'eccentricity': 0.2}  # Example of elliptical orbit
        orbit_type = classify_orbit(result)
        
        # Assert that the orbit type is 'Elliptical Orbit'
        self.assertEqual(orbit_type, "Elliptical Orbit")
