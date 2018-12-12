import sys
import io

def counter(fname):
	f=open(fname)
	num_twos=0
	num_threes=0
	
	for line in f:
		l=line.strip()
		counts = dict.fromkeys(l,0)
		for c in counts:
			# print "'" + c + "'"
			counts[c] = counts[c]+l.count(c)
		print "Generating counts"
		twos=sum(1 for x in counts.values() if x == 2) > 0
		threes=sum(1 for x in counts.values() if x == 3) > 0
		print "Twos:" + str(twos) + ", Threes:" + str(threes)
		if twos: num_twos += 1
		if threes: num_threes += 1
		print "Num Twos:" + str(num_twos) + ", Num Threes:" + str(num_threes)
	
	return num_twos, num_threes

def main(argv):
	if len(argv) != 2:
		print "No filename provided"
		quit(1)
	
	result = counter(argv[1])
	print str(result)
	print result[0] * result[1]


if __name__ == "__main__":
    main(sys.argv)
		