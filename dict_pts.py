points = {
    "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7,
    "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,
    "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21,
    "v":22, "w":23, "x":24, "y":25, "z":26
}

words = "Geschwindigkeitsbegrenzung"

def dict_pts(points, words):
    try:
        point = 0
        for char in words.lower():
            if char in points:
                point += points[char]
        return point
    except (AttributeError,TypeError,ValueError) as err:
        print(f"1. The variable words must be a string. \
              2. Value can not be 'None' \
              3. {err}")

def main():
    print(dict_pts(points,words))

if __name__ == "__main__":
    main()
