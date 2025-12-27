# =========================
# N-Queens Problem (Using Arrays)
# =========================

def nQueen(n):
    # Time: O(1) , Space: O(1)

    cols = [0] * n
    # cols[c] = 1 if column c is occupied
    # Time: O(n) , Space: O(n)

    ld = [0] * (2 * n)
    # left diagonal (row - col + n - 1)
    # Time: O(n) , Space: O(n)

    rd = [0] * (2 * n)
    # right diagonal (row + col)
    # Time: O(n) , Space: O(n)

    res = []
    # Time: O(1) , Space: O(1)

    def backtrack(r, cur):
        # Time: depends on recursion tree
        # Space: recursion stack O(n)

        # Base case: all queens are placed
        if r == n:
            res.append(cur[:])
            # Time: O(n)
            # Space: O(n)
            return

        for c in range(n):
            # Try placing queen in each column
            # Time: O(n) , Space: O(1)

            # Check column and diagonals
            if cols[c] or rd[r + c] or ld[r - c + n - 1]:
                # Time: O(1) , Space: O(1)
                continue

            # Choose
            cols[c] = 1
            rd[r + c] = 1
            ld[r - c + n - 1] = 1
            # Time: O(1) , Space: O(1)

            # Explore
            backtrack(r + 1, cur + [c + 1])
            # Time:
                # Number of valid permutations ≈ O(n!)
                # For each level, up to n choices are tried
                # Total Time = O(n! * n)
            # Space:
                # Recursion depth = O(n)
                # Path copy = O(n)

            # Un-choose (Backtracking)
            cols[c] = 0
            rd[r + c] = 0
            ld[r - c + n - 1] = 0
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
    for a in nQueen(4):
        print(*a)


# =========================
# Overall Complexity
# =========================
# Time Complexity  : O(n! * n)
# Space Complexity : O(n)
