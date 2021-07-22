import os

path='processed' 
outfile = open('script2.sh', 'w')



i=1
for txt in os.listdir(path):
	print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = outfile)
	print('python3 ./gen_berts_to_file_aggiornato.py --bertPath ./latin_bert 	# --tokenizerPath ./latin.subword.encoder  	# -f '+path+'/'+txt +' -o token/'+txt)
	print('python3 ./gen_berts_to_file_aggiornato.py --bertPath ./latin_bert --tokenizerPath ./latin.subword.encoder  -f '+ path +'/' + txt +' -o token/' + txt, file = outfile )
	i=i+1
outfile.close()
