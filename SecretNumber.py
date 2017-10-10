#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = int(13)

guess = int(raw_input("Ugani skrito število med 1 in 20:"))

if secret == guess:
    print "Čestitam, pravilno ste uganili skrito število! Nagrado dobite pri izhodu."
else:
    print "Žal niste uganili skrite številke, poskusite ponovno."
