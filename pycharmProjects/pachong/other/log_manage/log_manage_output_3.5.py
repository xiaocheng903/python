# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
import codecs
import collections
import re

class Log_manage(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def list_sort(self,data):
		return sorted(data,key=str.lower)

	def log_read(self,file,deep):
		try:
			with codecs.open(file,'r',encoding='gbk') as fp:
				lines=fp.readlines()
				count=len(lines)
				i=-1
				j=1
				line_list=[]
				while abs(i)<=count:
					m=self.searching_log_input(lines[i])
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

	def searching_log_input(self,line):
		if re.search(r'出参：',line):
			return True
		else:
			return False

	def format_str(self,str_dict):
		for i in str_dict:
			for j in range(len(str_dict[i])):
				str_dict[i][j]=self.list_sort(str_dict[i][j].split(", "))
		return str_dict

	def write_to_txt(self,str_dict):
		with codecs.open('出参--分析结果.txt','w',encoding='gbk') as fp:
			for i in str_dict:
				fp.write('\n'+i+'出参'+'\n')
				for j in str_dict[i]:
					for l in j:
						fp.write(l.strip()+'\n')
		return 

	def extracting_data(self,str_list):
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

	def createWidgets(self):
		self.hint_1_Label = Label(self,text='输入文件路径地址：')
		self.hint_1_Label.pack()
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.hint_2_Label = Label(self,text='输入分析深度：')
		self.hint_2_Label.pack()
		self.deepInput=Entry(self)
		self.deepInput.pack()
		self.alertButton=Button(self,text='Hello',command=self.main)
		self.alertButton.pack()

	def main(self):
		name=self.nameInput.get()
		deep=int(self.deepInput.get())
		line_list=self.log_read(name,deep)
		if line_list!=False:
			line_dict=self.extracting_data(line_list)
			line_dict=self.format_first(line_dict)
			list_dict=self.format_str(line_dict)
			self.write_to_txt(list_dict)
		else:
			messagebox.showinfo('Message','the file is not found')

if __name__=='__main__':
	obj_log=Log_manage()
	obj_log.master.title('hello world')
	obj_log.master.geometry('500x300+500+200')
	obj_log.mainloop()
