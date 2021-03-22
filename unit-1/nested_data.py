karaoke_queue = {
        "Rajan": ["I Want It That Way", "Jolene"],
        "Akira": ["Return of the Mack", "Mr. Brightside", "Jolene"],
        "Linh": ["Say My Name", "Since You Been Gone"]
    }

def get_song_list(karaoke_queue):
    """
    input: dictionary with keys that are names, and song list as values
    output: list of all the songs
    """
    # initializing and empty list
    songs = []
    # iterate through the dictionary
    #for friend, requests in karaoke_queue.items():
    for friend, requests in karaoke_queue.items():
        for request in requests:
            if request in songs:
                continue
            else:
                songs.append(request)

    #return the list
    return songs

print(get_song_list(karaoke_queue))


# school_dict = {
#         "school 1": {
#             "name": "Western Barkington University",
#             "city": "Barkingham"
#         },
#         "school 2": {
#             "name": "University of Barkington",
#             "city": "Beattle"
#         },
#         "school 3": {
#             "name": "Barkington State University",
#             "city": "Pullbark"
#         }
#     }

# def get_school_names(school_dict):
#     """
#     input: dictionary of dictionaries with school data
#     output: list of school names
#     """
#     # initialize an empty list
#     names = []
#     # iterate through dictionary
#     #for school_num, school_info in school_dict.items():
#     for key in school_dict:
#         #get the name of each school, and append it to the list
#         #school_info = school_dict[key]
#         names.append(school_dict[key]["name"])
#     # return the list
#     return names

# print(get_school_names(school_dict))










# karaoke_queue = {
#         "Rajan": ["I Want It That Way", "Jolene"],
#         "Akira": ["Return of the Mack", "Mr. Brightside", "Jolene"],
#         "Linh": ["Say My Name", "Since You Been Gone"]
#     }

# def get_song_list(karaoke_queue):
#     # initialize an empty list
#     song_list = []
#     # iterate over karaoke_queue
#     #for name, songs in karaoke_queue.items():
#     for name in karaoke_queue:
#         # iterate over the value (lists)
#         #songs = karaoke_queue[name]
#         #for song in songs:
#         for song in karaoke_queue[name]:
#             # append each song title to our empty list
#             if song not in song_list:
#                 song_list.append(song)
    
#     # return strong_list
#     return song_list


# print(get_song_list(karaoke_queue))


# # def test_get_school_names():
# #     schools = {
# #         "school 1": {
# #             "name": "Western Barkington University",
# #             "city": "Barkingham"
# #         },
# #         "school 2": {
# #             "name": "University of Barkington",
# #             "city": "Beattle"
# #         },
# #         "school 3": {
# #             "name": "Barkington State University",
# #             "city": "Pullbark"
# #         }
# #     }

# #     names = get_school_names(schools)

# #     assert names == ["Western Barkington University",
# #                      "University of Barkington", "Barkington State University"]


# # def test_get_school_names_no_names():
# #     no_names = get_school_names({})
# #     assert no_names == []

# # def get_school_names(school_dict):
# #     '''
# #     input -> schools, nested dictionary
# #     ouput -> list of names
# #     '''
# #     # initialize list for names
# #     names = []
# #     # iterate through schools dictionary
# #     for school, info in school_dict.items():
# #         # for key, value in info.items():
# #         #     if key == "name"
# #         names.append(value["name"])
# #         #names.append(school_dict[key]["name"])

# #     # get the name of each school and append it to the list
# #     # return the list
# #     return names

# # school_dict = {
# #         "school 1": {
# #             "name": "Western Barkington University",
# #             "city": "Barkingham"
# #         },
# #         "school 2": {
# #             "name": "University of Barkington",
# #             "city": "Beattle"
# #         },
# #         "school 3": {
# #             "name": "Barkington State University",
# #             "city": "Pullbark"
# #         }
# #     }

# # print(get_school_names(school_dict))
# # print(get_school_names({}))