from decimal import Decimal


class ViolationRecord:
    """
    This class encapsulates the recommendation data.
    """
    def __init__(self):
        self.year = ''
        self.state = ''
        self.efsi = ''
        self.fsn = ''
        self.lead_latest, self.lead_mean = 'no data', 'no data'
        self.co_latest, self.co_mean = 'no data', 'no data'
        self.nox_latest, self.nox_mean = 'no data', 'no data'
        self.pmpri_latest, self.pmpri_mean = 'no data', 'no data'
        self.so2_latest, self.so2_mean = 'no data', 'no data'
        self.voc_latest, self.voc_mean = 'no data', 'no data'
        self.in_violation = 'N'

    def update_in_violation(self):
        """
        This method does not return anything.

        It compares the data from the latest year, to the mean of the data from the previous years,
        and sets the in_violation property to Y, if in violation (i.e. needs recommendation).

        It sets the in_violation property to Y, if and only if ALL of the following conditions are satisfied -
        1. Latest year's data is not the same as the mean of the previous years' data.
        2. Latest year's data is not 'no data'
        3. Mean is not 'no data'
        4. Latest year's data is greater than the mean of the previous years' data.
        """
        latest = [self.lead_latest, self.co_latest, self.nox_latest, self.pmpri_latest, self.so2_latest, self.voc_latest]
        mean = [self.lead_mean, self.co_mean, self.nox_mean, self.pmpri_mean, self.so2_mean, self.voc_mean]
        latest_and_mean = list(zip(latest, mean))

        for tup in latest_and_mean:
            if not tup[0] == tup[1]:
                if not tup[0] == 'no data':
                    val1 = Decimal(tup[0])
                    if not tup[1] == 'no data':
                        val2 = Decimal(tup[1])
                        if val1 and val2:
                            if val1 > val2:
                                self.in_violation = 'Y'

    def __str__(self):
        return ','.join([self.efsi, self.fsn, self.state, self.year, self.lead_latest, self.lead_mean,
                         self.co_latest, self.co_mean, self.nox_latest, self.nox_mean,
                         self.pmpri_latest, self.pmpri_mean, self.so2_latest, self.so2_mean,
                         self.voc_latest, self.voc_mean, self.in_violation])