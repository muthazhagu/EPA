class Row:
    """
    Represents a row object.
    A row object consists of EFSI code, FSN, State abbr, year of the data observation,
    followed by the pollutant concentration for multiple pollutants.
    """

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
        """
        :param value: Takes the pollutant concentration as an input string.
        :return: None.

        Method sets the value of a pollutant if it contains 'no data', or if the existing
        value is lesser than :param value.
        """
        if self._lead == 'no data':
            self._lead = value
        elif int(self._lead) < int(value):
            self._lead = value

    @property
    def co(self):
        return self._co

    @co.setter
    def co(self, value):
        if self._co == 'no data':
            self._co = value
        elif int(self._co) < int(value):
            self._co = value

    @property
    def nox(self):
        return self._nox

    @nox.setter
    def nox(self, value):
        if self._nox == 'no data':
            self._nox = value
        elif int(self._nox) < int(value):
            self._nox = value

    @property
    def pmpri(self):
        return self._pmpri

    @pmpri.setter
    def pmpri(self, value):
        if self._pmpri == 'no data':
            self._pmpri = value
        elif int(self._pmpri) < int(value):
            self._pmpri = value

    @property
    def so2(self):
        return self._so2

    @so2.setter
    def so2(self, value):
        if self._so2 == 'no data':
            self._so2 = value
        elif int(self._so2) < int(value):
            self._so2 = value

    @property
    def voc(self):
        return self._voc

    @voc.setter
    def voc(self, value):
        if self._voc == 'no data':
            self._voc = value
        elif int(self._voc) < int(value):
            self._voc = value

    def signature(self):
        return ','.join([self.efsi, self.fsn, self.state, self.year])

    def __str__(self):
        """
        :return: String representation of the Row object.
        Primarily used to write out the Row representation into a file.
        """
        return ','.join([self.efsi, self.fsn, self.state, self.year, self.lead, self.co, self.nox, self.pmpri, self.so2,
                         self.voc])

    def __eq__(self, other):
        return self.year == other.year and \
               self.state == other.state and \
               self.efsi == other.efsi and \
               self.fsn == other.fsn


