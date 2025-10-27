"""
Location data module for managing location-specific information.
"""


class LocationData:
    """
    Manages location-specific data and multipliers.
    
    This can be extended to include location-specific costs,
    tax rates, and market factors.
    """
    
    # Default location multipliers (can be customized)
    LOCATION_MULTIPLIERS = {
        'downtown': 1.3,
        'suburban': 1.0,
        'rural': 0.7,
    }
    
    @classmethod
    def get_location_multiplier(cls, location):
        """
        Get the cost multiplier for a specific location type.
        
        Args:
            location (str): Location identifier
            
        Returns:
            float: Multiplier for the location (default 1.0)
        """
        location_lower = location.lower()
        
        # Check for keyword matches
        for key, multiplier in cls.LOCATION_MULTIPLIERS.items():
            if key in location_lower:
                return multiplier
        
        return 1.0
    
    @classmethod
    def add_location_multiplier(cls, location_type, multiplier):
        """
        Add or update a location multiplier.
        
        Args:
            location_type (str): Type of location
            multiplier (float): Cost multiplier
        """
        cls.LOCATION_MULTIPLIERS[location_type.lower()] = multiplier
    
    @classmethod
    def get_all_locations(cls):
        """
        Get all available location types and their multipliers.
        
        Returns:
            dict: Dictionary of location types and multipliers
        """
        return cls.LOCATION_MULTIPLIERS.copy()
