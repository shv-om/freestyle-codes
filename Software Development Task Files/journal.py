#!python3

import datetime
import pickle, os

class Journal:
	
	def create_journal(self, username):

		journal_text = input("\n\t\tplease Enter Anything to test:\n\t\t")
		journal_posted = datetime.datetime.now()
		
		try:
			#Make Changes to this Value to check the queue like structure of journal entries:
			if len(data[username]) >= 50:
				print("\n\t\t\t\t\tWarning! Journal Limited to 50\n\t\t\t\t\t")
				data[username].pop(0)
			else:
				print("\n\t\t\t\tNo Problem")
			data[username].append({journal_posted.strftime(time_format): journal_text})
		except KeyError:
			data[username] = [{journal_posted.strftime(time_format): journal_text}]

		journal_file = open("journal_file", 'wb+')
		pickle.dump(data, journal_file)
		journal_file.close()

	def list_journal(self, username):
		for key in data:
			if key == username:
				for subvalues in data[key]:
					for i in subvalues:
						print("\n\t\t" + i + " :- " + subvalues[i])

# Time to confirm the Time of Application Start
time_format = '%d %m %Y %I:%M %p'	# Time Pattern Format for the Journal Enteries
app_started = datetime.datetime.now()
print(app_started.strftime(time_format))

path = os.getcwd()
data = {}	#dictionary to store all the updation of the Journal updation etc.

try:
	if 'journal_file' in os.listdir(path):
		journal_read = open("journal_file", 'rb+')
		data = pickle.load(journal_read)
		journal_read.close()
except EOFError:
	journal_file_write = open("journal_file", 'wb+')
	journal_file_write.close()