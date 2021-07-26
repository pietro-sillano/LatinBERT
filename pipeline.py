import os
from cltk.sentence.lat import LatinPunktSentenceTokenizer as SentenceTokenizer
from cltk.tokenizers.lat.lat import LatinWordTokenizer as WordTokenizer

#questa 'e la cartella  dove si salvano i preprocess
path='processed' 
if not os.path.exists(path):
  os.mkdir(path)

#questa 'e la cartella  dove si salvano i token
token='token'
if not os.path.exists(token):
  os.mkdir(token)


#source='library_super_reduced'
source='library_reduced'
#source='latin_library_text' 


max_docs=10


authors=[]
for folder in os.listdir(source):
    authors.append(folder)
print(authors)




#le chiavi sono gli autori, scrivo su file le prime 100 sentences
max_sents=200

splitter = SentenceTokenizer()
for author in authors:
	j=1
	for file in os.listdir(source+'/'+author):
		if(j<=max_docs):
		    f = open(source+'/'+author+'/'+file, "r")
		    fout=open(path+'/'+file, 'w')

		    text=f.read()
		    sentences = splitter.tokenize(text)
		    print(author,file,len(sentences))
		    sentences=sentences[:max_sents]
		    fout.writelines(["%s\n" % sentence  for sentence in sentences])
		    fout.close()
		    j=j+1




#SCRIPT GENERATOR
scriptfile = open('script.sh', 'w')

i=1
for txt in os.listdir(path):
	print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = scriptfile)
	
	
	#print('python3 ./gen_file2.py --bertPath ./latin_bert --tokenizerPath ./latin.subword.encoder  -f '+ path +'/' + txt +' -o token/' + txt, file = scriptfile )
	
	print('python3 ./gen_file2.py --bertPath ./latin_bert --tokenizerPath ./latin.subword.encoder  -f '+ path +'/' + txt +' -o ' + txt, file = scriptfile )
	
	i=i+1

scriptfile.close()  
