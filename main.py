from app.calculator import Calculator

if __name__ == "__main__":
    try:
        Calculator.run()
    except Exception as e:
        print(f"An error occurred: {e}")
