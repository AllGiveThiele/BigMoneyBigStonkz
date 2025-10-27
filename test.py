print("Hello from test.py")

try:
    from Houses import Houses, ReadInData
    print("Successfully imported Houses and ReadInData")
except Exception as e:
    print(f"Import error: {e}")

try:
    from data import HousesOfInterest, MinPortfolio
    print("Successfully imported data")
    print(f"Houses: {list(HousesOfInterest.keys())}")
    print(f"Portfolio: {MinPortfolio}")
except Exception as e:
    print(f"Data import error: {e}")
