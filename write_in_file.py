def write_in_file(path_to_dir, write_file, list_data):
    """Writing the required data to a separate file.

    We will use the recording of the necessary data, in this case, the name of the file
    from which the values were taken, year, month, day, lead time, hour of calculation
    and wind speed in a separate file, since the files with predicted data contain a large
    amount of information and, if necessary, make calculations for these points, it will be
    much faster to retrieve data from a file that contains only the necessary information

    """
    my_file = open(path_to_dir + write_file, 'w')
    for i in range(0, len(list_data)):
        for j in range(0, len(list_data[i])):
            if j == (len(list_data[i]) - 1):
                my_file.write(str(list_data[i][j]))
            else:
                my_file.write(str(list_data[i][j]) + ';')
        my_file.write('\n')
    my_file.close()
    return print('End of writing list in file')