import os
path='library_reduced'
#path='library_super_reduced'
f = open('script.sh', 'w')

authors=[]
for folder in os.listdir(path):
  authors.append(folder)


for author in authors:
    for file in os.listdir(path+'/'+author):
        #print('python3 ./gen_berts_to_file_aggiornato.py --bertPath ./latin_bert --tokenizerPath ./latin.subword.encoder  -f '+path+'/'+author+'/'+file +' -o token/'+file)
        print('python3 ./gen_berts_to_file_aggiornato.py --bertPath ./latin_bert --tokenizerPath ./latin.subword.encoder  -f '+path+'/'+author+'/'+file +' -o token/'+file, file = f)



f.close()
