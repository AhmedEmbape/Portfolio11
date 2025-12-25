# =========================
# N-Queens Problem
# =========================

def nQueen(n):
    # Time: O(1) , Space: O(1)

    res = []  
    # Time: O(1) , Space: O(1)

    cols, d1, d2 = set(), set(), set()
    # cols  -> columns
    # d1    -> main diagonal (row - col)
    # d2    -> secondary diagonal (row + col)
    # Time: O(1) , Space: O(n)

    def backtrack(r, path):
        # Time: depends on recursion tree
        # Space: recursion stack O(n)

        # Base case: all queens are placed
        if r == n:
            res.append([c + 1 for c in path])
            # Time: O(n)
            # Space: O(n)
            return

        for c in range(n):
            # Try each column
            # Time: O(n) , Space: O(1)

            # Check column and diagonals
            if c in cols or r - c in d1 or r + c in d2:
                # Time: O(1) , Space: O(1)
                continue

            # Choose
            cols.add(c)      
            d1.add(r - c)    
            d2.add(r + c)    
            # Time: O(1) , Space: O(1)

            # Explore
            backtrack(r + 1, path + [c])
            # Time:
                # Number of valid permutations ≈ O(n!)
                # Each recursive call tries up to n choices
                # Total Time = O(n! * n)
            # Space:
                # Recursion depth = O(n)
                # Path copy = O(n)

            # Un-choose (Backtracking)
            cols.remove(c)   
            d1.remove(r - c)
            d2.remove(r + c)
            # Time: O(1) , Space: O(1)

    backtrack(0, [])
    # Time: O(n! * n)
    # Space: O(n)

    return res
    # Time: O(1) , Space: O(1)


# =========================
# Test Case
# =========================

if __name__ == "__main__":
    for ans in nQueen(4):
        print(*ans)

# =========================
# Overall Complexity
# =========================
# Time Complexity  : O(n! * n)
# Space Complexity : O(n)
