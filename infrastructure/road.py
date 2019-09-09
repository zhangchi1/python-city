def draw_road(length, orientation):
    """

    :param length: integer defining the length of the road
    :param orientation: string defining vertical or horizontal road
    :return:
    """
    if length <= 0:
        print("length is equal or less than 0")
        raise ValueError
    for i in range(length):
        if orientation == 'vertical':
            print("-", end="")
        elif orientation == 'horizontal':
            print("|")
        else:
            print("orientation is not valid")
            raise ValueError
    return
