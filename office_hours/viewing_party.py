# write a function make_address_entry(name, address)that takes a literal name and an address, and returns a dictionary with the keys "name" and "address".
#import pytest

def make_address_entry(name, address):
    entry = {
        "name": name,
        "address": address
    }

    return entry

#sumitra_entry = make_address_entry("sumitra", "123 john st")

#print("dictionary: ", sumitra_entry)

def test_make_address_entry():

    #Arrange
    name = "Becca"
    address = "Valley St"

    #Act
    entry = make_address_entry(name, address)

    #Assert
    assert entry["name"] == name
    assert entry["address"] == address

#user input
name = input("what is your name?")
address = input("what is your address?")

#function to create dictionary
entry = make_address_entry(name, address)

print("dictionary: ", entry)