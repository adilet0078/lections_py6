def distance_squared(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def classify_triangle(x1, y1, x2, y2, x3, y3):
    d12 = distance_squared(x1, y1, x2, y2)
    d13 = distance_squared(x1, y1, x3, y3)
    d23 = distance_squared(x2, y2, x3, y3)

    sides = [d12, d13, d23]
    sides.sort()

    if sides[0] + sides[1] == sides[2]:
        return "R"
    elif sides[0] + sides[1] > sides[2]:
        if sides[0] == sides[1] == sides[2]:
            return "E"
        elif sides[0] + sides[1] > sides[2]:
            return "A"
        else:
            return "O"
    else:
        return "L"

# Example usage:
x1, y1, x2, y2, x3, y3 = map(int, input().split())
result = classify_triangle(x1, y1, x2, y2, x3, y3)
print(result)