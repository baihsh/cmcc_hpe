#!/usr/bin/python
#Filename: objvar.py

class Person:
	'''Represents a person.'''
	population = 0 
	def __init__(self,name):
		self.myname = name
		print '(Initializing %s' % self.myname

		# When this person is created,he/she
		# adds to the population
		Person.population += 1
	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' % self.myname
		Person.population -= 1
		
		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d people left.' % Person.population

	def sayHi(self):
		'''Greeting by person.
		Really, that's all it does.'''
		print 'Hi, my name is %s.' % self.myname	
	
	def howMany(self):
		''' prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population

baihsh = Person('Baihsh')
baihsh.sayHi()
baihsh.howMany()

erpang = Person('Erpang')
erpang.sayHi()
erpang.howMany()

