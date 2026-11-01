12
def calculate_bill():
    try:
        # Prompt the user for input
        input_data = input("Enter the number of units consumed: ")
        
        # Convert input to a float (to handle decimal units if any)
        units = float(input_data)
        
        # Check for negative unit values
        if units < 0:
            raise ValueError("Units consumed cannot be negative!")
            
    except ValueError as e:
        # Handles invalid text input or negative number errors
        print(f"Error: Invalid input ({e}). Please enter a valid positive number.")
        
    else:
        # Executes only if no exception occurred
        bill_amount = 0.0
        
        # Slab-based tariff calculation logic
        if units <= 100:
            bill_amount = units * 1.50  # ₹1.50 per unit for first 100 units
        elif units <= 200:
            bill_amount = (100 * 1.50) + ((units - 100) * 2.50)  # ₹2.50 for next 100 units
        else:
            bill_amount = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)  # ₹4.00 for units above 200
            
        print(f"\n--- Electricity Bill Summary ---")
        print(f"Units Consumed : {units}")
        print(f"Total Bill Amount: ₹{bill_amount:.2f}")
        
    finally:
        # Always executes regardless of whether an error occurred or not
        print("--- Calculation process completed. Thank you! ---\n")

# Run the function
if __name__ == "__main__":
    calculate_bill()