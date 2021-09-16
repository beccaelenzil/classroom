schools = {
        "school 1": {
            "name": "Western Barkington University",
            "city": "Barkingham"
        },
        "school 2": {
            "name": "University of Barkington",
            "city": "Beattle"
        },
        "school 3": {
            "name": "Barkington State University",
            "city": "Pullbark"
        }
    }

def get_school_names(schools):
    names = []
    for school, school_info in schools.items():
        for key in school_info:
            names.append(school_info["name"])
        
    return names

print(get_school_names(schools))