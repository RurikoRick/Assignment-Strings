# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{scorer_0} {goal_0}, {scorer_1} {goal_1}"
report = f"{scorer_0} scored in the {goal_0}nd minute\n" + f"{scorer_1} scored in the {goal_1}th minute" 

print(scorers)
print("-----") # For a enter in the output
print(report)
print("-----") # For a enter in the output

# Part 2
player = "Ronald Koeman"
first_name = player[:player.find(" ")]
last_name = player[player.find(" ") + 1:]
last_name_len = len(last_name)
name_short = player[0:1] + ". " + last_name

print(first_name)
print(last_name)
print(last_name_len)
print(name_short)

chant = f"{first_name}! " * len(first_name[:-1]) + f"{first_name}!"
print(chant)

good_chant = f"{first_name}! " != f"{first_name}!"
print(good_chant)