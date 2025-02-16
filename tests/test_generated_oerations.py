from app.calculator import Calculator


def test_generated_operations(num1, num2, operation, expected_result):
    result = Calculator.compute(operation, float(num1), float(num2))
    assert result == expected_result
