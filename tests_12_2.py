import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner('Усэйн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)
        self.distans = 90

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    def test_1(self):
        tourn_1 = Tournament(self.distans, self.run_1, self.run_3)
        result = tourn_1.start()
        self.all_results['test_1'] = result

    def test_2(self):
        tourn_2 = Tournament(self.distans, self.run_2, self.run_3)
        result = tourn_2.start()
        self.all_results['test_2'] = result

    def test_3(self):
        tourn_3 = Tournament(self.distans, self.run_1, self.run_2, self.run_3)
        result = tourn_3.start()
        self.all_results['test_3'] = result

#Дополнительно.

    def test_4(self):
        tourn_4 = Tournament(5, self.run_1, self.run_2, self.run_3)
        result = tourn_4.start()
        self.all_results['test_4'] = result


if __name__ == '__main__':
  unittest.main()

