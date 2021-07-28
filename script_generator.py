#SCRIPT GENERATOR

import os
path='corpus2' 
bertpath='/home/wsojka00/Desktop/latin_bert' 


pickle='pickle'
if not os.path.exists(pickle):
  os.mkdir(pickle)

scriptfile = open('script.sh', 'w')

i=1
for txt in os.listdir(path):
	print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = scriptfile)
	
	
	
	print('python3 ./gen_file2.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f '+ path +'/' + txt +' -o ' +pickle +'/' + txt, file = scriptfile )
	
	i=i+1

scriptfile.close()  


