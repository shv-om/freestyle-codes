"""
This code uses regular expression in python to solve the searching task using folder/files name inside the root directory...

You need to do some changes to use this code.

"""

import os, re
import shutil

folderlist = []
found_folder_list = []
#creating .txt file in the folder
try:
	os.makedirs(os.path.join(os.path.dirname(os.getcwd()), 'All pksl found'))
except Exception as FileExistsError:
	pass

found = open('found.txt', 'w')
found.close()

def search_list(folders, search_fol):

	fol_list_name = re.compile(r'''(
								([A-Z]{3}[\s]*[0-9]{4})
								(\s)+
								([A-Za-z]+)
								(\s)+
								([A-za-z]+)
								)''', re.VERBOSE)
	for groups in fol_list_name.findall(folders):
		#print(groups[1] + ',' + groups[2]+ ',' + groups[3]+ ',' + groups[4])
		code = groups[1]
		genus = groups[3]
		species = groups[5]
		for rootfolder, subfolder, files in os.walk(search_fol):
			print(genus)
			for file in files:
				print(os.path.basename(file))
				if genus in os.path.basename(file):
					if species in os.path.basename(file):
						print(genus + ' and ' + species + ' found.')
						#creating txt file to contain the codes and name of folder found in all data.
						found = open('found.txt', 'a')
						found.write(' '.join([code,genus,species]) +' ,\t' +'\\'.join([rootfolder,file]) + '\n')
						#found.write(' '.join([code,genus,species]) + '\n')
						found.close()
						#appending found folder list
						#found_folder_list.append(' '.join([code,genus,species]))
						return True 	#break
	#print(found_folder_list)



def collect_name():

	search_folder_path = os.getcwd()	#to get current working directory
	data_folder = input("Please enter the full path of folder where the search will occur.\n")
	for rootfolder, subfolder, filename in os.walk(search_folder_path):
		name = re.compile(r'''(
							([A-Z]{3}[\s]*[0-9]{4})
							(\s)+
							([A-Za-z]+)
							(\s)+
							([A-Za-z]+)
							(.*)
							)''', re.VERBOSE)
		for groups in name.findall(rootfolder):
			#print(groups[0]+','+groups[1]+','+ groups[2]+','+groups[3]+','+groups[4]+','+groups[5]+','+groups[6])
			if search_list(' '.join([groups[1],groups[3],groups[5]]), data_folder) == True:
				print(shutil.move(rootfolder, os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'All pksl found'), os.path.basename(rootfolder))))
			#folderlist.append(' '.join([groups[1],groups[3],groups[5]]))
	#print(folderlist)
	#search_list(folderlist)

collect_name()
