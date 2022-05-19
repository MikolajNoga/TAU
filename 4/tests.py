import pytest
from main import delta_function, fibonacci, gcd


class TestDeltaFunction:
    def test_negative_result_value(self):
        assert delta_function(0.5, 2, 3) == -2

    def test_positive_result_value(self):
        assert delta_function(0.5, 5, 3) == 19

    def test_non_numeric_input_should_throw_exception(self):
        with pytest.raises(TypeError):
            delta_function(0.5, 5, "t")


class TestFibonacci:
    def test_provided_negative_value(self):
        with pytest.raises(RecursionError):
            assert fibonacci(-4) == -2

    def test_positive_result_value(self):
        assert fibonacci(5) == 5

    def test_non_numeric_input_should_throw_exception(self):
        with pytest.raises(TypeError):
            assert fibonacci('t')

class TestGCD:
    def test_provided_negative_values(self):
        assert gcd(-4, -2) == -2

    def test_provided_positive_values(self):
        assert gcd(150, 50) == 50

    def test_non_numeric_input_should_throw_exception(self):
        with pytest.raises(TypeError):
            assert gcd("t", "t")