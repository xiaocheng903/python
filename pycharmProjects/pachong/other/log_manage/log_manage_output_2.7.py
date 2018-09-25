# -*- coding: UTF-8 -*-
import codecs
import collections
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Log_manage(object):

	def __init__(self):
		self.file='debug.20170522.0.log'
		self.deep=5

	def list_sort(self,data):
		D=[]
		for d in data:
			d=d.encode('utf-8')
			D.append(d)
		return sorted(D,key=str.lower)

	def log_read(self,file,deep):
		with codecs.open(file,'r','gbk') as fp:
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

	def searching_log_input(self,line):
		if re.search(u'出参：',line):
			return True
		else:
			return False

	def format_str(self,str_dict):
		for i in str_dict:
			for j in range(len(str_dict[i])):
				str_dict[i][j]=self.list_sort(str_dict[i][j].split(", "))
		return str_dict

	def write_to_txt(self,str_dict):
		with codecs.open(u'出参--分析结果.txt','w','gbk') as fp:
			for i in str_dict:
				fp.write('\n'+i+u'出参'+'\n')
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

	def main(self):
		line_list=self.log_read(self.file,self.deep)
		line_dict=self.extracting_data(line_list)
		line_dict=self.format_first(line_dict)
		list_dict=self.format_str(line_dict)
		self.write_to_txt(list_dict)

if __name__=='__main__':
	obj_log=Log_manage()
	obj_log.main()
