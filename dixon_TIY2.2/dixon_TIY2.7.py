# Program 2.7  Using "strip" commands to alter unneeded whitespace.
# After first taking the variable "name",
#   each command after (using "strip") alters the whitespace
#    either on the left or the right, or all!
# The absolute value " | | " signs were used to show what happened to the whitespace
#  after it got printed. This "discovery" was found by (and credited to) Manuel.
name =  '   james   '
print(f"\t|{name}|\n|{name.rstrip()}|\n|{name.lstrip()}|\n|{name.strip()}|")


