#This is a MadLibs project
#My name: Michhael Garcia Celis
#Who I collaborated with: N/A
print("************************************")
print("|                                  |")
print("| Welcome to MadLibs               | ")
print("|                                  |")
print("************************************")
print("""MadLibs is a fill-in-the-blanks story
game. The player chooses words based on the
given prompts, and the program returns a
short story that includes the words the user chose.""")

play = input("Do you want to play MadLibs? (y/n) ").strip().lower()

if play.startswith('y'):
	person_name = input("Choose a name for a person: ").strip()
	place = input("Choose a place: ").strip()
	noun_1 = input("Choose a singular noun: ").strip()
	animal_1 = input("Choose an animal: ").strip()
	adjective_1 = input("Choose an adjective for a feeling: ").strip()
	adjective_2 = input("Choose an adjective: ").strip()
	adjective_3 = input("Choose an adjective: ").strip()
	animal_2 = input("Choose another animal: ").strip()
	food = input("Choose a food: ").strip()

	story = f"""
Over break I am going camping with {person_name}. It is important
to be prepared when camping at {place}, so I made sure to pack a
sleeping bag, flashlight, and a {noun_1}. The possibility of seeing a
{animal_1} makes me feel {adjective_1}. I am excited to go
hiking on the {adjective_2} trail. If I see a {adjective_3} {animal_2}
on the hike, I will take it home as my new pet! The best part of
camping is eating {food} by the campfire!
"""

	print(story)
	print("Thanks for playing! Goodbye!")
else:
	print("Goodbye!")
	

########################## Question 2#####################################
input("Would you like to do an addition problem or a subtraction problem?")
problem_type = input("Type 'addition' or 'subtraction': ").strip().lower()
if problem_type == 'addition':
	num1 = float(input("Enter the first number to add: "))
	num2 = float(input("Enter the second number to add: "))
	result = num1 + num2
	print(f"The result of adding {num1} and {num2} is: {result}")
elif problem_type == 'subtraction':
	num1 = float(input("Enter the number to subtract from: "))
	num2 = float(input("Enter the number to subtract: "))
	result = num1 - num2
	print(f"The result of subtracting {num2} from {num1} is: {result}")
else:
	print("Invalid input. Please type 'addition' or 'subtraction'.")