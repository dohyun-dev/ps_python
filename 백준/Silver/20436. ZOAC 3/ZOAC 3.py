def calc(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

keyboard_left = {
    "q": (0, 0), "w": (0, 1), "e": (0, 2), "r": (0, 3), "t": (0, 4),
    "a": (1, 0), "s": (1, 1), "d": (1, 2), "f": (1, 3), "g": (1, 4),
    "z": (2, 0), "x": (2, 1), "c": (2, 2), "v": (2, 3)
}
keyboard_right = {
    "y": (0, 5), "u": (0, 6), "i": (0, 7), "o": (0, 8), "p": (0, 9),
    "h": (1, 5), "j": (1, 6), "k": (1, 7), "l": (1, 8),
    "b": (2, 4), "n": (2, 5), "m": (2, 6)
}

l, r = map(lambda x: keyboard_left[x] if x in keyboard_left else keyboard_right[x], input().split())
answer = 0

for c in input():
    if c in keyboard_left:
        x, y = keyboard_left[c]
        time = calc(l[0], l[1], x, y)
        l = (x, y)
    else:
        x, y = keyboard_right[c]
        time = calc(r[0], r[1], x, y)
        r = (x, y)
    answer += time + 1
print(answer)