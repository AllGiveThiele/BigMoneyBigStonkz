class Houses():
    def __init__(self, kontantinsats: int, månadsinkomst: int, houses_list=None):
        self.kontantinsats = kontantinsats
        self.månadsinkomst = månadsinkomst
        self.houses = houses_list if houses_list is not None else []
    
    def add_house(self, house_spec):
        """Add a single house (Specs object) to the houses list"""
        self.houses.append(house_spec)
    
    def display_houses(self):
        """Display all houses in a formatted way"""
        print(f"\n=== Houses Portfolio ===")
        print(f"Kontantinsats: {self.kontantinsats:,} kr")
        print(f"Månadsinkomst: {self.månadsinkomst:,} kr")
        print(f"Number of houses: {len(self.houses)}")
        print("\nHouses:")
        for i, house in enumerate(self.houses, 1):
            print(f"{i}. {house.adress}")
            print(f"   Budpris: {house.budpris:,} kr")
            print(f"   Kvm: {house.kvm}")
            print(f"   Amortering: {house.ammorteringsprocent}%")
            print(f"   Ränta: {house.räntaprocent}%")
            print(f"   Kommunalskatt: {house.kommunalskatt*100:.2f}%")
            print(f"   Avgift: {house.avgift:,} kr/month")
            print()
    

    def analyze_time_periods(self, periods_in_months: list):
        """Analyze costs over multiple time periods"""
        print(f"\n=== Cost Analysis Over Different Time Periods ===")
        
        for house in self.houses:
            print(f"\n{house.adress}:")
            print(f"{'Period':<15} {'Monthly Payment':<15} {'Amortization Cost':<15} {'Interest Cost':<15} {'Remaining Money':<15} {'Remaining Loan':<15}")
            print("-" * 95)
            
            for months in periods_in_months:
                breakdown = house.calculate_total_payment(months, self.kontantinsats, self.månadsinkomst)
                years = months / 12
                period_str = f"{months}m ({years:.1f}y)"

                print(f"{period_str:<15} {breakdown['monthly_payment']:<15.2f} {breakdown['total_amortization']:<15,.0f} {breakdown['total_interest']:<15,.0f} {breakdown['total_remaining']:<15,.0f} {breakdown['remaining_loan']:<15,.0f}")
class Specs():
    def __init__(self,
                 adress: str,
                 budpris: int,
                 ammorteringsprocent: float,
                 räntaprocent: float,
                 kvm : int,
                 kommunalskatt : float,
                 avgift: int):
        self.adress = adress
        self.budpris = budpris
        self.ammorteringsprocent = ammorteringsprocent
        self.räntaprocent = räntaprocent
        self.kvm = kvm
        self.kommunalskatt = kommunalskatt
        self.avgift = avgift
    
    def calculate_total_payment(self, months: int, kontantinsats: int = 0, monthly_income: int = 0):
        """
        Calculate total payment for the apartment over specified months
        
        Args:
            months: Number of months to calculate for
            kontantinsats: Down payment amount (default 0)
            monthly_income: Monthly income for calculating remaining money (default 0)
            
        Returns:
            dict: Dictionary containing breakdown of payments
        """
        # Calculate loan amount (after down payment)
        loan_amount = self.budpris - kontantinsats
        
        # Monthly interest rate
        monthly_interest_rate = self.räntaprocent / 100 / 12
        
        # Monthly amortization amount
        monthly_amortization = (loan_amount * self.ammorteringsprocent / 100) / 12
        
        # Monthly interest payment (calculated on remaining loan amount)
        # For simplicity, we'll calculate average interest over the period
        # In reality, this would decrease as the loan is paid down
        average_loan_balance = loan_amount - (monthly_amortization * months / 2)
        monthly_interest = average_loan_balance * monthly_interest_rate
        
        # Total monthly payment (amortization + interest + avgift)
        monthly_payment = monthly_amortization + monthly_interest + self.avgift
        
        # Monthly tax calculation (kommunalskatt on income)
        monthly_tax = monthly_income * self.kommunalskatt if monthly_income > 0 else 0
        
        # Monthly remaining money after payment and taxes
        monthly_remaining = monthly_income - monthly_payment - monthly_tax if monthly_income > 0 else 0
        
        # Total payments over the period
        total_amortization = monthly_amortization * months
        total_interest = monthly_interest * months
        total_avgift = self.avgift * months
        total_monthly_payments = monthly_payment * months
        total_tax = monthly_tax * months
        total_remaining = monthly_remaining * months
        total_paid = total_monthly_payments
        
        return {
            'months': months,
            'kontantinsats': kontantinsats,
            'loan_amount': loan_amount,
            'monthly_amortization': monthly_amortization,
            'monthly_interest': monthly_interest,
            'monthly_avgift': self.avgift,
            'monthly_payment': monthly_payment,
            'monthly_tax': monthly_tax,
            'monthly_remaining': monthly_remaining,
            'total_amortization': total_amortization,
            'total_interest': total_interest,
            'total_avgift': total_avgift,
            'total_monthly_payments': total_monthly_payments,
            'total_tax': total_tax,
            'total_remaining': total_remaining,
            'total_paid': total_paid,
            'remaining_loan': loan_amount - total_amortization
        }
    
    def display_payment_breakdown(self, months: int, kontantinsats: int = 0, monthly_income: int = 0):
        """
        Display a formatted breakdown of payments for the apartment
        """
        breakdown = self.calculate_total_payment(months, kontantinsats, monthly_income)
        
        print(f"\n=== Payment Breakdown for {self.adress} ===")
        print(f"Time period: {months} months ({months/12:.1f} years)")
        print(f"Apartment price: {self.budpris:,} kr")
        print(f"Down payment: {kontantinsats:,} kr")
        print(f"Loan amount: {breakdown['loan_amount']:,} kr")
        print(f"\nMonthly payments:")
        print(f"  Amortization: {breakdown['monthly_amortization']:.2f} kr")
        print(f"  Interest: {breakdown['monthly_interest']:.2f} kr")
        print(f"  Avgift: {breakdown['monthly_avgift']:.2f} kr")
        print(f"  Total monthly: {breakdown['monthly_payment']:.2f} kr")
        print(f"\nTotal over {months} months:")
        print(f"  Total amortization: {breakdown['total_amortization']:,.2f} kr")
        print(f"  Total interest: {breakdown['total_interest']:,.2f} kr")
        print(f"  Total avgift: {breakdown['total_avgift']:,.2f} kr")
        print(f"  Total monthly payments: {breakdown['total_monthly_payments']:,.2f} kr")
        print(f"  Total paid (including down payment): {breakdown['total_paid']:,.2f} kr")
        print(f"  Remaining loan: {breakdown['remaining_loan']:,.2f} kr")
        print(f"\nEffective cost: {breakdown['total_paid'] - breakdown['total_amortization']:,.2f} kr")
        print(f"  (Down payment + Interest paid)")


class ReadInData():
    def __init__(self):
        pass
    
    def read_houses_from_dict(self, houses_dict):
        """
        Reads house data from a dictionary and returns a list of Specs objects
        """
        specs_list = []
        
        for address, house_data in houses_dict.items():
            # Create a Specs object for each house
            house_spec = Specs(
                adress=address,
                budpris=house_data["Budpris"],
                ammorteringsprocent=house_data["amorteringprocent"],
                räntaprocent=house_data["räntaprocent"],
                kvm=house_data["kvm"],
                kommunalskatt=house_data["kommunalskatt"],
                avgift=house_data["avgift"]
            )
            specs_list.append(house_spec)
        
        return specs_list
    
    def read_portfolio_data(self, portfolio_dict):
        """
        Reads portfolio data and returns kontantinsats and månadsinkomst
        """
        return {
            'kontantinsats': portfolio_dict["kontantinsats"],
            'månadsinkomst': portfolio_dict["månadsinkomst"]
        }
    
    def create_houses_from_data(self, houses_dict, portfolio_dict):
        """
        Creates a complete Houses object from both houses and portfolio data
        """
        house_specs = self.read_houses_from_dict(houses_dict)
        portfolio_data = self.read_portfolio_data(portfolio_dict)
        
        return Houses(
            kontantinsats=portfolio_data['kontantinsats'],
            månadsinkomst=portfolio_data['månadsinkomst'],
            houses_list=house_specs
        )










