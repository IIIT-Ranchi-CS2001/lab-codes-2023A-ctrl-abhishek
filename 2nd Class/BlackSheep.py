S = "Ba Ba Black Sheep"
length_of_S = len(S)
print(f"Length of the string S: {length_of_S}")
first_occurrence_of_e = S.find('e')  
print(f"First occurrence of the letter 'e': {first_occurrence_of_e}")
total_occurrences_of_a = S.lower().count('a')
print(f"Total number of occurrences of 'a': {total_occurrences_of_a}")
modified_string = S.replace('Ba', 'Ta', 2) 
print(f"Modified string: {modified_string}")