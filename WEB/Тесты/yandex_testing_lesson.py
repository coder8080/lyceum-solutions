class Rectangle:
    def __init__(self, w, h):
        if type(w) != int or type(h) != int:
            raise TypeError()
        if w < 0 or h < 0:
            raise ValueError()
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return self.w + self.w + self.h + self.h
