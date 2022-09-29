import meteor_data_class
import useful_functions

def main():
    file = open("meteorite_landings_data.txt", "r")
    file.readline()
    split_data = []
    dataset_mass = []
    dataset_year = []

    while True:
        line = file.readline()
        if line == '':
            break
        strip_line = line.strip('\n')
        split_line = strip_line.split('\t')
        split_data.append(split_line)

    for meteor_entry in split_data:
        m_name = meteor_entry[0]
        m_ident = meteor_entry[1]
        m_nametype = meteor_entry[2]
        m_recclass = meteor_entry[3]
        m_mass = useful_functions.str_convert(meteor_entry[4])
        m_fall = meteor_entry[5]
        m_year = useful_functions.str_convert(meteor_entry[6])
        m_reclat = meteor_entry[7]
        m_reclong = meteor_entry[8]
        m_geolocation = meteor_entry[9]
        m_states = meteor_entry[10]
        m_counties = meteor_entry[11]








if __name__ == '__main__':
    main()

