import re
import sys
import math

#Map, find, filter
#Reject, contains, pluck
#Max, min
	#Sortby ?
	
	#Indexby, countby
		
def map(function, my_list, key):
	new_list = []
	for element in my_list:
		new_list.append(function(element[key]))
	return new_list

def find(function, my_list, key):
	for element in my_list:
		if function(element[key]):
			return element

def filter(function, my_list, key):
	new_list = []
	for element in my_list:
		if function(element[key]):
			new_list.append(element)
	return new_list

def reject(function, my_list, key):
	new_list = []
	for element in my_list:
		if not function(element[key]):
			new_list.append(element)
	if len(new_list) != 0:
		return new_list


def contains(my_list, key, value):
	for element in my_list: 
		if element[key] == value:
			return 'Yes!'

def pluck(my_list, key):
	values = []
	for element in my_list:
		values.append(element[key])
	return values

def max_salary(my_list, key):
	max = my_list[0][key]
	for element in my_list:
		if element[key] > max:
			max = element[key]
	return max

def min_salary(my_list, key):
	min = my_list[0][key]
	for element in my_list:
		if element[key] < min:
			min = element[key]
	return min

#def group_by(function, my_list, key):
	#for element in my_list:
		#return(function(element[key]))
	
	#So.. aici m am cam blocat. In teorie, functia mea  tax_brackets e una care sorteaza income pe tax brackets. Adica 7 grupuri posibile. 
	#Doar ca in contextul group_by, nu stiu cum sa call it/ce si ce sa o fac sa returneze. Help?

def tax_brackets(income_list):
	first_bracket = []
	second_bracket = []
	third_bracket = []
	fourth_bracket = []
	fifth_bracket = []
	sixth_bracket = []
	seventh_bracket = []
	for element in income_list:
		if element >= 0 and element <= 9225:
			first_bracket.append(element)
		if element > 9225 and element <= 37450:
			second_bracket.append(element)
		if element > 37450 and element <= 90750:
			third_bracket.append(element)
		if element > 90750 and element <= 189300:
			fourth_bracket.append(element)
		if element > 189300 and element <= 411500:
			fifth_bracket.append(element)
		if element > 411500 and element <= 413200:
			sixth_bracket.append(element)
		if element > 413200:
			seventh_bracket.append(element)
	return('???')



def legal(age):
	return age >= 21

def dating_age(age):
	return int(age/2 + 7)

def main(argv):
	my_list = [{'Name': 'Ioana','Age':23,'Salary':60000},{'Name':'Cezar','Age':22,'Salary':120000}, {'Name': 'Roxana','Age':21.9,'Salary':70000}]
	#Calculate partner's minimum age for every person
	print map(dating_age, my_list, 'Age')
	#Find and return the first person over 21
	print 'First person found who is over 21: ' + str(find(legal, my_list, 'Age')['Name'])
	#Find and return all people over 21 
	#Question: aici as fi vrut sa returnez doar numele, ca mai sus, dar pentru ca sunt mai multi, nu pot sa dau ['Name'] la lista... thoughts?
	print 'People who are over 21: ' + str(filter(legal, my_list, 'Age'))
	#Find and return all people who are not over 21
	print 'People who are not over 21: ' + str(reject(legal, my_list, 'Age'))
	#Check if there are people who are exactly 21
	print 'People who are exactly 21: ' + str(contains(my_list, 'Age', 21))
	#Return list of all names
	print 'All names: ' + str(pluck(my_list, 'Name'))
	#Return the maximum salary in the given list of individuals
	print 'The maximum salary is: ' + str(max_salary(my_list, 'Salary'))
	#Return the minimum salary in the given list of individuals
	print 'The minimum salary is: ' + str(min_salary(my_list, 'Salary'))



if __name__ == "__main__":
	main(sys.argv[1:])

