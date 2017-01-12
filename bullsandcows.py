#!/usr/bin/env python

# github.com/zvolsky/bullsandcows

import random


def play():
    multi = lambda point, e=False: '' if point == 1 else (('e' if e else '') + 's')

    secret = str(10000 + random.randint(0,9999))[-4:]

    print '''
    Hi there!
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    Enter a number
    '''

    attempt_no = 0
    for attempt_no in xrange(999999999):
        attempt_no += 1
        attempt = raw_input('>>> ')
        if len(attempt) != 4 or not attempt.isdigit():
            print 'I need a 4 digit number.'
        else:
            bulls = cows = 0
            sec_cows = att_cows = ''
            for pos, creature in enumerate(secret):
                if creature == attempt[pos]:
                    bulls += 1
                else:
                    sec_cows += creature
                    att_cows += attempt[pos]
            if bulls == 4:
                print "Correct, you've guessed the right number in %s guess%s!" % (
                    attempt_no, multi(attempt_no, e=True))
                print "That's %s." % ('amazing', 'average', 'not so good')[min(2, int(attempt_no/7))]
                break
            sec_cows_list = list(sec_cows)
            for creature in att_cows:
                try:
                    sec_cows_list.remove(creature)
                    cows += 1
                except ValueError as exc:
                    pass
            print "%s bull%s, %s cow%s." % (bulls, multi(bulls), cows, multi(cows))


if __name__ == "__main__":
    play()
