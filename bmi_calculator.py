# BMI Calculator - Beginner Version (Console Based)
# This program calculates Body Mass Index using user input

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / height (m)^2
    """
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    """
    Determine BMI category based on WHO standards
    """
    if bmi < 18.5:
        return "Underweight - Consider consulting a nutritionist"
    elif 18.5 <= bmi < 25:
        return "Normal weight - Maintain your healthy lifestyle"
    elif 25 <= bmi < 30:
        return "Overweight - Exercise regularly and eat balanced food"
    else:
        return "Obese - Please consult a healthcare professional"


def main():
    print("=" * 50)
    print("WELCOME TO BMI CALCULATOR".center(50))
    print("=" * 50)

    while True:
        try:
            # Input weight
            weight = float(input("\nEnter your weight in kilograms (kg): "))
            if weight <= 0:
                print("❌ Weight must be greater than zero!")
                continue

            # Input height
            height = float(input("Enter your height in meters (m): "))
            if height <= 0:
                print("❌ Height must be greater than zero!")
                continue

            break

        except ValueError:
            print("❌ Please enter valid numeric values!")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    # Display result
    print("\n" + "=" * 50)
    print("BMI RESULT".center(50))
    print("=" * 50)
    print(f"Your BMI value is: {bmi:.2f}")
    print(f"Category: {category}")
    print("=" * 50)

    # Repeat option
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again == "yes" or again == "y":
        main()
    else:
        print("\nThank you for using BMI Calculator!")
        print("Stay healthy 💪")


# Program entry point
if __name__ == "__main__":
    main()
