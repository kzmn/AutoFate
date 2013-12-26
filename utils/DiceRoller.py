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

    def rolldice(self, dicedict):
        """
        Rolls a set of polyhedral dice and returns a list of the results
        :param self: the self parameter
        :param dicedict:  A diction of dice, the key is the number of
        sides to the die, the value is the number of dice of that type to roll.
        :rtype : (int)
        """
        random.seed()
        results = []
        for key in dicedict.keys():
            [results.append(random.randrange(1, key, 1)) for _ in
             range(dicedict[key])]
        return results

    def roll4dfudge(self):
        """
        Rolls 4 fudge dice and returns a list of the results.
        :rtype : (string)
        """
        return self.rollfudgedice(4)


    def rollfudgedice(self, count):
        """
        Rolls a given number of fudge dice.
        :param count: the number of dice to roll.
        """
        numericrolls = self.rolldice({6: count})
        return list(map(__convertd6todf__, numericrolls))
