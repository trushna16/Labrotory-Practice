class NQueensBranchBound:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.board = [-1] * n
        self.col_available = [True] * n
        self.diagonal1_available = [True] * (2 * n - 1)
        self.diagonal2_available = [True] * (2 * n - 1)

    def solve(self):
        self.place_queen(0)
        return self.solutions

    def place_queen(self, row):
        if row == self.n:
            self.save_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.col_available[col] = False
                self.diagonal1_available[row + col] = False
                self.diagonal2_available[row - col + self.n - 1] = False
                self.place_queen(row + 1)

                self.board[row] = -1
                self.col_available[col] = True
                self.diagonal1_available[row + col] = True
                self.diagonal2_available[row - col + self.n - 1] = True

    def is_safe(self, row, col):
        return self.col_available[col] and \
               self.diagonal1_available[row + col] and \
               self.diagonal2_available[row - col + self.n - 1]

    def save_solution(self):
        self.solutions.append(self.board.copy())


def print_solution(solution):
    n = len(solution)
    for row in range(n):
        for col in range(n):
            if solution[row] == col:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()
    print()


# Example usage
n = int(input('Please Enter the size of the chessboard : '))  # Size of the chessboard
branch_bound_solver = NQueensBranchBound(n)
solutions = branch_bound_solver.solve()

print(f"Number of solutions (Branch and Bound): {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    print_solution(solution)
