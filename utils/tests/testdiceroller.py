from django.test import TestCase
from utils.diceroller import DiceRoller
import random


def __is_valid_fate_roll__(roll):
    if roll == "+" or "-" or " ":
        return True
    else:
        return False


class TestDiceRoller(TestCase):
    """
    Test cases for the DiceRoller class.
    """

    def setUp(self):
        self.roller = DiceRoller()
        random.seed()

    def test_roll_dice(self):
        """
        Tests that the dice roller works as intended.  Do to the random nature
        of dice rolls the tests are repeated 100 times to make sure we have
        a decent set of test data.
        """
        for _ in range(100):
            # test the simple case of rolling 4d6
            # TODO: If we update to 3.4 at some point, update to use subtests.
            # with self.subTest():
            results = self.roller.roll_dice({6: 4})
            self.assertTrue(len(list(filter(lambda x: x <= 0, results))) == 0)
            self.assertTrue(len(list(filter(lambda x: x > 6, results))) == 0)
            self.assertTrue(
                len(list(filter(lambda x: 0 < x <= 6, results))) == 4)

            # test more complicated case involving multiple types of dice
            # rolls 2d20 + 27d10 + 3d8 + 4d6
            results = self.roller.roll_dice({6: 4, 8: 3, 10: 27, 20: 2})
            # no roll should be less than or equal to 0 regardless of dice type.
            self.assertTrue(len(list(filter(lambda x: x <= 0, results))) == 0)

            # set up the sub-lists for each die type.
            d6rolls = results[0:4]
            d8rolls = results[4:7]
            d10rolls = results[7:34]
            d20rolls = results[34:36]

            # test the d6 rolls
            self.assertTrue(len(list(filter(lambda x: x > 6, d6rolls))) == 0)
            self.assertTrue(
                len(list(filter(lambda x: 0 < x <= 6, d6rolls))) == 4)

            # test the d8 rolls
            self.assertTrue(len(list(filter(lambda x: x > 8, d8rolls))) == 0)
            self.assertTrue(
                len(list(filter(lambda x: 0 < x <= 8, d8rolls))) == 3)

            # test the d10 rolls
            self.assertTrue(len(list(filter(lambda x: x > 10, d10rolls))) == 0)
            self.assertTrue(
                len(list(filter(lambda x: 0 < x <= 10, d10rolls))) == 27)

            # test the d20 rolls
            self.assertTrue(len(list(filter(lambda x: x > 20, d20rolls))) == 0)
            self.assertTrue(
                len(list(filter(lambda x: 0 < x <= 20, d20rolls))) == 2)


    def test_roll_fudge_dice(self):
        """
        Tests that the dice roller handles the rolling of an arbitrary number
        of fudge dice correctly.
        """
        # TODO: look into passing in specific results from the roll_dice method
        # to test that the fudge dice method is translating to fudge properly
        # (will likely require some kind of method stubbing if python supports
        # that.
        for _ in range(100):
            numdice = random.randint(1, 50)
            results = self.roller.roll_fudge_dice(numdice)
            self.assertTrue(
                len(list(filter(__is_valid_fate_roll__, results))) == numdice)


    def test_roll_4dfudge(self):
        """
        Tests that the dice roller rolls 4dfudge correctly
        """
        for _ in range(100):
            results = self.roller.roll_4dfudge()
            self.assertTrue(
                len(list(filter(__is_valid_fate_roll__, results))) == 4)



