import re
file=open('simpsons_phone_book.txt','r')
for line in file:
 if re.search(r'^J\w*\s*(Neu)',line):
  print(line)
file.close()