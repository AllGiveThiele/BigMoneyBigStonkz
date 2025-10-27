"""
Input handling module for collecting and validating user inputs.
"""


class InputHandler:
    """Handles user input collection and validation."""
    
    @staticmethod
    def get_float_input(prompt, min_value=0):
        """
        Get a float input from the user with validation.
        
        Args:
            prompt (str): The prompt to display to the user
            min_value (float): Minimum acceptable value
            
        Returns:
            float: Validated float input
        """
        while True:
            try:
                value = float(input(prompt))
                if value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number")
    
    @staticmethod
    def get_int_input(prompt, min_value=1):
        """
        Get an integer input from the user with validation.
        
        Args:
            prompt (str): The prompt to display to the user
            min_value (int): Minimum acceptable value
            
        Returns:
            int: Validated integer input
        """
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid integer")
    
    @staticmethod
    def get_string_input(prompt):
        """
        Get a string input from the user.
        
        Args:
            prompt (str): The prompt to display to the user
            
        Returns:
            str: User input string
        """
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Please enter a non-empty value")
    
    def collect_apartment_data(self):
        """
        Collect all required apartment data from the user.
        
        Returns:
            dict: Dictionary containing all apartment data
        """
        print("\n=== Apartment Cost Calculator ===\n")
        
        cost = self.get_float_input("Enter the cost of the apartment: ", min_value=0)
        rent = self.get_float_input("Enter the monthly rent: ", min_value=0)
        amortization = self.get_int_input("Enter the amortization period (years): ", min_value=1)
        location = self.get_string_input("Enter the location of the apartment: ")
        
        return {
            'apartment_cost': cost,
            'monthly_rent': rent,
            'amortization_years': amortization,
            'location': location
        }
