from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
supportedTags =  ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]


file = input("FileName please: Thank you ")
filename = open(file)


for line in filename:

	valid, tagg, remainder, arguments = "N", "", "", ""

	lineList = line.split()
	level_num = str(line[:1])
	for word in lineList:
		if(word in supportedTags):
			valid = "Y"
			tagg = word

	if(tagg == "INDI" or tagg == "FAM"):
		arguments = lineList[1]
	else:
		arguments = " ".join(lineList[2:])
	if(tagg == "NAME" and level_num != "1"):
		valid = "N"
	if(tagg == "DATE" and level_num != "2"):
		valid = "N"
	if(valid == "N"):
		tagg =  lineList[1]

	print("--> " + line)
	print("<-- " + level_num + "|" + tagg + "|" + valid + "|" + arguments)




