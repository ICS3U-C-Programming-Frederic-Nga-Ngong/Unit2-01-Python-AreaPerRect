#!/usr/bin/env python3
# Created By: Frederic
# Date: Feb 2008 18
# Calculates the area of rectangle, perimeter of rectangle and displays the output
def main():
    # get the length
    length = int(input("Enter the length of rectangle (cm) ="))
    # get the width
    width = int(input("Enter the width o rectangle (cm) ="))
    # calculates the area
    Area = length * width
    # shows the output to user
    print("The area of the rectangle is:{} cm²".format(Area))
    # calculates the perimeter of rectangle
    perimeter = 2 * (length + width)
    # displays the output
    print("the perimeter of the rectangle is:{}cm".format(perimeter))


if __name__ == "__main__":

    main()
