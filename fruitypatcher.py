import argparse
import time
import binascii
import os
start = time.time()


#set up args for file
parser = argparse.ArgumentParser(description='the file location lmao')
parser.add_argument('fileloc', metavar='N', type=str, nargs='+',
                    help='file location')
args = parser.parse_args()
fileloc = args.fileloc[0]

if not '-fruitier.flp' in fileloc:
    betterpath = os.path.basename(os.path.normpath(fileloc.replace('.flp', ''))) + '-fruitier.flp'
else:
    betterpath = os.path.basename(os.path.normpath(fileloc))
#the "love bytes" (sometimes my cat gives me love bytes)

with open(fileloc,'rb') as f:
    #i hate this part
    hexd = f.read()
    thing = binascii.hexlify(hexd)
    thesix = binascii.unhexlify(thing[120:])

    mybytes = b'FLhd\x06\x00\x00\x00\x00\x00\x8d\x00`\x00FLdt\xe9\x8eJ\x00\xc7\x0c20.6.2.1549\x00\x9f\r\x06\x00\x00\x1c\x01%\x01\xc8\x02\x00\x00\x9c\x00\xf4\x01\x00C\r\x00\t\x01\x0b'
    final = mybytes + thesix
    if not '-fruitier.flp' in fileloc:
        x = open(fileloc.replace('.flp', '') + "-fruitier.flp",'wb')
    else:
         x = open(fileloc,'wb')
    print("Making file...")
    #ALMOST DONE ALMOST DONE LETS GO BABY
    print('Writing to',betterpath + '...' )
    x.write(final)
    end = time.time()
    #YES YES YES 
    print("Finished writing to", betterpath, 'in', str(round(end-start,3))[1:].replace('.',''), 'ms')
    x.close()
f.close()
