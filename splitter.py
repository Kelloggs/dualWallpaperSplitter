from PIL import Image
import sys
import getopt
import os

class ParameterException(Exception):
	'''
	Parameter Exception is thrown, if parameters could not be validated
	'''
	def __init__(self):
		pass

def printUsageInfo():
	print "Call from command line"
	print "python splitter.py -i [filename]"


def userInput(argv=None):
	files = []

	if argv is None:
		argv = sys.argv

	try:
		opts, _ = getopt.getopt(argv[1:], "hi:", ["help", "input"])
	except getopt.error, _:
		raise ParameterException

	for o, a in opts:
		#print usage info
		if o in ("-h", "--help"):
			printUsageInfo()
		if o in ("-i", "--input"):
			files.append(str(a))
			
	return files

def main():
	files = userInput()
	
	for file in files:

		im = Image.open(file)
		width, height = im.size

		left = im.crop((0, 0, int(0.5*width), height))
		right =  im.crop((int(0.5*width), 0, width, height))

		filename = file.split(os.extsep, 1)
		left.save(filename[0] + "_left.jpg")
		right.save(filename[0] + "right.jpg")

		print "Done"


if __name__ == '__main__':
	main()
