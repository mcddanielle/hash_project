#!/usr/bin/env python3

"""
Danielle McDermott
July 24, 2019
will import the dumb_reader module, 
use it to read in Pa0, and then parse it all...
"""
import sys

import dumb_file_reader as dfr

################################################################
################################################################
################################################################

if __name__ == "__main__":

    #------------------------------------------------------------------------
    #get data for initial frame, 
    #------------------------------------------------------------------------
    inputfile = "Pa0"
    
    (Sx, Sy, radius, maxtime, writemovietime ) = dfr.get_input_data(inputfile)

    print(Sx, Sy, radius, maxtime, writemovietime)

    
