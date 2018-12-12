import sys
import io

def counter(fname):
	f=open(fname)
	id1=None
	id2=None
	
	for line in f:
		l=line.strip()
		counts = dict.fromkeys(l,0)
		for c in counts:
			# print "'" + c + "'"
			counts[c] = counts[c]+l.count(c)
	
	return id1, id2

def main(argv):
	if len(argv) != 2:
		print "No filename provided"
		quit(1)
	
	result = counter(argv[1])
	print str(result)
	print result[0] * result[1]


if __name__ == "__main__":
    main(sys.argv)
		
