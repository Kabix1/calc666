from nose.tools import assert_in, assert_equal
import operation.unary
import inverse.unary
import inverse.binary


def get_functions(m):
    return [getattr(m, x) for x in dir(m) if callable(getattr(m, x))]


def test_elementary():
    multiply_5 = operation.unary.elementary(factor=5)
    assert multiply_5(7) == 35
    sum_5 = operation.unary.elementary(summand=5)
    assert sum_5(6) == 11
    power_4 = operation.unary.elementary(power=4)
    assert power_4(4) == 256
    square_root = operation.unary.elementary(power=0.5)
    assert square_root(9) == 3
    combined = operation.unary.elementary(summand=3,
                                          factor=6,
                                          power=2)
    assert combined(5) == 153


def test_factorial():
    fact = operation.unary.factorial()
    assert fact(5) == 120
    assert fact(7) == 5040


def test_elementary_inverse():
    multiply_5 = inverse.unary.elementary(factor=5)
    assert multiply_5(35) == [7]
    sum_5 = inverse.unary.elementary(summand=5)
    assert sum_5(11) == [6]
    power_4 = inverse.unary.elementary(power=4)
    assert power_4(256) == [4, -4]
    square_root = inverse.unary.elementary(power=0.5)
    assert square_root(3) == [9]
    combined = inverse.unary.elementary(summand=3,
                                        factor=6,
                                        power=2)
    assert set(combined(153)) == set([5, -5])


def test_factorial_inverse():
    fact = inverse.unary.factorial()
    assert fact(120) == [5]
    assert fact(5040) == [7]


def test_binary_multiply_inverse():
    multiply = inverse.binary.multiplication()
    assert multiply(21,3) == [7]
    sq = operation.unary.elementary(power=2)
    sq_inv = inverse.unary.elementary(power=2)
    multiply_squares = inverse.binary.multiplication(operation1=sq, inverse1=sq_inv,
                                                     operation2=sq, inverse2=sq_inv)
    assert set(multiply_squares(total=144,arg=3)) == set([-4, 4])


def test_binary_division_inverse():
    division = inverse.binary.division()
    assert set(division(10, 100)) == set([10, 1000])
    sq = operation.unary.elementary(power=2)
    sq_inv = inverse.unary.elementary(power=2)
    division_squares = inverse.binary.division(operation1=sq, inverse1=sq_inv,
                                               operation2=sq, inverse2=sq_inv)
    assert set(division_squares(total=100,arg=100)) == set([10, -10, 1000, -1000])


def test_binary_sum_inverse():
    sum = inverse.binary.sum()
    assert sum(21,3) == [18]
    sq = operation.unary.elementary(power=2)
    sq_inv = inverse.unary.elementary(power=2)
    sum_squares = inverse.binary.sum(operation1=sq, inverse1=sq_inv,
                                     operation2=sq, inverse2=sq_inv)
    assert set(sum_squares(total=25,arg=3)) == set([-4, 4])


def test_all_unary():
    operations = get_functions(operation.unary)
    for ops in operations:
        inv = getattr(inverse.unary, ops.__name__)
        o = ops()
        i = inv()
        for n in range(5, 125):
            assert_in(n, i(o(n)))
            inverses = i(n)
            for num in inverses:
                assert_equal(o(num), n)
