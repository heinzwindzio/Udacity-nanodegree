
def test_dictionary(family_dic):

    #print(family_dic)
    #print(family_dic['father']) 
    #print(family_dic['father'][0])
    #print(family_dic['father'][1])  
    #print(family_dic['sister'][2])  #IndexError: list index out of range

    #now we have a list length of 3
    #family_dic['father'].append('04/08/1971') 

    file_dic = {}

    with open('family_names.txt', 'r') as f:
        
        for line in f:
            #populate the dic with each line a new key
            family_line_list = line.strip().lower().split(", ")

            for item in family_line_list:

                 file_dic[item] = 0

        print(file_dic)

        #loop through each key's value in the [0] position and see if there is a match within file_dic
        for key in family_dic:      
        
            print(f"Here's the first value: {family_dic[key][0]}")

            if family_dic[key][0] in file_dic:
                print("Found a match")

                #append a new value to the list, so now the list length is 3
                family_dic[key].append(1)

            if len(family_dic[key]) == 3:
                print(f"This should be a 1: {family_dic[key][2]}")   

def main():
    family_dic = {'father': ['John', 45], 'mother': ['jane', 45], 'sister': ['Lily', 20], 'brother': ['Tom', 15]}   
    test_dictionary(family_dic)
    print(family_dic)

if __name__ == '__main__':
    main()
