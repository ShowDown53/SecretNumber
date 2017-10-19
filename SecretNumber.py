#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():
    secret = random.randint(1, 20)

    while True:
        guess = int(raw_input("Ugani skrito število med 1 in 20: "))

        if secret == guess:
            print "Čestitam, '%s' je skrito število! Nagrado dobite pri izhodu." % secret
            break
        else:
            print "Žal %s ni skrito število, poskusite ponovno." % guess

if __name__ == "__main__":
    main()