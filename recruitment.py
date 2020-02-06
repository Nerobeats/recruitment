def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	cv["name"] = input("Please enter your name:  ")
	cv["age"] = input("please enter your age:  ")
	cv["experience"] = input("please enter your years of experience:  ")
	cv["skills"] = []
	i=1
	for skill in skills:
		print (str(i) + " " +skill)
		i+=1
	cv["skills"].append(skills[int((input("please choose your skill by entering skill number:  " ))) -1])
	cv["skills"].append(skills[int((input("please choose another skill by entering skill number:  " ))) -1])
	if cv["age"] < 40 and cv["age"] > 25 and cv["experience"] > 5 and skills[5] in cv["skills"] :
		print("You have been accepted, {}.".format(cv["name"]))
	else :
		print("You have been rejected, {}.".format(cv["name"]))



if __name__ == '__main__':
	main()
