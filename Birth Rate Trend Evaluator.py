
number_of_data_points = int(input("How many data points do you have? "))
# Ask the user how many data points they want to enter

continue_the_program = True

# Boolean that can be used to stop loops

if number_of_data_points <= 0:
    print("Must enter at least one data point.")
    continue_the_program = False

# Conditional used to make it clear that at least one data point should be entered

else:
    data_point_number = 1
    """
    If at least one data point is entered, we can then continue on with the program
    I created a variable for the data point number
    It starts as 1
    Later on I will increase it
    """
    year_list = []
    # Created a list for all the years entered
    birth_rate_list = []
    # Created a list for all the birth rates entered
    while data_point_number <= number_of_data_points and continue_the_program:
        """
        While the data point number is less than the number of data points entered by the user
        The code in the while loop below will run
        Boolean set to True
        If Boolean is not True, loop will not run
        """
        year = int(input("What is the year of data point " + str(data_point_number) + "? "))
        # Asks the user what is the year of the data point
        if data_point_number > 1 and year < year_list[-1] and year > 0:
            print("Years must be entered in order.")
            # If it is at least the second data point, and the entered year is less than the previously entered year, then they are not in order
            continue_the_program = False
            # Boolean changed to false to end the loop
        elif data_point_number > 1 and year == year_list[-1] and year > 0:
            print("Same year entered twice.")
            # If it is at least the second data point, and the entered year is equal to the previously entered year, then the same year has been entered twice
            continue_the_program = False
            # Boolean changed to false to end the loop
        elif year > 0:
            birth_rate = float(input("What is the birth rate of data point " + str(data_point_number)+ "? "))
            # I will then ask about birth rate
            if birth_rate >= 0.0:
                year_list.append(year)
                birth_rate_list.append(birth_rate)
                # If birth rate is valid, I will add the year and birth rate to their respective lists
            else:
                print("Invalid birth rate.")
                continue_the_program = False
                # If birth rate is not greater than 0.0, it is an invalid birth rate
                # Boolean changed to false to end the loop
        else:
            print("Invalid year.")
            continue_the_program = False
            # Used for when year is not greater than 0
            # Boolean changed to false to end the loop
        data_point_number = data_point_number + 1
        # I increase the data point number
        # This will continue until the data point number is greater than the number of data points that the user has



while continue_the_program:
    # Loop will iterate only if all previous conditions are met
    data_analysis_1 = int(input("Which year would you like to start with? "))
    # Ask which year the user wants as their start year
    if data_analysis_1 in year_list:
        data_analysis_2 = int(input("Which year would you like to end with? "))
        # If their start year is in the year list, I will ask for their end year
        if data_analysis_2 in year_list and data_analysis_2 > data_analysis_1:
            x = year_list.index(data_analysis_1)
            y = year_list.index(data_analysis_2)
            birth_rate_1 = birth_rate_list[x]
            birth_rate_2 = birth_rate_list[y]
            average_birth_rate = (birth_rate_1 + birth_rate_2) / 2
            average_birth_rate_rounded = "%.2f" % average_birth_rate
            # If the end year is in the list and it is after the start year
            # I find the index of the start and end year from the year list
            # I do this so I can find the birth rates of those years from the birth rate list
            # The average of the birth rates is equal to their sum divided by 2
            # I round the average birth rate to two decimals
            if birth_rate_2 > birth_rate_1:
                print("The average birth rate of these two years is", str(average_birth_rate_rounded) + ".")
                print("There is an upward trend.")
                # If birth rate 2 is bigger than birth rate 1, there is an upward trend
                continue_the_program = False
            elif birth_rate_2 < birth_rate_1:
                print("The average birth rate of these two years is", str(average_birth_rate_rounded) + ".")
                print("There is a downward trend.")
                continue_the_program = False
                # If birth rate 2 is less than birth rate 1, there is a downward trend
            else:
                print("The average birth rate of these two years is", str(average_birth_rate_rounded) + ".")
                print("There is a sideways trend.")
                continue_the_program = False
                # If birth rate 2 is equal to birth rate 1, there is a sideways trend
        elif data_analysis_2 not in year_list:
            print("The end year does not exist.")
            # If the end year is not in the year list, it doesn't exist.
            continue_the_program = False
        elif data_analysis_2 <= data_analysis_1:
            print("End year must be after start year.")
            continue_the_program = False
            # If end year is not after start year, the program stops
    else:
        print("The start year does not exist.")
        continue_the_program = False
        # If start year is not in year list, it doesn't exist




                      
        
