class PrintBox(object):
    def __init__(self, length, s1 = '', s2 = '', s3 = '', s4 = '', s5 = ''):
        self.length = length
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
    
    def add_box(self, person):
        if person is not None:
            self.s1 += " " + "_" * int(self.length - 2) + " "
            self.s2 += "| " + person.last + ", " + person.first + " " * (self.length - 5 - len(person.last) - len(person.first)) + "|"
            self.s3 += "|   Born: " + person.birth + " " * (self.length - 16) + " |"
            self.s4 += "|   Died: " + person.death + " " * (self.length - 16) + " |"
            self.s5 += "'" + "-" * (self.length - 2) + "'"
        else:
            self.s1 += " " * self.length
            self.s2 += " " * self.length
            self.s3 += " " * self.length
            self.s4 += " " * self.length
            self.s5 += " " * self.length