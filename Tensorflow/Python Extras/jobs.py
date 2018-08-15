'''
    Preprocesses the jobs column from the Telemarketing Dataset.
    We're going to map the categorical values to a numerical one.
'''

# This creates a mapping between the attributes
# and a value.
map_dict = {
    'unknown': 0,
    'admin': 1,
    'blue-collar': 2,
    'entrepreneur': 3,
    'housemaid': 4,
    'management': 5
}