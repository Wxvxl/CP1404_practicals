COLORS = {
    "Absolute Zero": "#0048ba",
    "International Orange": "#ff4f00",
    "Alizarin Crimson": "#e32636",
    "Amethyst": "#9966cc",
    "Battleship Gray": "#848482",
    "Black Coffee": "#3b2f2f",
    "Blue Bell": "#a2a2d0",
    "Brick Red": "#cb4154",
    "Persian Rose": "#fe28a2",
    "Iris": "#5a4fcf"
}

color_code = input("Enter color name: ").title()
while color_code != "":
    if color_code in COLORS:
        print(color_code, "is", COLORS[color_code])
    else:
        print("Invalid color name")
    color_code = input("Enter color name: ").title()
