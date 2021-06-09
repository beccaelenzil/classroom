
def pairs_with_given_sum(numbers, target):
    for number in numbers:
        n = target - number
        if n in numbers:
            count += 1

# # def pairs_with_given_sums(numbers, target):
# #     count = 0
# #     n = len(numbers)
# #     for i in range(n-1):
# #         for j in range(i+1,n):
# #             if (numbers[i] + numbers [j]) == target:
# #                 count += 1

# #     return count

# # print(pairs_with_given_sums([1, 2, 4, 5],6))
# # print(pairs_with_given_sums([97, 51, 49, 35, 3, 65],100))


# def pairs_with_given_sums(list1):

#     n = len(numbers)
#     count = 0

#     for i in range(n-1):
#         for j in range(i+1,n):
#             print("pairs: ", numbers[i], numbers[j])
#             if numbers[i] + numbers[j] == target:
#                 count += 1

#     return count

# print(pairs_with_given_sums([1, 2, 4, 5],6))
# print(pairs_with_given_sums([97, 51, 49, 35, 3, 65],100))

# def sort(numbers1, numbers2):

#     i = 0
#     j = 0

#     #keep going until I've made it through both lists
#     while i < len(numbers1) and j < len(numbers2):

#     #find lowest, if lower is in numbers1, incremement i, 
#     # if lowest is in numbers2, increment j    
#         if numbers1[i] < numbers[j]:
#             # append numbers[i] to sorted list
#         else:
#             # append numbers[j] to sorted list
