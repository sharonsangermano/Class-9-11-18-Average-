def main():
    sum3 = add_three(2, 3, 4)
    ave = divide_three(sum3, 3)
    print('This is the average of the three numbers: {}'.format(ave))


def add_three(v1, v2, v3):
    """
    :param v1: number one
    :param v2: number two
    :param v3: number three
    :returns: sum of 3
    """

    sum_of_three = v1 + v2 + v3
    return sum_of_three


def divide_three(v1, v2):
    """
    :param v1: sum of numbers
    :param v2: number of numbers
    :returns: division
    """
    div = v1/v2
    return div

if __name__ == "__main__":
    main()
