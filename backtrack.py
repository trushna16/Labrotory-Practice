class NQueensBacktracking:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.board = [-1] * n

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
                self.place_queen(row + 1)
                self.board[row] = -1

    def is_safe(self, row, col):
        for r in range(row):
            if self.board[r] == col or \
                    self.board[r] - r == col - row or \
                    self.board[r] + r == col + row:
                    return False
        return True

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
    
backtrack_solver = NQueensBacktracking(n)
backtrack_solutions = backtrack_solver.solve()

print(f"Number of solutions (Backtracking): {len(backtrack_solutions)}")
for i, solution in enumerate(backtrack_solutions):
    print(f"Solution {i + 1}:")
    print_solution(solution)