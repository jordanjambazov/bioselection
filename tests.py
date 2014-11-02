import unittest

from athlete import Athlete


class AthleteTests(unittest.TestCase):
    def test_athlete_male(self):
        male = Athlete("male", birth_year=2000, birth_month=2,
                       weight=50, height=195)
        exam = male.examine(exam_year=2014, exam_month=10)
        self.assertEqual(exam.calendar_age, 176)
        self.assertAlmostEqual(exam.bio_age, 11.752, places=3)

    def test_athlete_female(self):
        male = Athlete("female", birth_year=2000, birth_month=2,
                       weight=50, height=165)
        exam = male.examine(exam_year=2014, exam_month=10)
        self.assertEqual(exam.calendar_age, 176)
        self.assertAlmostEqual(exam.bio_age, 73.43, places=2)

if __name__ == '__main__':
    unittest.main()