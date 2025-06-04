def sort_by_consonant_count(listicle):
    
    working_dict = {}
    consonants = 'bcdfghjklmnpqrstvwxyz'
   
    for element in listicle:
        no_spaces = element.replace(' ', '')     
        max_adjacent = 0
        current_adjacent = 0   
        
        for char in no_spaces:
            if char.lower() in consonants:
                current_adjacent += 1
            else:
                if current_adjacent > max_adjacent:
                    max_adjacent = current_adjacent
                current_adjacent = 0

        if current_adjacent >= 2 and current_adjacent > max_adjacent:
            max_adjacent = current_adjacent
       
        working_dict[element] = max_adjacent
    

    interim_stage = dict(sorted(working_dict.items(), key=lambda item: item[1], reverse=True))    
    final = list(interim_stage.keys())

    return final
    

my_list1 = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list1)) #['dddaa', 'ccaa', 'aa', 'baa']

my_list2 = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list2)) #['salt pan', 'can can', 'batman', 'toucan']

my_list3 = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list3)) #['bar', 'car', 'far', 'jar']

my_list4 = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list4)) #['month', 'day', 'week', 'year']

my_list5 = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list5)) #['xxxx', 'xxxb', 'xxxa']