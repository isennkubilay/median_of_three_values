def alternateMedian(a,b,c):
    return a + b + c - min(a,b,c) - max(a,b,c)
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))
    print(f"The median value is: {alternateMedian(x,y,z)} ")
main()