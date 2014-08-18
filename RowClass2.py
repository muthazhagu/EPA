class Row:
    """
    Alternate implementation of the Row class.
    This is not used in the program.
    """
    def __init__(self):
        self.year = ''
        self.state = ''
        self.efsi = ''
        self.fsn = ''
        self.lead = []
        self.co = []
        self.nox = []
        self.pmpri = []
        self.so2 = []
        self.voc = []

    def longestlist(self):
        length = [len(item) for item in [self.lead, self.co, self.nox, self.pmpri, self.so2, self.voc]]
        return max(length)

    def popper(self):
        poppeditems = [item.pop(0) if item else '' for item in
                       [self.lead, self.co, self.nox, self.pmpri, self.so2, self.voc]]
        return poppeditems

    def __str__(self):
        string = ''
        for i in range(self.longestlist()):
            string += self.year + ',' + self.state + ',' + self.efsi + ',' + self.fsn + ',' + ','.join(
                self.popper()) + '\n'
        return string

    def __eq__(self, other):
        return self.year == other.year and \
               self.state == other.state and \
               self.efsi == other.efsi and \
               self.fsn == other.fsn
