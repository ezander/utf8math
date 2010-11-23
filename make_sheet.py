import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def make_sheet( name, cname, u1, u2 ):
    u2=u2+1;
    
    f=open(name+".inc","w")
    f.write( "\\begin{{tabular}}{{|l|*{{{num}}}{{c|}}}}\n".format(num=u2-u1) )
    f.write( "\\hline\n" )

    f.write( "&" )
    f.write( "&".join("\\textbf{{{i:03X}}}".format(i=i) for i in range(u1,u2)) )
    f.write( "\\\\\n")
    f.write( "\\hline\n")


    for j in range(0x00, 0x10): 
        f.write( "\\textbf{{{j:1X}}}&\n".format(j=j))
        f.write( "&".join( "\\utfchar{{{utf}}}{{{cp:4x}}}"\
                               .format(cp=0x10*i+j,utf=unichr(0x10*i+j)) \
                               for i in range(u1,u2)) )
        f.write( "\\\\\n" )
        f.write( "\\hline\n" )
    f.write( "\\end{tabular}\n" )
    f.close()

make_sheet( "u0370", "greek", 0x037, 0x03F );
#make_sheet( "u2190", "arrows", 0x219, 0x21F );
make_sheet( "u2190", "arrows", 0x219, 0x21A );
make_sheet( "u2200", "math ops", 0x220, 0x22F );


