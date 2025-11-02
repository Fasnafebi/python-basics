def lengthOfLastWord(s: str) -> int:
    s = s.strip()  
    words = s.split() 
    return len(words[-1]) 
if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Length of the last word is:", lengthOfLastWord(s))
