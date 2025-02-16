#2021-12-23
#Saw a question on /r/learnpython and decided to give it a go.

def sortPos(list):

	positiveList = []
	negativeList = []
	
	for i in list:
		if i < 0:
			negativeList.append(i)
		else:
			positiveList.append(i)
			
	positiveList.sort()
		
	return positiveList + negativeList
assert sortPos([1, -2, 0, 4, 3, -5]) == [0, 1, 3, 4, -2, -5]
