def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right 


if __name__ == "__main__":
    x = int(input("Enter a number: "))
    print("Square root (rounded down) is:", mySqrt(x))
