import meteor_data_class
import useful_functions

def main():
    file = open("meteorite_landings_data.txt", "r")
    file.readline()
    split_text = []

    while True:
        line = file.readline()
        if line == '':
            break
        strip_line = line.strip('\n')
        split_line = strip_line.split('\t')
        m_name = split_line[0]
        m_ident = split_line[1]
        m_nametype = split_line[2]
        m_recclass = split_line[3]
        m_mass = useful_functions.str_convert(split_line[4])
        m_fall = split_line[5]
        m_year = useful_functions.str_convert(split_line[6])
        m_reclat = split_line[7]
        m_reclong = split_line[8]
        m_geolocation = split_line[9]
        m_states = split_line[10]
        m_counties = split_line[11]
        print(split_line)





























if __name__ == '__main__':
    main()
