"""
Core calculator module for apartment cost calculations.
"""


class ApartmentCostCalculator:
    """
    Calculator for determining the effective cost of buying an apartment.
    
    Attributes:
        apartment_cost (float): The purchase price of the apartment
        monthly_rent (float): The monthly rent that could be earned or saved
        amortization_years (int): Number of years to amortize the cost
        location (str): Location of the apartment
    """
    
    def __init__(self, apartment_cost, monthly_rent, amortization_years, location):
        """
        Initialize the apartment cost calculator.
        
        Args:
            apartment_cost (float): Purchase price of the apartment
            monthly_rent (float): Monthly rent amount
            amortization_years (int): Years for amortization
            location (str): Location of the apartment
        """
        self.apartment_cost = float(apartment_cost)
        self.monthly_rent = float(monthly_rent)
        self.amortization_years = int(amortization_years)
        self.location = location
        
    def calculate_monthly_cost(self):
        """
        Calculate the monthly cost based on amortization.
        
        Returns:
            float: Monthly cost of the apartment
        """
        if self.amortization_years <= 0:
            raise ValueError("Amortization years must be positive")
        
        total_months = self.amortization_years * 12
        return self.apartment_cost / total_months
    
    def calculate_net_monthly_cost(self):
        """
        Calculate net monthly cost considering potential rental income.
        
        Returns:
            float: Net monthly cost (cost minus rent)
        """
        monthly_cost = self.calculate_monthly_cost()
        return monthly_cost - self.monthly_rent
    
    def calculate_total_cost(self):
        """
        Calculate total cost over the amortization period.
        
        Returns:
            float: Total cost of ownership
        """
        return self.apartment_cost
    
    def calculate_break_even_years(self):
        """
        Calculate how many years until the apartment cost is recovered through rent.
        
        Returns:
            float: Years to break even, or None if rent is 0
        """
        if self.monthly_rent <= 0:
            return None
        
        return self.apartment_cost / (self.monthly_rent * 12)
    
    def get_summary(self):
        """
        Get a comprehensive summary of the apartment costs.
        
        Returns:
            dict: Dictionary containing all calculated metrics
        """
        monthly_cost = self.calculate_monthly_cost()
        net_monthly_cost = self.calculate_net_monthly_cost()
        break_even = self.calculate_break_even_years()
        
        return {
            'location': self.location,
            'apartment_cost': self.apartment_cost,
            'monthly_rent': self.monthly_rent,
            'amortization_years': self.amortization_years,
            'monthly_amortization_cost': monthly_cost,
            'net_monthly_cost': net_monthly_cost,
            'total_cost': self.calculate_total_cost(),
            'break_even_years': break_even,
        }
