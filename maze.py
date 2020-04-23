class Maze:

    def __init__(self, grid, start_position, end_position):
        self.grid = grid
        self.border_x = len(grid[0])
        self.border_y = len(grid)
        self.start_position = start_position
        self.end_position = end_position

    @classmethod
    def from_template(cls, str_grid, start_pos, end_pos):
        cells_corr = {
            '#': Wall,
            ' ': Ground,
            'X': Path
        }

        grid = [[cells_corr[x](col_ix, row_ix) for col_ix, x in enumerate(row)] for row_ix, row in enumerate(str_grid)]
        return cls(grid, start_pos, end_pos)

    def str_render_with_pos(self, *positions, char):
        for yix, row in enumerate(self.grid):
            for xix, value in enumerate(row):
                if (yix, xix) in positions:
                    value = char
                print(value, end=' ')
            print('')


class Challenger:

    def __init__(self):
        self.pos = None
        self.maze = None
        self.visited = []
        self.good_path = []

    def solve_maze(self, maze):
        self.pos = maze.start_position
        self.maze = maze
        self.get_next_paths()
        win = self.run_box()
        if win:
            print('Welcome to the Maze !')
            print('')
            self.maze.str_render_with_pos(*self.good_path, char='X')
            print('')
            print("You Won !")
        else:
            print("This maze is impossible")

    def run_box(self):
        current = self.pos
        if self.check_win():
            self.good_path.append(current)
            return True
        self.visited.append(self.pos)
        neighbors = self.get_next_paths()
        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.go_to(neighbor)
                if self.run_box():
                    self.good_path.append(current)
                    return True
        return False

    def go_to(self, new):
        self.pos = new

    def check_win(self):
        return self.pos == self.maze.end_position

    def get_next_paths(self):
        open_neighbors = []
        y = self.pos[0]
        x = self.pos[1]
        neighbors_pos = [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]
        for yix, xix in neighbors_pos:
            if 0 <= yix <= maze.border_y and 0 <= xix <= maze.border_x:
                if self.maze.grid[yix][xix] != '#':
                    open_neighbors.append((yix, xix))
        return open_neighbors


grid1 = [
    ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    [' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#'],
    ['#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#'],
]

start = (5, 0)
end = (1, 9)
maze = Maze(grid1, start_position=start, end_position=end)
challenger = Challenger()
challenger.solve_maze(maze)
