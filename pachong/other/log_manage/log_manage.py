# -*- coding : utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.filedialog
import collections
import re

class Log_manage(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def list_sort(self,data):
		return sorted(data,key=str.lower)

	def log_read(self,file,deep,parm):
		try:
			with open(file,'r',encoding='gbk') as fp:
				lines=fp.readlines()
				count=len(lines)
				i=-1
				j=1
				line_list=[]
				while abs(i)<=count:
					m=self.searching_log(lines[i],parm)
					if j<=deep:
						if m==True:
							line_list.append(lines[i])
							j+=1
					if j==(deep+1):
						return line_list
					i-=1
				return line_list
		except Exception as e:
			return False

	def searching_log(self,line,parms):
		if re.search(parms,line):
			return True
		else:
			return False

	def format_str_input(self,str_dict):
		for i in str_dict:
			str_dict[i]=self.list_sort(str_dict[i].split(","))
		return str_dict

	def format_str_output(self,str_dict):
		for i in str_dict:
			for j in range(len(str_dict[i])):
				str_dict[i][j]=self.list_sort(str_dict[i][j].split(", "))
		return str_dict

	def write_to_listbox_input(self,str_dict):
		self.listbox_filename.delete(0,END)
		for i in str_dict:
			self.listbox_filename.insert(END,'')
			self.listbox_filename.insert(END,i+"入参")
			for j in str_dict[i]:
				self.listbox_filename.insert(END,j.strip())

	def write_to_listbox_output(self,str_dict):
		self.listbox_filename.delete(0,END)
		for i in str_dict:
			self.listbox_filename.insert(END,'')
			self.listbox_filename.insert(END,i+'出参')
			for j in str_dict[i]:
				for l in j:
					self.listbox_filename.insert(END,l.strip())

	def write_to_listBox_all(self,str_dict_i,str_dict_o):
		self.listbox_filename.delete(0,END)
		for i in str_dict_i:
			self.listbox_filename.insert(END,'')
			self.listbox_filename.insert(END,i+"入参")
			for j in str_dict_i[i]:
				self.listbox_filename.insert(END,j.strip())
			self.listbox_filename.insert(END,'')
			self.listbox_filename.insert(END,i+'出参')
			for j in str_dict_o[i]:
				for l in j:
					self.listbox_filename.insert(END,l.strip())

	def extracting_data_input(self,str_list):
		L=collections.OrderedDict()
		i=0
		for l in str_list:
			a=str(i)+'_'+l[24:30]
			L[a]=l[34:-2]
			i+=1
		return L

	def extracting_data_output(self,str_list):
		L=collections.OrderedDict()
		i=0
		for l in str_list:
			a=str(i)+'_'+l[24:30]
			L[a]=l[36:-5]
			i+=1
		return L

	def format_first(self,line_list):
		for i in line_list:
			line_list[i]=line_list[i].split("}, {")
		return line_list

	def selectPath(self):
		path_=tkinter.filedialog.askopenfilename(filetypes=[("text file", "*.log")])
		path.set(path_)

	def get_screen_height(self):
		return self.winfo_screenheight()

	def get_screen_width(self):
		return self.winfo_screenwidth()

	def createWidgets(self):
		global path
		global var 
		var=IntVar()
		path=StringVar()
		data=['入参','出参','同时']
		for i in range(3):
			Radiobutton(self,variable =var,text = data[i],value = i).grid()

		self.hint_1_Label = Label(self,text='输入文件路径地址：')
		self.hint_1_Label.grid(row = 3, column = 0)
		self.nameInput=Entry(self,textvariable=path,width=40)
		self.nameInput.grid(row = 3, column = 1)
		self.pathButton=Button(self,text='选择路径',command=self.selectPath)
		self.pathButton.grid(row =3, column = 2)
		self.hint_2_Label = Label(self,text='输入分析深度：')
		self.hint_2_Label.grid(row = 4, column = 0)
		self.deepInput=Entry(self,width=40)
		self.deepInput.grid(row = 4, column = 1)
		self.alertButton=Button(self,text='确认',command=self.main,width=10)
		self.alertButton.grid(row = 5)
		self.listbox_filename = Listbox(self, width=80,height=30,selectmode=EXTENDED)
		self.listbox_filename.grid(row=6, column=0, columnspan=4, rowspan=4, padx=5, pady=5)


	def main(self):
		if var.get()==0:
			parm='入参：'
		else:
			if var.get()==1:
				parm='出参：'
			else:
				parm='同时'
		name=self.nameInput.get()
		try:
			deep=int(self.deepInput.get())
		except Exception as e:
			messagebox.showinfo('Message','请输入分析深度，整数值')
			return None
		line_list=self.log_read(name,deep,parm)

		if line_list!=False:
			if parm=='入参：':
				line_dict=self.extracting_data_input(line_list)
				list_dict=self.format_str_input(line_dict)
				self.write_to_listbox_input(list_dict)
			else:
				if parm=='出参：':
					line_dict=self.extracting_data_output(line_list)
					line_dict=self.format_first(line_dict)
					list_dict=self.format_str_output(line_dict)
					self.write_to_listbox_output(list_dict)
				else:
					line_list_i=self.log_read(name,deep,'入参')
					line_dict_i=self.extracting_data_input(line_list_i)
					list_dict_i=self.format_str_input(line_dict_i)

					line_list_o=self.log_read(name,deep,'出参')
					line_dict_o=self.extracting_data_output(line_list_o)
					line_dict_o=self.format_first(line_dict_o)
					list_dict_o=self.format_str_output(line_dict_o)
					self.write_to_listBox_all(list_dict_i,list_dict_o)
		else:
			messagebox.showinfo('Message','不能找到这个文件')
			return None

if __name__=='__main__':
	obj_log=Log_manage()
	obj_log.master.title('日志分析工具')
	obj_log.master.geometry('%dx%d+%d+0' % (obj_log.get_screen_width()/2,obj_log.get_screen_height(),obj_log.get_screen_width()/2))
	obj_log.mainloop()