# ACME WEATHER DATA APP

Your task is to implement a program, the "ACME WEATHER DATA APP" (tm), which 

- Can read the data in any given CSV file. The program asks the user to type the file name, and given a CSV file it reads the weather data and stores it in a data structure. 
- After the program has read data the user should be able to select one day in the 25 day period by typing it's date, and the program should print that days average, minimum and maximum temperatures, in addition to the average rainfall of the day. 
- The program should calculate some average statistics of the data: Calculate the average of the entire 25 days (by using the mean temperature of individual days). Also calculate the average minimum temperature and average maximum temperature. 
- In addition, the program should also draw a simple text based scatterplot of the average temperatures. 

In the assignment your task is to interpret and analyze weather data from the Finnish Meteorological Institute. You can access these same data at https://en.ilmatieteenlaitos.fi/past-30-day-weather. In short, we will use weather data from the last 25 days, calculate some averages, and analyze weather on individual days.

You need to save these files (right-click the link and select "Save file as" from your browser) into the working directory you will be storing the program code in the assignment. 

## THE MENU

The program should operate in an infinite loop, where a menu of four options is presented. The user can choose from five options: 

        1) Choose weather data file
        2) See data for selected day
        3) Calculate average statistics for the data
        4) Print a scatterplot of the average temperatures
        0) Quit program

Choosing 0 should end the program (= break out of the loop). Following is an example of the menu's operation. 

At the end of the loop print an additional empty line (= after the number choice and whatever the choice makes the program print, but before the next "ACME WEATHER..." line). 

## LOADING THE DATA

Implement a function which asks the user for a file name, and then reads the data into a list data structure. Once loaded, the function should print "Loaded weather data from [town name]." You can get the town name from the file name. 

The function should return a list containing all weather data. How you store the data in the list is up to you (that is, you can simply store one line from the file as one item in the list, but you can also do something different..) 

## VIEWING DAILY DATA AND CALCULATING AVERAGES

When the user selects viewing daily data the program should ask for a date, and the program should look up that day's weather data, and show the average temperature, minimum temperature, maximum temperature and the daily rainfall measure. 

When the user selects calculating average statistics, calculate the average of all average temperatures of all days. Also calculate the average minimum temperature and average maximum temperature. 

## PRINTING THE SCATTERPLOT

When choosing the fourth option from the menu, the program should print a scatterplot of the daily temperatures, using just plain text, numbers, and the dash symbol (-). An example plot is below: 

    06.10                            -
    07.10                            -
    08.10                               -
    09.10                               -
    10.10                                     -
    11.10                                              -
    12.10                                              -
    13.10                                           -
    14.10                               -
    15.10                            -
    16.10                                     -
    17.10                               -
    18.10                                        -
    19.10                                                    -
    20.10                                              -
    21.10                                     -
    22.10                                              -
    23.10                                              -
    24.10                                                 -
    25.10                                                 -
    26.10                                        -
    27.10                         -
    28.10                   -
    29.10             -
    30.10                -
          -5 -4 -3 -2 -1 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 

The dashes (lines) represent temperatures. The vertical axis has the 25 dates, whereas the horizontal axis has temperatures from -5 to 15 centigrade. 

The first function, print_temperature_line(day, month, temp), takes three parameters:

1. the day as a string, in "dd" format
2. the month as a string, in "mm" format
3. the temperature as an integer number (note that this value should be rounded!)

The second function, print_temperature_line()  takes no parameters. It only prints the last of the scatterplot chart, i.e. the numeric temperature scale. 

    def print_temperature_line(day, month, temp): 
        
        print(day + "." + month + " ", end="")

        print("   "*(temp+5) + "-", end="")
        
        print()


    def print_temperature_axis():
        print("      ", end="")
        for i in range(-5,16):
            print("{:02d} ".format(i), end="")
        print()

## ADDITIONAL REQUIREMENTS
In addition to the features described below, there are the following requirements: 

  - You must implement the features described above as functions. Each menu choice has to be implemented as a function (that is, after the user selects an option, a function is called). 
  - You may not use global variables! (Go back to Lesson 6 for what global scope for a variable means.) 