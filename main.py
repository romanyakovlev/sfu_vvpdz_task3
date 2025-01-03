
def get_colors(color: str, percent: int) -> tuple[int, int, int]:
    if color[0] != '#' or len(color) != 7:
        raise ValueError('Color must be in hex format')
    if percent < 0 or percent > 100:
        raise ValueError('Percent must be between 0 and 100')
    rr, gg, bb = color[1:3], color[3:5], color[5:7]
    rr, gg, bb = int(rr, 16), int(gg, 16), int(bb, 16)
    if any(x < 0 or x > 255 for x in (rr, gg, bb)):
        raise ValueError('Color must be in hex format')
    return rr, gg, bb


def darken(color: str, percent: int) -> str:
    rr, gg, bb = get_colors(color, percent)
    rr += int((255 - rr) * (percent / 100))
    gg += int((255 - gg) * (percent / 100))
    bb += int((255 - bb) * (percent / 100))
    return f'#{rr:02X}{gg:02X}{bb:02X}'


def lighten(color: str, percent: int) -> str:
    rr, gg, bb = get_colors(color, percent)
    rr -= int(rr * (percent / 100))
    gg -= int(gg * (percent / 100))
    bb -= int(bb * (percent / 100))
    return f'#{rr:02X}{gg:02X}{bb:02X}'


def main():
    print("Примеры для darken")
    print(f"Пример для darken('#000000', 100):  {darken('#000000', 100)}")
    print(f"Пример для darken('#000000', 0):    {darken('#000000', 0)}")
    print(f"Пример для darken('#000000', 50):   {darken('#000000', 50)}")
    print(f"Пример для darken('#FFFFFF', 50):   {darken('#FFFFFF', 50)}")
    print(f"Пример для darken('#FF5733', 20):   {darken('#FF5733', 20)}")
    print(f"Пример для darken('#3498DB', 10):   {darken('#3498DB', 10)}")
    print(f"Пример для darken('#2ECC71', 75):   {darken('#2ECC71', 75)}")
    print(f"Пример для darken('#9B59B6', 40):   {darken('#9B59B6', 40)}")
    print("Примеры для lighten")
    print(f"Пример для lighten('#FFFFFF', 100): {lighten('#FFFFFF', 100)}")
    print(f"Пример для lighten('#FFFFFF', 50):  {lighten('#FFFFFF', 50)}")
    print(f"Пример для lighten('#FFFFFF', 0):   {lighten('#FFFFFF', 0)}")
    print(f"Пример для lighten('#000000', 100): {lighten('#000000', 100)}")
    print(f"Пример для lighten('#FF5733', 20):  {lighten('#FF5733', 20)}")
    print(f"Пример для lighten('#3498DB', 10):  {lighten('#3498DB', 10)}")
    print(f"Пример для lighten('#2ECC71', 75):  {lighten('#2ECC71', 75)}")
    print(f"Пример для lighten('#9B59B6', 40):  {lighten('#9B59B6', 40)}")


if __name__ == "__main__":
    main()
