# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1="Ruud Gullit"
scorer_2="Marco van Basten"
goal_0=32

goal_1=54
scorers=scorer_1 + " " + str(goal_0) + "," + " " + scorer_2 + " " + str(goal_1)
report= f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"
print(len(scorer_1))

player="Er Koema"
find_first_name=player.find(" ")
first_name=player[:find_first_name]
print(first_name)

find_last_name=player.find(" ")
last_name_len=len(player[find_last_name:-1])
print(last_name_len)

last_name=player[find_first_name:]
name_short=f"{first_name[0]}.{last_name}"
print(name_short)

length_first_name=len(first_name)
excl_first_name=(f"{first_name}! ")
chant=(excl_first_name*length_first_name).strip()
print(chant)

good_chant = chant[-1] != " "
print(good_chant)



