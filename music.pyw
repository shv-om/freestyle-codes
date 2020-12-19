#! python3
#defining class for music

import os, sys, shelve
from tkinter import *
from tkinter import filedialog as fd

class Music(Frame):
	
	path=''
	
	def __init__(self,parent):
		Frame.__init__(self,parent)
		
		#parent.geometry("300x60")
		parent.title("Music Search")
		
		parent.music_entry = Entry(music_window, width=60)
		parent.music_entry.grid(row = 0, column = 0, columnspan = 2)
		parent.music_entry.focus_set()
		
		#disablining resizing of window or the maximize button
		parent.resizable(width = False, height = False)

		browse_music=Button(music_window,text="Browse",command=self.folder_browse).grid(row = 1, column = 0)
		play=Button(music_window,text="play",command=self.play).grid(row = 1, column = 1)

	def folder_browse(self):
		global path
		path = fd.askopenfilename(filetypes=[("music files","*.mp3")])
		music_window.music_entry.delete(0,END)
		music_window.music_entry.insert(0,path)
		return path
	
	def save_path(self):
		global path
		
		save_path = os.path.dirname(path)
		
		#comment this after creation of the files once
		music_path_c = shelve.open('music_path', 'c')
		music_path_c['music_path'] = [save_path]
		music_path_c.close()
		
		"""music_path_append = shelve.open('music_path', 'w')
		if save_path not in music_path_append['music_path']:
			music_path_append['music_path'] = music_path_append['music_path']+[save_path]
			print(music_path_append['music_path'])
		else:
			print(music_path_append['music_path'])
		music_path_append.close()"""
		
	
	def play(self):
		global path
		print(path)
		self.save_path()
		#os.startfile(path)
