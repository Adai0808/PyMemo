# -*- coding: gbk -*-
class Record(object):
	'''
	��¼��
	���ݼ�¼�����ͣ�������¼������ת��¼�������п�Ƭ������
	����ǻ�����¼����ôֻ����1�ſ�Ƭ
	�������ת��¼����ô����2�ſ�Ƭ�������ſ�Ƭ������ǡ���෴�����������Ŷ����Ŀ�Ƭ
	'''
	def __init__(self, cardId, ques, ans, type, addTime, alertTime, libId, grade=0, ):
		self.cardId = cardId
		self.question = ques
		self.answer =ans
		self.type =type
		self.addTime =addTime
		self.alertTime = alertTime
		self.libId = libId
		self.grade = grade

	# get/set ����
	def getId(self):
		return self.cardId
	def getQues(self):
		return self.question
	def setQues(self, content):
		self.question = content
	def getAns(self):
		return self.answer
	def setAns(self, content):
		self.answer = content
	def getType(self):
		return self.type
	def setType(self, typeFlag):
		self.type = typeFlag
	def getAddTime(self):
		return self.addTime
	def getAlertTime(self):
		return self.alertTime
	def setAlertTime(self, time):
		self.alertTime = time
	def getLibId(self):
		return self.libId
	def setLibId(self, id):
		self.libId = id
	def getGrade(self):
		return self.grade
	def setGrade(self, grade):
		self.grade = grade
