#To Do List that organizes items into now, soon and eventually lists

#Import
try: 
	from Tkinter import *
except:
	from tkinter import *
from datetime import datetime
import helper_methods
from datetime import datetime
import helper_methods

#global variables
to_do_list= []
now_items= []
soon_items= []
eventually_items= []


class GUI:
	def __init__(self, root):
		#Home Screen

		#Frames
		frame= Frame(root)
		frame.pack()

		frame_two= Frame(root)
		frame_two.pack()

		frame_three= Frame(root)
		frame_three.pack()

		frame_four= Frame(root)
		frame_four.pack()

		frame_five= Frame(root)
		frame_five.pack()


		self.title= Label (frame, text= "To Do List", width= 15, height=1, font= ("Helvetica", 52))
		self.title.pack()


		#Add Entry
		self.add_entry_button= Button(frame, text= "Add Entry", height= 1, font= ("TkDefaultFont", 12), command= lambda: self.make_entry_name(frame,to_do_list))
		self.add_entry_button.config(height= 1, width= 9)
		self.add_entry_button.pack()

		self.seperator_two= Label(frame)
		self.seperator_two.pack()


		#Now List
		self.now_title= Label (frame, text= "Now", font=("Helvetica", 32))
		self.now_title.pack()
		self.scrollbar = Scrollbar(frame_two, orient=VERTICAL)
		self.now_list= Listbox(frame_two, height= 8, width= 42, font= ("Courier"), yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.now_list.yview)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.now_list.pack(fill=BOTH, expand=1)
		self.now_list.pack()	

		self.delete_now= Button(frame_three, text= "Clear Item", font= ("TkDefaultFont", 12), command= lambda now_list=self.now_list: self.delete_item_now(frame, now_list, to_do_list))
		self.delete_now.config(height= 2, width= 8)
		self.delete_now.pack()
		

		#Soon List
		self.soon_title= Label (frame_three, text= "Soon", font=("Helvetica", 32))
		self.soon_title.pack()
		self.scrollbar_two = Scrollbar(frame_three, orient=VERTICAL)
		self.soon_list= Listbox(frame_three, height= 8, width=42, font= ("Courier"), yscrollcommand=self.scrollbar_two.set)
		self.scrollbar_two.config(command=self.soon_list.yview)
		self.scrollbar_two.pack(side=RIGHT, fill=Y)
		self.soon_list.pack(fill=BOTH, expand=1)
		self.soon_list.pack()

		self.delete_soon= Button(frame_four, text= "Clear Item", font= ("TkDefaultFont", 12), command= lambda soon_list=self.soon_list: self.delete_item_soon(frame, soon_list, to_do_list))
		self.delete_soon.config(height= 2, width= 8)
		self.delete_soon.pack()
		

		#Eventually List	
		self.eventually_title= Label (frame_four, text= "Eventually", font=("Helvetica", 32))
		self.eventually_title.pack()
		self.scrollbar_three = Scrollbar(frame_four, orient=VERTICAL)
		self.eventually_list= Listbox(frame_four, height= 8, width=42, font= ("Courier"), yscrollcommand=self.scrollbar_three.set)
		self.scrollbar_three.config(command=self.eventually_list.yview)
		self.scrollbar_three.pack(side=RIGHT, fill=Y)
		self.eventually_list.pack(fill=BOTH, expand=1)
		self.eventually_list.pack()

		self.delete_eventually= Button(frame_five, text= "Clear Item", font= ("TkDefaultFont", 12), command= lambda eventually_list=self.eventually_list: self.delete_item_eventually(frame, eventually_list, to_do_list))
		self.delete_eventually.config(height= 2, width= 8)
		self.delete_eventually.pack()

		#Loads an existing to_do_list if user_data.txt exists
		to_do_list= helper_methods.unsave_to_do()

		try:
			if len(to_do_list)!=0:
				self.display_to_do_list(frame, to_do_list)
		except:
			to_do_list= []
	

	def delete_item_now(self, frame, list_delete, to_do_list):
		
		try:
			#Delete button for now_list
			a= int(list_delete.curselection()[0])
			b= self.now_items[a]
			to_do_list.remove(b)
			list_delete.delete(ANCHOR)
			helper_methods.save_to_do(to_do_list)
			self.display_to_do_list(frame, to_do_list)
		except:
			pass


	def delete_item_soon(self, frame, list_delete, to_do_list):
		try:
			#Delete button for soon_list
			a= int(list_delete.curselection()[0])
			b= self.soon_items[a]
			to_do_list.remove(b)
			list_delete.delete(ANCHOR)
			helper_methods.save_to_do(to_do_list)
			self.display_to_do_list(frame, to_do_list)
		except:
			pass

	def delete_item_eventually(self, frame, list_delete, to_do_list):
		#Delete button for eventually_list
		try:
			a= int(list_delete.curselection()[0])
			b= self.eventually_items[a]
			to_do_list.remove(b)
			list_delete.delete(ANCHOR)
			helper_methods.save_to_do(to_do_list)
			self.display_to_do_list(frame, to_do_list)
		except:
			pass



	def make_entry_name (self, frame,to_do_list):
		#method for make entry button

		self.add_entry_button.pack_forget()

		self.now_title.pack_forget()
		self.now_list.pack_forget()
		self.scrollbar.pack_forget()
		self.delete_now.pack_forget()

		self.soon_title.pack_forget()
		self.soon_list.pack_forget()
		self.scrollbar_two.pack_forget()
		self.delete_soon.pack_forget()

		self.eventually_title.pack_forget()
		self.eventually_list.pack_forget()
		self.scrollbar_three.pack_forget()
		self.delete_eventually.pack_forget()



		self.name_title= Label (frame, text= "Name of assignment", height= 2)
		self.name_title.pack()

		self.entry_text_box_name= Entry(frame)
		self.entry_text_box_name.pack()

		self.name_entry_add_button= Button (frame, text= "Enter", height=2, command= lambda: self.make_entry_date(frame, to_do_list))
		self.name_entry_add_button.pack()

	def make_entry_date (self, frame, to_do_list): 
		#method for when due date is entered

		#checks if valid name
		name= self.entry_text_box_name.get()
		check_valid_name= helper_methods.check_name_valid(name)

		if check_valid_name== False:
			try:
				self.invalid_name.winfo_exists()
				self.invalid_name.pack()
			except:
				self.invalid_name= Label(frame, text= "You didn't enter anything", fg="red" )
				self.invalid_name.pack()
		else: 
			try:
				self.invalid_name.winfo_exists()
				self.invalid_name.pack_forget()
			except: 
				pass

			self.name_title.pack_forget()
			self.entry_text_box_name.pack_forget()
			self.name_entry_add_button.pack_forget()
			self.due_date_title= Label (frame, text= "When is the assignment due?", height=2)
			self.due_date_title.pack()

			self.tomorrow_button= Button (frame, text= "Tomorrow", height=2, command= lambda: self.add_tomorrow_item(frame,name, to_do_list))
			self.tomorrow_button.pack()

			self.or_title= Label (frame, text= "OR", height=2)
			self.or_title.pack()

			self.due_date_directions= Label (frame, text= "Enter date: mm/dd/yyyy", height=1)
			self.due_date_directions.pack()

			self.entry_text_box_one= Entry(frame)
			self.entry_text_box_one.pack()

			self.entry_add_button_one= Button (frame, text= "Enter", height=2, command= lambda: self.make_entry_days_needed(frame,name, to_do_list))
			self.entry_add_button_one.pack()

	def make_entry_days_needed (self, frame, name, to_do_list): 
		#method for when days_needed is entered

		#first checks if the date received is valid
		due_date= self.entry_text_box_one.get()
		check_valid_date= helper_methods.check_date_valid(due_date)

		if check_valid_date== False:
			#checks if other error label exists
			try:
				self.not_future_date.winfo_exists()
				self.not_future_date.pack_forget()
				try:
					self.not_valid_date.winfo_exists()
					self.not_valid_date.pack()

				except:
					self.not_valid_date= Label(frame, text= "Not valid, match formatting with instructions eg. 1/7/2015", fg="red" )
					self.not_valid_date.pack()

			#checks if relevant error label exists
			except:
				try:
					self.not_valid_date.winfo_exists()
				except:
					self.not_valid_date= Label(frame, text= "Not valid, match formatting with instructions eg. 1/7/2015", fg="red" )
					self.not_valid_date.pack()
		elif check_valid_date== "earlier date":	

			#checks if other error label exists
			try:
					self.not_valid_date.winfo_exists()
					self.not_valid_date.pack_forget()
					try:
						self.not_future_date.winfo_exists()
						self.not_future_date.pack()
					except:
						self.not_future_date= Label(frame, text= "Not valid, this date is in the past", fg="red" )
						self.not_future_date.pack()

			#checks if relevant error label exists			
			except: 
				try:
					self.not_future_date.winfo_exists()
				except:
					self.not_future_date= Label(frame, text= "Not valid, this date is in the past", fg="red" )
					self.not_future_date.pack()

		#if date is valid, makes days_needed entry screen
		else:
			#removes error messages
			try: 
				self.not_valid_date.winfo_exists()
				self.not_valid_date.pack_forget()
			except:
				pass

			try:
				self.not_future_date.winfo_exists()
				self.not_future_date.pack_forget()
			except:
				pass

			#makes days_needed entry box
			self.due_date_title.pack_forget()
			self.tomorrow_button.pack_forget()
			self.or_title.pack_forget()
			self.entry_text_box_one.pack_forget()
			self.due_date_directions.pack_forget()
			self.entry_add_button_one.pack_forget()

			self.days_needed_directions= Label (frame, text= "Days of work required: ", height=1)
			self.days_needed_directions.pack()

			self.entry_text_box_two= Entry(frame)
			self.entry_text_box_two.pack()

			self.entry_add_button_two= Button (frame, text= "Enter", height=1, command= lambda: self.entry_added(frame, name, due_date, to_do_list))
			self.entry_add_button_two.pack()

	def add_tomorrow_item (self, frame, name, to_do_list):
		#For when tomorrow button is pressed
		current_date= datetime.now()
		month= int (current_date.month)
		day= int (current_date.day)+1
		year= int (current_date.year)

		due_date= str(month)+ '/' +str(day) + '/' +str(year)
		days_needed= 1

    	#goes to homescreen
		try: 
			self.not_valid_date.winfo_exists()
			self.not_valid_date.pack_forget()
		except:
			pass

		try:
			self.not_future_date.winfo_exists()
			self.not_future_date.pack_forget()
		except:
			pass

		#Returns to homescreen
		self.due_date_title.pack_forget()
		self.tomorrow_button.pack_forget()
		self.or_title.pack_forget()
		self.entry_text_box_one.pack_forget()
		self.due_date_directions.pack_forget()
		self.entry_add_button_one.pack_forget()
		self.seperator_two.pack_forget()

		self.add_entry_button.pack()
		self.seperator_two.pack()


		self.now_title.pack()
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.now_list.pack(fill=BOTH, expand=1)
		self.now_list.pack()
		self.delete_now.pack()

		self.soon_title.pack()
		self.scrollbar_two.pack(side=RIGHT, fill=Y)
		self.soon_list.pack(fill=BOTH, expand=1)
		self.soon_list.pack()
		self.delete_soon.pack()
	
		self.eventually_title.pack()
		self.scrollbar_three.pack(side=RIGHT, fill=Y)
		self.eventually_list.pack(fill=BOTH, expand=1)
		self.eventually_list.pack()
		self.delete_eventually.pack()

		to_do_list.append([name, due_date, days_needed])

		helper_methods.save_to_do(to_do_list)
		
		self.display_to_do_list(frame, to_do_list)


		

	def entry_added(self, frame, name, due_date, to_do_list): 
		#When entire entry is added but 

		#checks if days_needed entry is valid
		days_needed= self.entry_text_box_two.get()
		check_days_needed= helper_methods.check_days_needed_valid(days_needed)

		#if not valid
		if check_days_needed== False:
			try:
				self.not_valid_days_needed.winfo_exists()
			except:
				self.not_valid_days_needed= Label(frame, text= "Not valid, not a number", fg="red" )
				self.not_valid_days_needed.pack()

		#if valid
		else:

			#removes errors
			try:
				self.not_valid_days_needed.winfo_exists()
				self.not_valid_days_needed.pack_forget()
			except:
				pass

			#saves variable
			days_needed= int(days_needed)	

			#returns to homescreen 
			self.entry_text_box_two.pack_forget()
			self.days_needed_directions.pack_forget()
			self.entry_add_button_two.pack_forget()
			self.seperator_two.pack_forget()

			self.add_entry_button.pack()
			self.seperator_two.pack()


			self.now_title.pack()
			self.scrollbar.pack(side=RIGHT, fill=Y)
			self.now_list.pack(fill=BOTH, expand=1)
			self.now_list.pack()
			self.delete_now.pack()


			self.soon_title.pack()
			self.scrollbar_two.pack(side=RIGHT, fill=Y)
			self.soon_list.pack(fill=BOTH, expand=1)
			self.soon_list.pack()
			self.delete_soon.pack()


			self.eventually_title.pack()
			self.scrollbar_three.pack(side=RIGHT, fill=Y)
			self.eventually_list.pack(fill=BOTH, expand=1)
			self.eventually_list.pack()
			self.delete_eventually.pack()



			index_date= []

			#stores due_date in right format
			for i in range (0, len(due_date)):
				if due_date[i]=='/' or due_date[i]== '-':
					index_date.append(i)
			month= int (due_date[0:index_date[0]])
			day= int (due_date [index_date[0]+1:index_date[1]])
			year= int (due_date [index_date[1]+1:])
			due_date= str(month) + '/' + str(day) + '/' + str(year)


			to_do_list.append([name, due_date, days_needed])

			helper_methods.save_to_do(to_do_list)


			self.display_to_do_list(frame, to_do_list)

	def display_to_do_list(self, frame, to_do_list):
		#displays to_do_list

		to_do_list= helper_methods.append_days_left(to_do_list)

		organized_list= helper_methods.organize_list(to_do_list)

		#delete old display
		self.now_list.delete(0,END)
		self.soon_list.delete(0, END)
		self.eventually_list.delete(0,END)

		#used for delete method
		self.now_items= []
		self.soon_items= []
		self.eventually_items= []
		count_now=1
		count_soon=1
		count_eventually=1

		#Now display
		for i in organized_list[0]:
			if i[3]==5000:
				to_do_list.remove(i)
				continue
			self.now_items.append(i)
			formatting= helper_methods.formatting_display(i[0], i[3])
			if len (i[0])>=34:
				if i[3]<10:
					i[0]= i[0][0:30]+ "... "
				if i[3]>=10:
					i[0]=i[0][0:29]+ "... "
			self.now_list.insert (END, str(count_now)+"."+ i[0] +str(formatting[0]) +str(formatting[1]) )
			count_now+=1


		#Soon display
		for i in organized_list[1]:
			if i[3]==5000:
				to_do_list.remove(i)
				continue
			self.soon_items.append(i)
			formatting= helper_methods.formatting_display(i[0], i[3])
			if len (i[0])>=34:
				if i[3]<10:
					i[0]= i[0][0:29]+ "... "
				if i[3]>=10:
					i[0]=i[0][0:28]+ "... "
			self.soon_list.insert (END, str(count_soon)+ "." + i[0] +formatting[0] +formatting[1] )
			count_soon+=1

		#Eventually display
		for i in organized_list[2]:
			if i[3]==5000:
				to_do_list.remove(i)
				continue
			self.eventually_items.append(i)
			formatting= helper_methods.formatting_display(i[0], i[3])
			if len (i[0])>=34:
				if i[3]<10:
					i[0]= i[0][0:29]+ "... "
				if i[3]>=10:
					i[0]=i[0][0:28]+ "... "
			self.eventually_list.insert (END, str(count_eventually)+ "." + i[0] +formatting[0] +formatting[1] )
			count_eventually+=1






#Starts main loop
root= Tk()
GUI= GUI(root)
root.geometry('400x725')
root.mainloop()
