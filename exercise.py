# Build a small program that turns a fullname into its initials
# eg. make_initials("Will Smith") #=> 'W.S'

# Parameters
#    - fullname, a string (eg. "Xiao Chan")
# Returns
#    - string (eg. 'X.C')
# Side effects
#    - None
def make_initials(fullname):
    names = fullname.split()
    firstname = names[0][0]
    surname= names[1][0]
    return firstname + "."+ surname


# Tasks
# - 

print(make_initials('Will Smith'))