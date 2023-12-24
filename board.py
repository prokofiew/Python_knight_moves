from field import Field


class Board:
    def __init__(self):
        self.height = None
        self.width = None
        self.board = []
        self.field = Field()
        self.set_board_size()

    def set_board_size(self):
        board_size = input("Enter board height and width (4x4): ")
        dimensions_list = board_size.split('x')

        self.height = int(dimensions_list[0])
        self.width = int(dimensions_list[1])
        self.board = [[self.field for _ in range(self.width)] for _ in range(self.height)]

        return self.height, self.width

    def __str__(self):
        return '\n'.join([' '.join(str(field.value) for field in row) for row in self.board])
