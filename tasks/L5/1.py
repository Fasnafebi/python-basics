# Pascal's Triangle 

class Solution:
    def generate(self, numRows: int):
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)

            
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)  

        return result

if __name__ == "__main__":
    numRows = int(input("Enter the number of rows: "))
    solution = Solution()
    triangle = solution.generate(numRows)

    print("\nPascal's Triangle:")
    for row in triangle:
        print(row)
