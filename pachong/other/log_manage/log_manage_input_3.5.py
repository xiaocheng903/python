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
		#self.file='debug.20170522.0.log'
		#self.deep=10

	def list_sort(self,data):
		return sorted(data,key=str.lower)

	def log_read(self,file,deep):
		try:
			with open(file,'r',encoding='gbk') as fp:
				lines=fp.readlines()
				count=len(lines)
				i=-1
				j=1
				line_list=[]
				while abs(i)<=count:
					m=self.searching_log(lines[i])
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

	def searching_log(self,line):
		if re.search(r'入参：',line):
			return True
		else:
			return False

	def format_str(self,str_dict):
		for i in str_dict:
			str_dict[i]=self.list_sort(str_dict[i].split(","))
		return str_dict

	def write_to_txt(self,str_dict):
		with open('分析结果.txt','w',encoding='gbk') as fp:
			for i in str_dict:
				fp.write('\n'+i+"入参"+'\n')
				for j in str_dict[i]:
					fp.write(j.strip()+'\n')

	def write_to_listbox(self,str_dict):
		self.listbox_filename.delete(0,END)
		for i in str_dict:
			self.listbox_filename.insert(END,'\n'+i+"入参"+'\n')
			for j in str_dict[i]:
				self.listbox_filename.insert(END,j.strip()+'\n')

	def extracting_data(self,str_list):
		L=collections.OrderedDict()
		i=0
		for l in str_list:
			a=str(i)+'_'+l[24:30]
			L[a]=l[34:-2]
			i+=1
		return L

	def selectPath(self):
		path_=tkinter.filedialog.askopenfilename(filetypes=[("text file", "*.log")])
		path.set(path_)

	def createWidgets(self):
		global path
		global var 
		var=IntVar()
		path=StringVar()
		data=['入参','出参']
		for i in range(2):
			Radiobutton(self,variable =var,text = data[i],value = i).grid()

		self.hint_1_Label = Label(self,text='输入文件路径地址：')
		self.hint_1_Label.grid(row = 2, column = 0)
		self.nameInput=Entry(self,textvariable=path,width=40)
		self.nameInput.grid(row = 2, column = 1)
		self.pathButton=Button(self,text='选择路径',command=self.selectPath)
		self.pathButton.grid(row =2, column = 2)
		self.hint_2_Label = Label(self,text='输入分析深度：')
		self.hint_2_Label.grid(row = 3, column = 0)
		self.deepInput=Entry(self,width=40)
		self.deepInput.grid(row = 3, column = 1)
		self.alertButton=Button(self,text='确认',command=self.main,width=10)
		self.alertButton.grid(row = 4)
		self.listbox_filename = Listbox(self, width=80,height=15)
		self.listbox_filename.grid(row=5, column=0, columnspan=4, rowspan=4, padx=5, pady=5)


	def main(self):
		name=self.nameInput.get()
		try:
			deep=int(self.deepInput.get())
			line_list=self.log_read(name,deep)
		except Exception as e:
			messagebox.showinfo('Message','请输入分析深度，整数值')
			return None
		if line_list!=False:
			line_dict=self.extracting_data(line_list)
			list_dict=self.format_str(line_dict)
			self.write_to_listbox(list_dict)
		else:
			messagebox.showinfo('Message','不能找到这个文件')

if __name__=='__main__':
	obj_log=Log_manage()
	obj_log.master.title('日志分析工具')
	obj_log.master.geometry('600x500+400+100')
	obj_log.mainloop()
