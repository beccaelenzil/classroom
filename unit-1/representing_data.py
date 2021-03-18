def find_seq_diff(seq1, seq2):
    differences = []
    n = len(seq1)
    # loop n times
    for i in range(n):
        # check if the elements in each sequence are different
        if seq1[i] != seq2[i]:
            # if they're different, store the difference
            differences.append([seq1[i], seq2[i]])

    return differences

differences = find_seq_diff('GAGCCTACTAACGGGAT', 	'CATCGTAATGACGGCCT')

print("These are the differences:", differences)
print("There are ", len(differences), "of them.")








# #Q1
# def find_seq_diffs(seq1, seq2):
#     i = 0
#     n1 = len(seq1)
#     n2 = len(seq2)
#     if n1 != n2:
#         return None
#     else:
#         differences = []
#         for i in range(n1):
#             if seq1[i] != seq2[i]:
#                 differences.append([seq1[i], seq2[i]])

#     return differences


# seq1 = 'GAGCCTACTAACGGGAT'
# seq2 = 'CATCGTAATGACGGCCT'
# differences = find_seq_diffs(seq1, seq2)

# print("There are", len(differences), "differences.")
# print("Here they are:", differences)

# #Q2
# color_data_by_time = {
#     '8:00': ['red', 'orange', 'green'],
#     '9:00': ['red', 'orange'],
#     '10:00': ['blue'],
#     '11:00': ['blue', 'green'],
#     '12:00': ['blue', 'gray']
# }

# def find_color_freq(color_data_by_time):
#     color_freq = {}
#     for time in color_data_by_time:
#         for color in color_data_by_time[time]:
#             if color in color_freq.keys():
#                 color_freq[color] += 1
#             else:
#                 color_freq[color] = 1
#     return color_freq

# print(find_color_freq(color_data_by_time))

