#Justin Cai, jc5pz
import re
nospace = re.compile('\S+')
quotation = re.compile('"\S[^"]+\S"')
twonum = re.compile('(-?\d+\.?\d*)[,\s]{1,2}(-?\d+\.?\d*)')
