class SmartBillCalculator:
    def __init__(self, rate_per_kwh=0.15):
        self.rate_per_kwh = rate_per_kwh

    def calculate_bill(self, usage_kwh):
        """Calculates the total cost."""
        return usage_kwh * self.rate_per_kwh

    def get_suggestions(self, usage_kwh):
        """
        Analyzes usage and returns a list of smart suggestions
        to reduce the bill.
        """
        suggestions = []
        
        # Logic 1: High Usage Alert
        if usage_kwh > 500:
            suggestions.append("⚠️ ALERT: Your usage is extremely high (>500 kWh).")
            suggestions.append("💡 Tip: Check for faulty appliances or old wiring that might be draining power.")
        
        # Logic 2: Heating/Cooling (Assumes high usage is often due to HVAC)
        elif usage_kwh > 300:
            suggestions.append("⚠️ NOTICE: Your usage is moderate-high.")
            suggestions.append("🌡️ Tip: Adjust your thermostat by 1-2 degrees. Heating/cooling accounts for ~50% of bills.")
            suggestions.append("⏰ Tip: Use heavy curtains to block heat in summer or keep heat in winter.")

        # Logic 3: Moderate Usage
        elif usage_kwh > 150:
            suggestions.append("✅ Status: Usage is within normal range.")
            suggestions.append("🧹 Tip: Unplug devices (TV, PC) when not in use to eliminate 'phantom' load.")

        # Logic 4: Low Usage
        else:
            suggestions.append("🌟 Excellent! Your usage is very low.")
            suggestions.append("💡 Tip: You are already efficient! Consider switching to LED bulbs if you haven't already.")

        return suggestions

    def generate_report(self, usage_kwh):
        """Generates the final report."""
        bill_amount = self.calculate_bill(usage_kwh)
        tips = self.get_suggestions(usage_kwh)

        print("\n" + "="*40)
        print("      SMART ELECTRICITY BILL REPORT")
        print("="*40)
        print(f"Monthly Usage : {usage_kwh} kWh")
        print(f"Rate per Unit : ${self.rate_per_kwh}")
        print("-" * 40)
        print(f"TOTAL BILL    : ${bill_amount:.2f}")
        print("-" * 40)
        print("SMART SUGGESTIONS:")
        for tip in tips:
            print(f"  {tip}")
        print("="*40 + "\n")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Initialize calculator (Rate is $0.15 per kWh)
    calculator = SmartBillCalculator(rate_per_kwh=0.15)

    print("--- Smart Electricity Bill Calculator ---")
    try:
        # Get user input
        input_usage = float(input("Enter your monthly electricity usage (kWh): "))
        
        # Generate and display the report
        calculator.generate_report(input_usage)
        
    except ValueError:
        print("Invalid input! Please enter a numeric value (e.g., 250).")


