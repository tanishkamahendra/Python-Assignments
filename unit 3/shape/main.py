import shapes

def main():
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        area = shapes.circle_area(radius)
        print("Area of circle:", round(area, 2))

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = shapes.rectangle_area(length, width)
        print("Area of rectangle:", round(area, 2))

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = shapes.triangle_area(base, height)
        print("Area of triangle:", round(area, 2))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()