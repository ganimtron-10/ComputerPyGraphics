def bresenham_circle_algo(cg, r, xc=None, yc=None, show_step=False):
    """Creating a Circle using Bresenhams Circle Drawing Algorithm"""

    if xc == None or yc == None:
        xc = cg.width // 2
        yc = cg.height // 2

    x = 0
    y = r
    d = 3 - (2 * r)

    while x <= y:
        cg.putpixel(x + xc, y + yc)
        cg.putpixel(-x + xc, y + yc)
        cg.putpixel(x + xc, -y + yc)
        cg.putpixel(-x + xc, -y + yc)
        cg.putpixel(y + yc, x + xc)
        cg.putpixel(-y + yc, x + xc)
        cg.putpixel(y + yc, -x + xc)
        cg.putpixel(-y + yc, -x + xc)
        if d < 0:
            d = d + 4 * x + 6
            x += 1
        else:
            d = d + 4 * x - 4 * y + 10
            x += 1
            y -= 1

        if show_step:
            cg.run()

    if not show_step:
        cg.show()


if __name__ == "__main__":
    cg = CG(25, 25, ".")
    r = int(input("Enter the value of r: "))
    bresenham_circle_algo(r, show_step=True)
