def draw_road(length):
    if length <= 0:
        print("length is less than 0")
        raise ValueError
    for i in range(length):
        print("-", end="")
    return
