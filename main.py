import importlib
import sys
from Houses import Houses, ReadInData

def main():
    # Auto-reload data module to get fresh data on each run
    if 'data' in sys.modules:
        importlib.reload(sys.modules['data'])
    
    # Import data inside function to ensure fresh data
    from data import HousesOfInterest, MinPortfolio
    
    print("Loading house data and portfolio information...")
    
    # Create ReadInData instance and load all data
    data_reader = ReadInData()
    
    # Create Houses instance with all data from data.py
    houses = data_reader.create_houses_from_data(HousesOfInterest, MinPortfolio)
    
    # Display summary information
    print(f"Portfolio loaded: {len(houses.houses)} houses")
    print(f"Kontantinsats: {houses.kontantinsats:,} kr")
    print(f"Månadsinkomst: {houses.månadsinkomst:,} kr")
    
    # Analyze different time periods for 5 years
    time_periods = [12, 24, 36, 48, 60]  # 1, 2, 3, 4, 5 years
    houses.analyze_time_periods(time_periods)




if __name__ == "__main__":
    main()
