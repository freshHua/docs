import re;

sRegex =re.compile( "^Node\\s+(\\d+),.*. type\\s+(\\w+)\\s+([\s\d]+?)\s*$");
matcher = sRegex.match("Node    0, zone    DMA32, type      Movable   1862   1665   1697    885    344     99     42     15      4      3      2");
if  matcher:
	for group in matcher.groups():
	    print group

