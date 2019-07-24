#!/usr/bin/env python3

"""
Danielle McDermott
July 24, 2019
NOT portable code for reading parameter files in the McDermott lab

To Do:
rewrite the code so you read the values into a hash, 
eliminating the need to rewrite everything when you change the parameter file
"""

import csv, sys
#####################################################
#simple ascii text reader
#####################################################
def import_text(filename, separator):
    '''Simple csv file reader, reads line by line, ignores comments of '#' type

    file_name = absolute name
    separator = ' ', '\t', etc
    '''
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            if line[0].startswith("#"):
                continue #print("")
            elif line:
                #print line
                yield line
    return

################################################################
#get and parse information that allows us to make the movie
#this is hardcoded, which is ugly
#want these variables to be globals to work with the animation subroutine
def get_input_data(filename):
    '''
    hardcoded to look for two particular types of files
    will exit if it does not get those types

    filename: Pa0, Pcw0 (or Pd0 if you want to go back to 2012)
    '''

    if filename == "Pa0" or "Pcw0":

        print("Reading parameters from: %s"%(filename))

        try:
            #data is traditionally placed in a two column file
            #with a string/number format, where number is integer or float

            #make an empty list to hold data as strings
            input_data_strings = []
            for data in import_text(filename,' '):
                #print(data)
                input_data_strings.append(data)
                
        except:
            print("File read error")
            sys.exit()

        
    else:
        print("Code is not written to understand your input file")
        print("Either hardcode your parameters or write a new subroutine")
        sys.exit()
        
    if filename == "Pa0":

        density          = float(input_data_strings[0][1])
        #small_density    = float(input_data_strings[1][1])
        #large_density    = float(input_data_strings[2][1])
        pdensity         = float(input_data_strings[1][1])
        
        Sx               = [0.0,float(input_data_strings[2][1])]
        Sy               = [0.0,float(input_data_strings[3][1])]
        
        radius           = float(input_data_strings[4][1])
        #large_radius     = float(input_data_strings[7][1])
        runtime          = int(  input_data_strings[5][1])
        runforce         = float(input_data_strings[6][1])
        dt               = float(input_data_strings[7][1])
        
        maxtime          = int(input_data_strings[8][1])
        writemovietime   = int(input_data_strings[9][1])
        
        kspring          = float(input_data_strings[10][1])
        lookupcellsize   = float(input_data_strings[11][1])
        potentialrad     = float(input_data_strings[12][1])
        potentialmag     = float(input_data_strings[13][1])
        lengthscale      = float(input_data_strings[14][1])
        drivemag         = float(input_data_strings[15][1])
        drivefrq         = float(input_data_strings[16][1])
        decifactor       = int(  input_data_strings[17][1])
        restart          = int(  input_data_strings[18][1])
        drive_step_time  = int(  input_data_strings[19][1]) 
        drive_step_force = float(input_data_strings[20][1])


        return(Sx, Sy, radius, maxtime, writemovietime )

    elif filename == "Pcw0":
        id_str       = str(input_data_strings[0][1])
        Sx           = [0.0,float(input_data_strings[1][1])]
        Sy           = [0.0,float(input_data_strings[2][1])]
        
        nV           = int(  input_data_strings[3][1])
        f_p          = float(input_data_strings[4][1])
        tot_trough   = int(  input_data_strings[5][1])
        drop         = int(  input_data_strings[6][1])
        dc_current   = float(input_data_strings[7][1])
        dc_curr_incr = float(input_data_strings[8][1])
        dc_maxcurr   = float(input_data_strings[9][1])
        
        Temperature  = float(input_data_strings[10][1])
        temp_incr    = float(input_data_strings[11][1])
        maxtemper    = float(input_data_strings[12][1])
        tot_time     = int(  input_data_strings[13][1])
        restart      = int(  input_data_strings[14][1])
        A_v          = float(input_data_strings[15][1])
        decifactor   = int(  input_data_strings[16][1])
        writemovie   = int(  input_data_strings[17][1])
        bstrength    = float(input_data_strings[18][1])
        ac_current   = float(input_data_strings[19][1])
        ac_frequency = float(input_data_strings[20][1])
        drivenid     = int(  input_data_strings[21][1])

        radius = 1.0 #hardwired (it isn't well defined in colloid system)
        maxtime = tot_time
        writemovietime = writemovie

        dt=0.01 #hardwired in MD code
        
        return(Sx, Sy, radius, maxtime, writemovietime, drop, dt )
    
    else:
        print("TBD")
        sys.exit()
        
################################################################
################################################################
################################################################

if __name__ == "__main__":

    print(get_input_data("Pcw0"))
    print(get_input_data("Pa0"))
