import random


class DiceRoller():


    @staticmethod
    def rolldice(dicedict):
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
            print(key)
            [results.append(random.randrange(1, key, 1)) for _ in
             range(dicedict[key])]
        return results






