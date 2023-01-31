def read_dna(dna_filename):
    f = open(dna_filename)
    contents = f.read()
    return contents

def dna_length(dna_filename):
    return len(read_dna(dna_filename))

def read_strs(str_filename):
    import csv
    with open(str_filename, 'r') as myfile:
        csv_reader = csv.reader(myfile)
        name_list = []
        agat_list = []
        aatg_list = []
        tatc_list = []
        for i in csv_reader:
            name_list.append(i[0])
            agat_list.append(i[1])
            aatg_list.append(i[2])
            tatc_list.append(i[3])

        dic1 = {name_list[0]: name_list[1], agat_list[0]: agat_list[1], aatg_list[0]: aatg_list[1], tatc_list[0]: tatc_list[1]}
        dic2 = {name_list[0]: name_list[2], agat_list[0]: agat_list[2], aatg_list[0]: aatg_list[2], tatc_list[0]: tatc_list[2]}
        dic3 = {name_list[0]: name_list[3], agat_list[0]: agat_list[3], aatg_list[0]: aatg_list[3], tatc_list[0]: tatc_list[3]}
        all_dic = [dic1, dic2, dic3]
        return all_dic

def get_strs(str_profile):
    x = str_profile['AGAT']
    y = str_profile['AATG']
    z = str_profile['TATC']
    tup = [('AGAT', int(x)), ('AATG', int(y)), ('TATC', int(z))]
    return tup

def longest_str_repeat_count(str_frag, dna_sequence):                          
    count = 0
    i = 0
    largest_count = 0
    while i < len(dna_sequence):
        if dna_sequence[i:i+4] == str_frag:
            i += 4
            count += 1
            if count > largest_count:
                largest_count = count
        else:
            count = 0
            i+=1
    return largest_count

def find_match(str_profile, dna_seq):
    for i in str_profile:
        for k in get_strs(i):
            count = longest_str_repeat_count(k[0], dna_seq)
            if count != k[1]:
                return False
        return True

def dna_match(str_filename, dna_filename):
    count = 0
    while count < len(read_strs(str_filename)):
        for i in read_strs(str_filename):
            count += 1
            for j in get_strs(i) :
                if find_match(j, read_dna(dna_filename)) == True:
                    r = i['name']  
                    return r
    r = "No match"
    return r

if __name__ == '__main__':
    print(read_dna('dna_1.txt'))
    print(dna_length('dna_1.txt'))
    profiles = read_strs('str_profiles.csv')
    print(profiles)
    print(get_strs(profiles[0]))
    print(get_strs(profiles[0])[0])
    print(longest_str_repeat_count('TATC', read_dna('dna_1.txt')))
    print(find_match(read_strs('str_profiles.csv'), 'dna_1.txt'))
    print(dna_match('str_profiles.csv', 'dna_1.txt'))