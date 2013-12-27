import random


def __convertd6todf__(d6roll):
    """
    Converts the numeric value of a d6 roll into the "-" " " or "+"
    values on fudge dice
    :param d6roll:
    """
    if d6roll == 1 or d6roll == 2:
        return "-"
    elif d6roll == 3 or d6roll == 4:
        return " "
    elif d6roll == 5 or d6roll == 6:
        return "+"
    else:
        return None


class DiceRoller():
    """
    A simple dice roller that is capable of rolling both polyhedral as well
    as fudge dice.
    """

    def roll_dice(self, dicedict):
        """
        Rolls a set of polyhedral dice and returns a list of the results.  The
        results list will return with the results of lower sided dice at the
        beginning of the list and the results of higer sided dice at the end
        of the list.

        For example, if we roll {8: 3, 20: 2, 6: 4, 10: 5} the
        results list would look like: (d6, d6, d6, d6, d8, d8, d8, d10, d10,
        d10, d10, d10, d20, d20)

        :param self: the self parameter
        :param dicedict:  A diction of dice, the key is the number of
        sides to the die, the value is the number of dice of that type to roll.
        :rtype : (int)
        """
        random.seed()
        results = []
        # Roll each die indicated by the dice dict and put the result of the
        # roll into the results list.  We are sorting the keys of the dice
        # dictionary in order to ensure a predictable output for dice rolls
        # as python dictionaries have random order regardless of what order
        # keys were entered in.
        for key in sorted(dicedict.keys()):
            [results.append(random.randrange(1, key, 1)) for _ in
             range(dicedict[key])]
        return results

    def roll_4dfudge(self):
        """
        Rolls 4 fudge dice and returns a list of the results.
        :rtype : (string)
        """
        return self.roll_fudge_dice(4)


    def roll_fudge_dice(self, count):
        """
        Rolls a given number of fudge dice.
        :param count: the number of dice to roll.
        """
        numericrolls = self.roll_dice({6: count})
        return list(map(__convertd6todf__, numericrolls))
