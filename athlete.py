from examine import Examine


class Athlete:
    def __init__(self, sex, birth_year, birth_month, weight, height):
        self._sex = sex
        self._birth_year = birth_year
        self._birth_month = birth_month
        self._weight = weight
        self._height = height

    @property
    def birth_month(self):
        return self._birth_month

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def sex(self):
        return self._sex

    def examine(self, exam_year, exam_month):
        return Examine(self, exam_year, exam_month)