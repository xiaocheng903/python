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
		self.deep=2

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
				m=self.searching_log(lines[i])
				if j<=deep:
					if m==True:
						line_list.append(lines[i])
						j+=1
				if j==(deep+1):
					return line_list
				i-=1
			return line_list

	def searching_log(self,line):
		if re.search(u'入参：',line):
			return True
		else:
			return False

	def format_str(self,str_dict):
		for i in str_dict:
			str_dict[i]=self.list_sort(str_dict[i].split(","))
		return str_dict

	def write_to_txt(self,str_dict):
		with codecs.open(u'分析结果.txt','w','gbk') as fp:
			for i in str_dict:
				fp.write('\n'+i+u'入参'+'\n')
				for j in str_dict[i]:
					fp.write(j.strip()+'\n')

	def extracting_data(self,str_list):
		L=collections.OrderedDict()
		i=0
		for l in str_list:
			a=str(i)+'_'+l[24:30]
			L[a]=l[34:-3]
			i+=1
		return L

	def main(self):
		line_list=self.log_read(self.file,self.deep)
		line_dict=self.extracting_data(line_list)
		list_dict=self.format_str(line_dict)
		self.write_to_txt(list_dict)

if __name__=='__main__':
	obj_log=Log_manage()
	obj_log.main()
