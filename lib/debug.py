#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    yosemite = NationalPark("Yosemite")
    matteo = Visitor("Matteo")
    bruno = Visitor("Bruno")
    trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
    trip_2 = Trip(matteo, yosemite, "May 20th", "May 27th")
    trip3 = Trip(bruno, yosemite, "October 20th", "September 1st")

    # print(matteo.trips())
    # print(matteo.national_parks())
    yosemite.best_visitor()
    NationalPark.most_visited()


    ipdb.set_trace()
