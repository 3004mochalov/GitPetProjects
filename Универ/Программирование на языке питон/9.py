class Mainly:
    def __init__(self):
        self.state = -1

    def check(self):
        if self.state == -1:
            self.state = 0
        elif self.state == 6:
            self.state = 7
        else:
            raise KeyError
        return self.state

    def rock(self):
        if self.state == -1:
            self.state = 3
        else:
            raise KeyError
        return self.state

    def paste(self):
        if self.state == -1:
            self.state = 1
        elif self.state == 1 or self.state == 7:
            self.state = 9
        elif self.state == 5:
            self.state = 6
        elif self.state == 6:
            self.state = 8
        else:
            raise KeyError
        return self.state

    def fetch(self):
        if self.state == -1:
            self.state = 2
        elif self.state == 0:
            self.state = 4
        elif self.state == 4 or self.state == 3 or self.state == 8:
            self.state = 5
        else:
            raise KeyError
        return self.state


def main():
    return Mainly()
