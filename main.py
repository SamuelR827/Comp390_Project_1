import meteor_data_class
import useful_functions


def main():
    # The main function.
    # Open the meteor data file and setup variables, read the file once to skip the header line.
    # Setup empty lists for the datasets, and setup print variables.
    file = open("meteorite_landings_data.txt", "r")
    file.readline()
    split_data = []
    dataset_mass = []
    dataset_year = []
    name_label = 'NAME'
    mass_label = 'MASS (g)'
    year_label = 'YEAR'

    # Will loop and read each file of the meteor dataset line by line until it reaches the end.
    # The loop will break if it checks that the line is empty.
    # Otherwise, strip and split each line of the dataset and assign it to a new list.
    # This list contains each field for the meteorite.
    # Then add each meteor to a new data list, a list within a list.
    while True:
        line = file.readline()
        if line == '':
            break
        strip_line = line.strip('\n')
        split_line = strip_line.split('\t')
        split_data.append(split_line)

    # For each meteor entry in the new data list,
    # assign variables to each index seperated in the meteor list, which are strings.
    # Convert year and mass into an int by calling convert function in useful functions file.

    for meteor_entry in split_data:
        entry_name = meteor_entry[0]
        entry_ident = meteor_entry[1]
        entry_nametype = meteor_entry[2]
        entry_recclass = meteor_entry[3]
        entry_mass = useful_functions.str_convert(meteor_entry[4])
        entry_fall = meteor_entry[5]
        entry_year = useful_functions.str_convert(meteor_entry[6])
        entry_reclat = meteor_entry[7]
        entry_reclong = meteor_entry[8]
        entry_geolocation = meteor_entry[9]
        entry_states = meteor_entry[10]
        entry_counties = meteor_entry[11]
        # Check if mass > 2900000, and it is not 0 . If yes create a new meteor class by calling the class
        # with each corresponding field as a parameter. Then add the new meteor to the mass list.
        if entry_mass > 2900000 and entry_mass != 0:
            meteor = meteor_data_class.MeteorDataEntry(entry_name, entry_ident, entry_nametype,
                                                       entry_recclass, entry_mass, entry_fall,
                                                       entry_year, entry_reclat, entry_reclong,
                                                       entry_geolocation, entry_states, entry_counties)
            dataset_mass.append(meteor)

        # Check if year > 2013, and is not 0. If yes create a new meteor class by calling the class
        # with each corresponding field as a parameter. Then add the new meteor to the year list.
        elif entry_year >= 2013 and entry_year != 0:
            meteor = meteor_data_class.MeteorDataEntry(entry_name, entry_ident, entry_nametype,
                                                       entry_recclass, entry_mass, entry_fall,
                                                       entry_year, entry_reclat, entry_reclong,
                                                       entry_geolocation, entry_states, entry_counties)
            dataset_year.append(meteor)
        # If no other condition is satisfied, skip the meteor.
        else:
            continue
    # Print the names and mass of each meteor belonging to the mass list in a formatted table.
    print(f'{name_label:<24}{mass_label:<20}')
    print('===========================================')
    for meteor in dataset_mass:
        print(f'{meteor.field_name:<24}{meteor.field_mass:<20}')

    # Print a newline character to separate mass and year table.
    print('\n')
    # Print the names and year of each meteor belonging to the year list in a formatted table.
    print(f'{name_label:<24}{year_label:<20}')
    print('===========================================')
    for meteor in dataset_year:
        print(f'{meteor.field_name:<24}{meteor.field_year:<20}')


if __name__ == '__main__':
    main()
