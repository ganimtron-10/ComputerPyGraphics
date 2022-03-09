def bresenham_line_algo(cg, x1, y1, x2, y2, show_step=False):
    """Creating a line using Bresenhams Line Drawing Algorithm"""

    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx

    xi = x1
    yi = y1

    while xi != x2 and yi != y2:
        cg.putpixel(xi, yi)
        if d < 0:
            d = d + 2 * dy
            xi += 1
        else:
            d = d + 2 * dy - 2 * dx
            xi += 1
            yi += 1

        if show_step:
            cg.run()

    if not show_step:
        cg.show()


if __name__ == "__main__":
    cg = CG(20, 20, " ")
    x1 = int(input("Enter the value of x1: "))
    y1 = int(input("Enter the value of y1: "))
    x2 = int(input("Enter the value of x2: "))
    y2 = int(input("Enter the value of y2: "))

    bresenham_line_algo(x1, y1, x2, y2, True)
