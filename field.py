class Field:
    def __init__(self):
        self.value = 0
        self.is_taken = False

    def check_if_taken(self):
        return self.is_taken

    def occupy_field(self):
        self.is_taken = True
        self.value = 1
        return self.value
