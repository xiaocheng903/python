# -*- coding : utf-8 -*-

from tkinter import * 
import tkinter.messagebox as messagebox
import tkinter.filedialog
import collections
import re

class Reformat(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def collect_data_from_box(self):
		return self.data_text.get("0.0", "end") 

	def format_to_dict(self,data):
		L=collections.OrderedDict()
		data_1=data.split(',')
		if len(data_1)==1:
			data_1=self.list_sort(data.split('\n'))
		else:
			data_1=self.list_sort(data.split(','))
		n=0
		for i in data_1:
			if len(i.split('\n'))>1:
				data_1[n]=i.split('\n')[0]
			n+=1
		for i in data_1:
			l=i.split('=',1)
			a=l[0]
			if len(l)==1:
				pass
			else:
				L[a]=l[1]
		return L

	def write_to_listbox_all(self,data):
		self.data_write.delete("0.0", "end")
		for i in data:
			self.data_write.insert(END,"\""+i+"\""+':'+"\""+data[i]+"\""+','+'\n')
		self.data_write.delete('0.0','1.0')

	def write_to_listbox_only_key(self,data):
		self.data_write.delete("0.0","end")
		for i in data:
			self.data_write.insert(END,"\""+i+"\""+':'+"\""+"\""+','+'\n')
		self.data_write.delete('0.0','1.0')

	def list_sort(self,data):
		return sorted(data,key=str.lower)

	def get_screen_height(self):
		return self.winfo_screenheight()

	def get_screen_width(self):
		return self.winfo_screenwidth()

	def createWidgets(self):
		global var 
		var=IntVar()
		data=['只转换key','全部转换']
		self.data_text=Text(self,width=30)
		self.data_text.grid(row=0,column=0,rowspan=3, sticky=W)
		for i in range(2):
			Radiobutton(self,variable =var,text = data[i],value = i).grid(row=i, column=1)
		self.data_write=Text(self,width=30)
		self.data_write.grid(row=0,column=2,rowspan=3, sticky=E)
		self.alertButton=Button(self,text='确认',command=self.main,width=10)
		self.alertButton.grid(row=2,column=1)
	def main(self):
		data=self.collect_data_from_box()
		data=''.join([x for x in data if x!=' '])
		dict_data=self.format_to_dict(data)
		if var.get()==1:
			self.write_to_listbox_all(dict_data)
		else:
			self.write_to_listbox_only_key(dict_data)


if __name__=='__main__':
	obj_format=Reformat()
	obj_format.master.title('格式转换工具')
	obj_format.master.geometry("%dx%d+%d+%d" % (obj_format.get_screen_width()/2,obj_format.get_screen_height()/2,obj_format.get_screen_width()/4,obj_format.get_screen_height()/4))	
	obj_format.mainloop()