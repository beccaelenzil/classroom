def add_grocery(grocery_list, new_item):
    grocery_list.append(new_item)
    return grocery_list

# grocery_list = add_grocery(['banana', 'apple'], 'mango')
# print(grocery_list)

grocery_list = add_grocery(5, 'mango')
print(grocery_list)




# import pytest

# def count(n):
#     letters = ['a','b','c']
#     for i in range(n):
#         print(letters[i])

# def test_raises_index_error_for_largen():
#     #arrange
#     n = 10

#     # assert and act
#     with pytest.raises(IndexError):
#         count(n)
        