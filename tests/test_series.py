from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci():
    expected = 3
    input = 4
    actual = fibonacci(input)
    assert actual == expected

def test_lucas():
    expected = 29
    input = 7
    actual = lucas(input)
    assert actual == expected

def test_sum_series_fibonacci():
    expected = 13
    input = 7
    actual = sum_series(input)
    assert actual == expected

def test_sum_series_lucas():
    expected = 7
    input = 4
    actual = sum_series(input,2,1)
    assert actual == expected

def test_sum_series_other():
    expected = 44
    input = 5
    actual = sum_series(input,3,7) # {0:3, 1:7, 2:10, 3:17, 4:27, 5:44, 6:71, 7:115, 8:186}
    assert actual == expected

def test():
    expected = {
        'fibonacci-4':3,
        'fibonacci-6':8,
        'fibonacci-8':21,
        'lucas-4':7,
        'lucas-6':18,
        'lucas-8':47,
        'series_fibonacci-4':3,
        'series_fibonacci-6':8,
        'series_fibonacci-8':21,
        'series_lucas-4':7,
        'series_lucas-6':18,
        'series_lucas-8':47,
        'series_other-4':27,
        'series_other-6':71,
        'series_other-8':186,
    }
    actual = {}
    number = 4
    for i in range(15):
        if i <= 2:
            actual[f"fibonacci-{number}"] = fibonacci(number)
        elif i <= 5:
            actual[f"lucas-{number}"] = lucas(number)
        elif i <= 8:
            actual[f"series_fibonacci-{number}"] = sum_series(number)
        elif i <= 11:
            actual[f"series_lucas-{number}"] = sum_series(number,2,1)
        else:
            actual[f"series_other-{number}"] = sum_series(number,3,7)
        if number == 8:
            number = 4
        else:
            number += 2
    assert actual == expected