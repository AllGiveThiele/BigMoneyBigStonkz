#!/usr/bin/env python3
"""
Main entry point for the Apartment Cost Calculator CLI application.
"""

import sys
import argparse
from apartment_calculator.calculator import ApartmentCostCalculator
from apartment_calculator.input_handler import InputHandler
from apartment_calculator.location_data import LocationData


def format_currency(amount):
    """Format a number as currency."""
    return f"${amount:,.2f}"


def display_summary(summary):
    """
    Display a formatted summary of apartment costs.
    
    Args:
        summary (dict): Summary dictionary from calculator
    """
    print("\n" + "="*60)
    print("APARTMENT COST ANALYSIS SUMMARY")
    print("="*60)
    print(f"\nLocation: {summary['location']}")
    print(f"Apartment Cost: {format_currency(summary['apartment_cost'])}")
    print(f"Monthly Rent: {format_currency(summary['monthly_rent'])}")
    print(f"Amortization Period: {summary['amortization_years']} years")
    print("\n" + "-"*60)
    print("CALCULATED METRICS")
    print("-"*60)
    print(f"Monthly Amortization Cost: {format_currency(summary['monthly_amortization_cost'])}")
    print(f"Net Monthly Cost (after rent): {format_currency(summary['net_monthly_cost'])}")
    print(f"Total Cost: {format_currency(summary['total_cost'])}")
    
    if summary['break_even_years'] is not None:
        print(f"Break-even Period: {summary['break_even_years']:.1f} years")
    else:
        print("Break-even Period: N/A (no rental income)")
    
    print("="*60 + "\n")


def interactive_mode():
    """Run the calculator in interactive mode."""
    handler = InputHandler()
    
    # Collect data from user
    data = handler.collect_apartment_data()
    
    # Create calculator and get summary
    calculator = ApartmentCostCalculator(
        apartment_cost=data['apartment_cost'],
        monthly_rent=data['monthly_rent'],
        amortization_years=data['amortization_years'],
        location=data['location']
    )
    
    summary = calculator.get_summary()
    display_summary(summary)


def command_line_mode(args):
    """
    Run the calculator with command-line arguments.
    
    Args:
        args: Parsed command-line arguments
    """
    calculator = ApartmentCostCalculator(
        apartment_cost=args.cost,
        monthly_rent=args.rent,
        amortization_years=args.amortization,
        location=args.location
    )
    
    summary = calculator.get_summary()
    display_summary(summary)


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='Calculate the effective cost of buying an apartment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python main.py

  # Command-line mode
  python main.py --cost 500000 --rent 2500 --amortization 30 --location "Downtown NYC"
        """
    )
    
    parser.add_argument(
        '--cost',
        type=float,
        help='Cost of the apartment'
    )
    
    parser.add_argument(
        '--rent',
        type=float,
        help='Monthly rent amount'
    )
    
    parser.add_argument(
        '--amortization',
        type=int,
        help='Amortization period in years'
    )
    
    parser.add_argument(
        '--location',
        type=str,
        help='Location of the apartment'
    )
    
    args = parser.parse_args()
    
    # Check if all required arguments are provided for command-line mode
    if args.cost is not None or args.rent is not None or args.amortization is not None or args.location is not None:
        # Command-line mode: all arguments must be provided
        if not all([args.cost is not None, args.rent is not None, 
                   args.amortization is not None, args.location is not None]):
            parser.error("When using command-line mode, all arguments (--cost, --rent, --amortization, --location) must be provided")
        
        command_line_mode(args)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
