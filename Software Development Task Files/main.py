#!python3

import pickle, os, re
import journal

path = os.getcwd()
userinfo = {}
password_regex = re.compile(r'([a-zA-Z!#$&0-9]{8,})', re.VERBOSE)

try:
	if 'data' in os.listdir(path):
		data_file_read = open("data", 'rb+')
		userinfo = pickle.load(data_file_read)
		data_file_read.close()
except EOFError:
	data_file_write = open("data", 'wb+')
	data_file_write.close()

class User:
	def __init__(self, user):
		try:
			while True:
				print("\n\t\t\t\t\tYou are Logged in as {}".format(user))
				print('''\t\t\t\t\t\t1.) Post Journal\n\t\t\t\t\t\t2.) Show Journal List''')
				register__val = int(input("\t\t\t\t\t: "))
				
				self.Journal = journal.Journal()

				if register__val == 1:
					self.post_journal(user)
				elif register__val == 2:
					self.show_journal(user)
				else:
					print("\t\t\t\t\t\tWrong Value")
		except KeyboardInterrupt:
			start()

	def show_journal(self, user):
		print("\n\n\t\t\tThere is the List of all Your Journals:")
		self.Journal.list_journal(user)

	def post_journal(self, user):
		print("\n\n\t\t\tHere you can create new Journal:")
		self.Journal.create_journal(user)


class start():

	def __init__(self):
		os.system('cls')
		print("\n\t\t\t\t\t***---Software Development Task---***")
		print("\n\t\t\t\t\tPlease Enter ctrl+C to Quit:")
		print('''\t\t\t\t\t\t\t1.) Login\n\t\t\t\t\t\t\t2.) Sign Up
				''')
		register__val = int(input("\t\t\t\t\t\t: "))
		
		if register__val == 1:
			print("\n\t\t\tPlease Enter The Username:", end='	')
			_username = input()
			print("\n\t\t\tPlease Enter the Password:", end='	')
			_password = input()
			self.login(_username, _password)
		
		elif register__val == 2:
			self.signup()
		
		else:
			print("\n\t\t\t\t\t\t\tWrong Value")
		
	def signup(self):
		
		print("\n\t\t\tPlease Enter the Username:", end='	')
		entered_username1 = input()
		print("\n\t\t\tplease Enter the Password:", end='	')
		
		# To Ask fot the Valid Password not less than 8 characters
		while True:
			entered_password1 = input("\n\t\t\t")
			if password_regex.findall(entered_password1):
				break
			else:
				print("\t\t\tPlease Enter Valid Password with alphabets digits and special characters:")

		userinfo[entered_username1] = entered_password1
		
		# Make changes to this value to check Maximum Number of User can Signup:
		if len(userinfo) <= 10:
			data_file = open("data", 'wb+')
			pickle.dump(userinfo, data_file)
			data_file.close()
			print("\n\t\t\tSign Up Completed! Logging In...")
			self.login(entered_username1, entered_password1)

		else:
			print("\n\t\t\tSorry, But there are enough Users!")

	def login(self, _username, _password):
		
		try:
			# To authenticate the User Information (Username and Password)
			if userinfo[_username] == _password:
				print("\n\t\t\tYou are logged in")
				User(_username)
			else:
				print("\n\t\t\tYou Entered wrong information for authentication!")
		except Exception as KeyError:
			print("\n\t\t\tThis Username Does Not Exist. Please Signup!")
			self.signup()
		

try:
	while True:
		start()
		os.system('cls')
except KeyboardInterrupt:
	os.system('cls')
	print("You Exited")