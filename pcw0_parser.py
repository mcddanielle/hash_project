#!/usr/bin/env python3

"""
Danielle McDermott
July 24, 2019
will import the dumb_reader module, 
use it to read in pcw0, and then parse it all... 
"""


#to work with files, call sys.exit(), etc
import sys

import dumb_file_reader as dfr
################################################################
################################################################
################################################################

if __name__ == "__main__":

    #name of parameter file, this varies by simulation (Pa0, Pcw0, etc)
    inputfile = "Pcw0"
    

    #get the data from Pcw0 - hardwired for a certain format
    #this could be improved
    parameters_MD = dfr.get_input_data(inputfile)
    Sx=parameters_MD[0]
    Sy=parameters_MD[1]
    radius=parameters_MD[2]
    maxtime=parameters_MD[3]
    writemovietime=parameters_MD[4]
    drop=parameters_MD[5]
    dt=parameters_MD[6]
    

    print(parameters_MD)

    sys.exit()

    #####################################################################

