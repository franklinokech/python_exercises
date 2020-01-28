# Program to take a string value and return a sorted version
# The set(s) will remove duplicates
# sorted(sequence) will create a sorted list of sequences
# ''.join(sequence) will create a single string out of a sequence of strings

s = input("Enter a String\n")

#sorted_string = ''.join(sorted(set(s)))

string_set = set(s)
sort_set = sorted(string_set)
final_string = ''.join(sort_set)

print(final_string)