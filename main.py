# Part 1
scorer_name_1 = "Ruud Gullit"
scorer_name_2 = "Marco van Basten"

when_they_scored_1 = 32
when_they_scored_2 = 54

scorers = scorer_name_1 + " " + str(when_they_scored_1), \
          scorer_name_2 + " " + str(when_they_scored_2)

report = scorer_name_1 + " scored in the " + str(when_they_scored_1) + "nd minute\n" \
         + scorer_name_2 + " scored in the " + str(when_they_scored_2) + "th minute"

print(scorers)
print()
print(report)
print()

# Part 2
player = "Ronald Koeman"
first_name = slice(6)
last_name_len = slice(7, 13)
number1 = player.find("l")
number2 = player.find("R")
number3 = len(player)


print(player[first_name])     # slice function
print(number1)                # find function
print(player[last_name_len])  # slice function
print(number2)                # find function
print(number3)                # len function

name_short = "R. Koeman"
chant = "Ron! Ron! Ron!"