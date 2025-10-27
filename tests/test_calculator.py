"""
Unit tests for the Apartment Cost Calculator.
"""

import unittest
import sys
import os

# Add parent directory to path to import apartment_calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apartment_calculator.calculator import ApartmentCostCalculator
from apartment_calculator.location_data import LocationData


class TestApartmentCostCalculator(unittest.TestCase):
    """Test cases for ApartmentCostCalculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calculator = ApartmentCostCalculator(
            apartment_cost=500000,
            monthly_rent=2500,
            amortization_years=30,
            location="Downtown NYC"
        )
    
    def test_initialization(self):
        """Test calculator initialization."""
        self.assertEqual(self.calculator.apartment_cost, 500000)
        self.assertEqual(self.calculator.monthly_rent, 2500)
        self.assertEqual(self.calculator.amortization_years, 30)
        self.assertEqual(self.calculator.location, "Downtown NYC")
    
    def test_calculate_monthly_cost(self):
        """Test monthly cost calculation."""
        monthly_cost = self.calculator.calculate_monthly_cost()
        expected = 500000 / (30 * 12)
        self.assertAlmostEqual(monthly_cost, expected, places=2)
    
    def test_calculate_net_monthly_cost(self):
        """Test net monthly cost calculation."""
        net_cost = self.calculator.calculate_net_monthly_cost()
        monthly_cost = 500000 / (30 * 12)
        expected = monthly_cost - 2500
        self.assertAlmostEqual(net_cost, expected, places=2)
    
    def test_get_apartment_cost(self):
        """Test apartment cost getter."""
        cost = self.calculator.get_apartment_cost()
        self.assertEqual(cost, 500000)
    
    def test_calculate_break_even_years(self):
        """Test break-even calculation."""
        break_even = self.calculator.calculate_break_even_years()
        expected = 500000 / (2500 * 12)
        self.assertAlmostEqual(break_even, expected, places=2)
    
    def test_break_even_with_zero_rent(self):
        """Test break-even calculation with zero rent."""
        calc = ApartmentCostCalculator(300000, 0, 20, "Test Location")
        break_even = calc.calculate_break_even_years()
        self.assertIsNone(break_even)
    
    def test_get_summary(self):
        """Test summary generation."""
        summary = self.calculator.get_summary()
        
        self.assertIn('location', summary)
        self.assertIn('apartment_cost', summary)
        self.assertIn('monthly_rent', summary)
        self.assertIn('amortization_years', summary)
        self.assertIn('monthly_amortization_cost', summary)
        self.assertIn('net_monthly_cost', summary)
        self.assertIn('break_even_years', summary)
        
        self.assertEqual(summary['location'], "Downtown NYC")
        self.assertEqual(summary['apartment_cost'], 500000)
    
    def test_invalid_amortization(self):
        """Test that invalid amortization raises error."""
        calc = ApartmentCostCalculator(300000, 1500, 0, "Test")
        with self.assertRaises(ValueError):
            calc.calculate_monthly_cost()


class TestLocationData(unittest.TestCase):
    """Test cases for LocationData class."""
    
    def test_get_location_multiplier_downtown(self):
        """Test downtown location multiplier."""
        multiplier = LocationData.get_location_multiplier("Downtown NYC")
        self.assertEqual(multiplier, 1.3)
    
    def test_get_location_multiplier_suburban(self):
        """Test suburban location multiplier."""
        multiplier = LocationData.get_location_multiplier("Suburban Area")
        self.assertEqual(multiplier, 1.0)
    
    def test_get_location_multiplier_rural(self):
        """Test rural location multiplier."""
        multiplier = LocationData.get_location_multiplier("Rural Vermont")
        self.assertEqual(multiplier, 0.7)
    
    def test_get_location_multiplier_default(self):
        """Test default multiplier for unknown location."""
        multiplier = LocationData.get_location_multiplier("Unknown Place")
        self.assertEqual(multiplier, 1.0)
    
    def test_add_location_multiplier(self):
        """Test adding a new location multiplier."""
        LocationData.add_location_multiplier("urban", 1.2)
        multiplier = LocationData.get_location_multiplier("urban area")
        self.assertEqual(multiplier, 1.2)
    
    def test_get_all_locations(self):
        """Test retrieving all location multipliers."""
        locations = LocationData.get_all_locations()
        self.assertIsInstance(locations, dict)
        self.assertIn('downtown', locations)
        self.assertIn('suburban', locations)
        self.assertIn('rural', locations)


if __name__ == '__main__':
    unittest.main()
