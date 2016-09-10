from sys import exit

def age():
	print "How old are you? "
	age = raw_input('> ')

	if age < '18':
		print "Access denied! (Age restriction)"
		exit()
	if age >= '18':
		print "Access granted!"

def name():
	print "What is your first name? "
	firstname = raw_input('> ')
	print "Thank you %s \nNow what is your surname?" % firstname
	surname = raw_input('> ')
	print "Is this your name\n%s %s?" % (firstname, surname)
	user_input = raw_input('> ')
	if user_input == 'yes':
		print "Welcome %s %s!" % (firstname, surname)
	if user_input != 'yes':
		name()


def username():
	print "Please create your username:"
	user_name = raw_input('> ')

def login():
	print "Please login:"
	login = raw_input('> ')
		if login == user_name:
			print "Login succesfull!"
	from username in login:
		if login != user_name:
			print "Login incorrect!"
			login()

def start():
	age()
	name()
	username()
	login()

start()
