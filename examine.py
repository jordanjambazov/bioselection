import math


class Examine:
    def __init__(self, athlete, exam_year, exam_month):
        self._athlete = athlete
        self._exam_year = exam_year
        self._exam_month = exam_month
        self._coefficients = self._prepare_coefficients()

    def _prepare_coefficients(self):
        """
        Some magic numbers from the specification.
        :return:
        """
        s1 = self._athlete.weight * 10
        if self._athlete.sex == "male":
            s2 = self._athlete.height - (196 * math.log10(s1) - 2) + 66
            s3 = self._athlete.weight - (0.23 * s1 - 21)
            s4 = (1.75 * s2) - (7 * s3) + s1
            s5 = 0.62 * s4 - 24.6
        else:
            s2 = self._athlete.height - (163.6 * math.log10(s1) - 2) + 77.4
            s3 = self._athlete.weight - (0.22 * s1 - 19)
            s4 = (1.75 * s2) - (7 * s3) + s1
            s5 = 0.62 * s4 - 24.6
        return {
            's1': s1,
            's2': s2,
            's3': s3,
            's4': s4,
            's5': s5,
        }

    @property
    def bio_age(self):
        return self._coefficients.get('s5') - self.calendar_age

    @property
    def calendar_age(self):
        year_months = (self._exam_year - self._athlete.birth_year) * 12
        return self._exam_month - self._athlete.birth_month + year_months