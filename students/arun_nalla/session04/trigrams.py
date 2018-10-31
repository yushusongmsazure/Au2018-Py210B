with open("sherlock_small.txt") as f:
    words = f.read().strip().replace("\n", " ").split()

def trigram_dict(words):
	trilist = {}
	for i in range(len(words)-2):
    
		a = ",".join(words[i:i+2])
    
		b = words[i+2]    
		if a not in trilist.keys():
        
			trilist[a] = [b]
    
		else:
        
			trilist[a].append(b)

	return trilist

