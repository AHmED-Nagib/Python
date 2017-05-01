import string
from string import Template
from datetime import datetime

print '0123456789'
print '0123456789'[len('0123456789') / 2:]
print '0123456789'[1:10:2]
print "1" * 10
mystring = "my string "
mystring2 = "a b c d e f g h i j | "
print mystring.capitalize()
print mystring.center(20, '*')
print mystring.index('s')
print mystring.find('s')
print mystring.isalnum()
print mystring.isalpha()
print mystring.isdigit()
print mystring.count(' ')
print mystring.title(),"title"
print mystring.replace(' ', '*')
print mystring.strip().replace(' ', '*')
print mystring2.join(['1   ', ''])
print string.ascii_letters,"ascii_letters"
print string.letters,"letters"
print string.ascii_uppercase
print string.hexdigits , "hexdigits"
print string.punctuation , "punctuation"
print string.printable
print Template('$who likes $what').safe_substitute(who='a')
print 'ahmed nagib mohmed'.capitalize(),"capitalize"
# print 'ahmed nagib mohmed'.capwords(),"capwords"
print string.capwords('ahmed nagib mohmed'),"capwords"
print string.expandtabs('ahmed nagib \nmohmed',5)
print  "abcda".find("a"),"find"
print  "abcda".find("ab"),"find"
print  "abcda".rfind("a"),"rfind"
print  "abcda".count("a"),"count"
print 'ahmed nagib mohmed'.split(" "),"split"
print 'ahmed \n nagib mohmed'.splitlines(),"splitlines"
print string.join('ahmed nagib mohmed'.split(" "),','),"split"
print 'ahmed nagib mohmed'.center(50,'a'),"center"
# print 'ahmed nagib mohmed'.center(width=50,fillchar='a'),"center"
print string.zfill('ahmed nagib mohmed', 50),"zfill"
print 'ahmed nagib mohmed'.endswith('mohmed'),"endswith"
#what is suffix ?
print 'ahmed nagib mohmed'.partition(' '),"partition"
print 'ahmed  '.ljust(10,'*'),"ljust"
print 'ahmed  '.rjust(10,'*'),"rjust"





