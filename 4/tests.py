import pytest
import json

from main import delta_function, fibonacci, gcd


def read_file(string):
    f = open(string + '.json')
    data = json.load(f)
    test_data = data['data']
    f.close()
    return test_data


class TestDeltaFunction:

    @classmethod
    def setup_class(cls):
        print('\n----setup delta tests----')

    @classmethod
    def teardown_class(cls):
        print('\n----teardown delta tests----')

    test_data = read_file('delta')

    @pytest.mark.parametrize("a, b, c", [(0.5, 2, 3)])
    def test_negative_result_value(self, a, b, c):
        assert delta_function(a, b, c) == -2

    @pytest.mark.parametrize("a, b, c", [(0.5, 5, 3)])
    def test_positive_result_value(self, a, b, c):
        assert delta_function(a, b, c) == 19

    @pytest.mark.parametrize("a, b, c", [(0.5, 5, "t")])
    def test_non_numeric_input_should_throw_exception(self, a, b, c):
        with pytest.raises(TypeError):
            delta_function(a, b, c)

    @pytest.mark.parametrize("a, b, c, expected", test_data)
    def test_user_provided(self, a, b, c, expected):
        assert delta_function(a, b, c) == expected


class TestFibonacci:
    @classmethod
    def setup_class(cls):
        print('\n----setup Fibonacci tests----')

    @classmethod
    def teardown_class(cls):
        print('\n----teardown Fibonacci tests----')

    test_data = read_file('fibonacci')

    @pytest.mark.parametrize("n", [-4])
    def test_provided_negative_value(self, n):
        with pytest.raises(RecursionError):
            assert fibonacci(n) == -2

    @pytest.mark.parametrize("n", [5])
    def test_positive_result_value(self, n):
        assert fibonacci(n) == 5

    @pytest.mark.parametrize("n", ["t"])
    def test_non_numeric_input_should_throw_exception(self, n):
        with pytest.raises(TypeError):
            assert fibonacci(n)

    @pytest.mark.parametrize("n, expected", test_data)
    def test_user_provided(self, n, expected):
        assert fibonacci(n) == expected


class TestGCD:

    @classmethod
    def setup_class(cls):
        print('\n----setup GCD tests----')

    @classmethod
    def teardown_class(cls):
        print('\n----teardown GCD tests----')

    test_data = read_file('gcd')

    @pytest.mark.parametrize("a, b", [(-4, -2)])
    def test_provided_negative_values(self, a, b):
        assert gcd(a, b) == -2

    @pytest.mark.parametrize("a, b", [(150, 50)])
    def test_provided_positive_values(self, a, b):
        assert gcd(a, b) == 50

    @pytest.mark.parametrize("a, b", [("t", "t")])
    def test_non_numeric_input_should_throw_exception(self, a, b):
        with pytest.raises(TypeError):
            assert gcd(a, b)

    @pytest.mark.parametrize("a, b, expected", test_data)
    def test_user_provided(self, a, b, expected):
        assert gcd(a, b) == expected
