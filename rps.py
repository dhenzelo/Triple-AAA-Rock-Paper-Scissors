# data types =
# 	numbers = enter a number (5 , 3 , 4)
# 	strings = enter a thing, but then put in "" (x = "dhenzel")
# 	booleans = True / False 
# == , !> , < , > , + - /
# x = "dhenzel"
# x = x + " obeng"

# print(x)

# classroom = [
# 	"Dhenzel" ,
# 	"Daryl" ,
# 	"Donovan" ,
# 	"Niku"	,
# 	"420" ,
# 	"69" ,
# 	"cumgang",
# ]

# for student in classroom:
# 	print(student)

import random


player_score = 0
cpu_score = 0

weapons = ["R", "P", "S"]

print ("===========================")
print (" w el come t0 RPS")
print ("===========================")

while player_score < 5 and cpu_score < 5:
	player_weapon = input("What weapon is in your hand? ((R/P/S))")
	player_weapon = player_weapon.upper()
	cpu_num = random.randint(0, 2)
	cpu_weapon = weapons[cpu_num]

	if (
		(player_weapon == "R" and cpu_weapon == "S") or
		(player_weapon == "P" and cpu_weapon == "R") or 
		(player_weapon == "S" and cpu_weapon == "P") 
	):
		print("Player wins a point!")
		player_score = player_score + 1

	elif (
		(cpu_weapon == "R" and player_weapon == "S") or
		(cpu_weapon == "P" and player_weapon== "R") or 
		(cpu_weapon == "S" and player_weapon == "P") 
	):
		print("CPU wins a point!")
		cpu_score = cpu_score + 1

	else:
		print("You're both shit")
	
	print (player_weapon)
	print (cpu_weapon)

if player_score == 5:
	print("Player Wins!")
else: 
	print("You're dogshit, you lost to the computer")

print("===========================")
print("Player Score:", player_score)
print("CPU Score:", cpu_score)
print("===========================")