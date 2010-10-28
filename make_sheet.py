import sys
reload(sys)
sys.setdefaultencoding('utf-8')


for j in range(0x00, 0x10): 
    for i in range(0x220,0x230): 
        pass # print unichr(0x10*i+j),

print "&", 
print "&".join("{i:3X}".format(i=i) for i in range(0x220,0x230))
print "\\\\"
print "\\hline"


for j in range(0x00, 0x10): 
    print "{j:1X}&".format(j=j)
    print "&".join( "\\utfchar{{{utf}}}{{{cp:4x}}}".format(cp=0x10*i+j,utf=unichr(0x10*i+j)) for i in range(0x220,0x230))
    print "\\\\"
    print "\\hline"


