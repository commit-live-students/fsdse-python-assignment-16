from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint
        random_number = randint(0, 9)
        dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, random_number]}]}]}
        last_index_of_target = solution(dic)

        self.assertEqual(last_index_of_target, random_number)