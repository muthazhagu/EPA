class Row:
    def __init__(self):
        self.year = ''
        self.state = ''
        self.efsi = ''
        self.fsn = ''
        self._lead = 'no data'
        self._co = 'no data'
        self._nox = 'no data'
        self._pmpri = 'no data'
        self._so2 = 'no data'
        self._voc = 'no data'

    @property
    def lead(self):
        return self._lead

    @lead.setter
    def lead(self, value):
        if self._lead == 'no data':
            self._lead = value
        elif self._lead < value:
            self._lead = value
            
    @property
    def co(self):
        return self._co

    @co.setter
    def co(self, value):
        if self._co == 'no data':
            self._co = value
        elif self._co < value:
            self._co = value
            
    @property
    def nox(self):
        return self._nox

    @nox.setter
    def nox(self, value):
        if self._nox == 'no data':
            self._nox = value
        elif self._nox < value:
            self._nox = value
            
    @property
    def pmpri(self):
        return self._pmpri

    @pmpri.setter
    def pmpri(self, value):
        if self._pmpri == 'no data':
            self._pmpri = value
        elif self._pmpri < value:
            self._pmpri = value
            
    @property
    def so2(self):
        return self._so2

    @so2.setter
    def so2(self, value):
        if self._so2 == 'no data':
            self._so2 = value
        elif self._so2 < value:
            self._so2 = value
            
    @property
    def voc(self):
        return self._voc

    @voc.setter
    def voc(self, value):
        if self._voc == 'no data':
            self._voc = value
        elif self._voc < value:
            self._voc = value

    def signature(self):
        return ','.join([self.year, self.state, self.efsi, self.fsn])

    def __str__(self):
        return ','.join([self.year, self.state, self.efsi, self.fsn, self.lead, self.co, self.nox, self.pmpri, self.so2,
                         self.voc])

    def __eq__(self, other):
        return self.year == other.year and \
               self.state == other.state and \
               self.efsi == other.efsi and \
               self.fsn == other.fsn


