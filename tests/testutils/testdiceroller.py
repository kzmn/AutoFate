from django.test import TestCase
from utils.diceroller import DiceRoller

class TestDiceRoller(TestCase):

    def setUp(self):
        self.roller = DiceRoller()

    def test_roll_dice(self):
        """
        Tests that the dice roller works as intended.  Do to the random nature
        of dice rolls the tests are repeated 1000 times to make sure we have
        a decent set of test data.
        """
        for _ in range(1000):

            # test the simple case of rolling 4d6
            # TODO: If we update to 3.4 at some point, update to use subtests.
            # with self.subTest():
            results = self.roller.rolldice({6: 4})
            self.assertTrue(len(filter(lambda x: x <= 0, results)) == 0)
            self.assertTrue(len(filter(lambda x: x >= 6, results)) == 0)
            self.assertTrue(len(filter(lambda x: 0 < x <= 6, results)) == 4)

            # test more complicated case involving multiple types of dice
            # rolls 2d20 + 27d10 + 3d8 + 4d6
            results = self.roller.rolldice({6: 4, 8: 3, 10: 27, 20: 2})
            # no roll should be less than or equal to 0 regardless of dice type.
            self.assertTrue(self.assertTrue(len(filter(lambda x: x <= 0, results)) == 0))
            d6rolls = results[0:3]


