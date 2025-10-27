# BigMoneyBigStonkz

A comprehensive apartment cost calculator to help you make informed decisions when buying an apartment. This tool calculates various financial metrics including amortization costs, net monthly costs, and break-even analysis.

## Features

- **Interactive Mode**: User-friendly command-line interface for data entry
- **Command-Line Mode**: Direct calculation with command-line arguments
- **Comprehensive Analysis**: Multiple financial metrics including:
  - Monthly amortization cost
  - Net monthly cost (considering rental income)
  - Break-even analysis
  - Total cost of ownership
- **Location Support**: Track apartment locations for comparison
- **Modular Design**: Well-structured codebase for easy extension

## Project Structure

```
BigMoneyBigStonkz/
├── apartment_calculator/      # Main package
│   ├── __init__.py           # Package initialization
│   ├── calculator.py         # Core calculation logic
│   ├── input_handler.py      # User input handling
│   └── location_data.py      # Location-specific data
├── main.py                    # CLI application entry point
├── requirements.txt           # Python dependencies
├── config_example.json        # Example configuration
└── README.md                  # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AllGiveThiele/BigMoneyBigStonkz.git
cd BigMoneyBigStonkz
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (currently none required - uses Python standard library):
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Simply run the main script without arguments:

```bash
python main.py
```

You'll be prompted to enter:
- Cost of the apartment
- Monthly rent
- Amortization period (in years)
- Location of the apartment

### Command-Line Mode

Provide all parameters as command-line arguments:

```bash
python main.py --cost 500000 --rent 2500 --amortization 30 --location "Downtown NYC"
```

### Example Output

```
============================================================
APARTMENT COST ANALYSIS SUMMARY
============================================================

Location: Downtown NYC
Apartment Cost: $500,000.00
Monthly Rent: $2,500.00
Amortization Period: 30 years

------------------------------------------------------------
CALCULATED METRICS
------------------------------------------------------------
Monthly Amortization Cost: $1,388.89
Net Monthly Cost (after rent): $-1,111.11
Total Cost: $500,000.00
Break-even Period: 16.7 years
============================================================
```

## Input Parameters

### Apartment Cost
The purchase price of the apartment. This is the total amount you'll pay for the property.

### Monthly Rent
The monthly rental income you could receive (if renting out) or save (if living there instead of renting elsewhere).

### Amortization
The number of years over which to spread the apartment cost. Common values are 15, 20, 25, or 30 years.

### Location
The location of the apartment. This is used for tracking and can be extended to apply location-specific multipliers or factors.

## Extending the Project

### Adding New Calculations

Edit `apartment_calculator/calculator.py` to add new calculation methods to the `ApartmentCostCalculator` class.

### Location-Specific Factors

The `LocationData` class in `apartment_calculator/location_data.py` can be extended to include:
- Property tax rates by location
- Insurance costs
- Maintenance costs
- Market appreciation rates

### Configuration Files

Use `config_example.json` as a template to create predefined apartment scenarios for quick comparison.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available for personal use.
