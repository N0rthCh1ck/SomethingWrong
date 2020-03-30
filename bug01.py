# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: me
'''
	说明 某创新创业平台信息泄露检测小工具
	用法 
		修改mian()的 phone_num
		run
		等待结果
	补充
		懒，没有实现写到文件，后续可以考虑写到csv
		隐私信息涉嫌法律问题(懒)，未实现下载功能，仅提供检测
		涉嫌隐私相关的内容已经删除
	免责声明
		请勿用作非法用途，产生相关问题与作者无关
'''
import requests
import itertools as its
import threading

# 多线程
class PocThread(threading.Thread):

	def __init__(self, Thread_ID):
		threading.Thread.__init__(self)
		self.Thread_ID = Thread_ID
	def run(self):
		for phone_num in Phone_nums[self.Thread_ID]:
			spider(phone_num)

# 爬虫
def spider(phone_num):
	url = base_url + phone_num + ".jpeg"
	response = requests.get(url)
	# 长度为306说明不存在，此处通过响应头返回值判断是否存在
	if response.headers["Content-Length"] != '306':
		print(phone_num + "存在")

# 迭代器生成手机号字典
def genarator(prev_str, repeat):
	words = "0123456789"
	dic = its.product(words, repeat=repeat)
	for j in dic:
		num = prev_str + "".join(j)
		phone.append(num)

phone = []
Phone_nums = [[]]*10

base_url = "不给"
def main():
	# num：自定义号段
	phone_num = "不给"
	print("***开始检测 "+phone_num+" 号段，请稍等***")
	if len(phone_num) > 11:
		print("手机号格式输入错误")
		return
	elif len(phone_num) == 11:
		spider(phone_num)
	else:
		repeat = 11 - len(phone_num)
		if repeat != 0:
			genarator(phone_num,repeat)
			for i in range(10):
				start = i * len(phone)//10
				end = (i+1) * len(phone)//10
				Phone_nums[i] = phone[start:end]
		for i in range(10):
			try:
				PocThread(i).start()
			except Exception as e:
				print("error")
main()
