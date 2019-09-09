
def draw_firestation(size =10):
    """

    :param length: integer defining the size of the fire station
    :return:
    """
    if size <= 0:
        print("length is equal or less than 0")
        raise ValueError
    print("=" * size)
    print("=" * size)
    print("fire station")
    print("=" * size)
    return

draw_firestation(20)