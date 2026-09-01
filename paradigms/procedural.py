# Statements are structured into procedures
# The program composition is more of a procedure call where the programs might reside
# somewhere in the universe and the execution is sequential, thus becoming a bottleneck
# for resource utilization

def stringify(characters):
    string = ''
    for c in characters:
        string = string + c
    return stringify

sample_characters = ['p','y','t','h','o','n']
stringify(sample_characters)