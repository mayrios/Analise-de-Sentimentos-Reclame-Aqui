import nltk
from nltk.corpus import stopwords
import string
import csv
import re
import unicodedata


arquivo = open('reclamacoes_claro.csv', encoding='utf-8')
texto = csv.reader(arquivo)


def processa_texto(text):
	regex = re.compile('[%s]' % re.escape(string.punctuation))

	vetor_texto = []

	words = text.split()

	for row in words:
		new_token = regex.sub(u'', row)
		if not new_token == u'':
			vetor_texto.append(new_token)

	stopwords = nltk.corpus.stopwords.words('portuguese')
	conteudo = [w for w in vetor_texto if w.lower().strip() not in stopwords]

	clean_text = []

	for palavra in conteudo:

		nfkd = unicodedata.normalize('NFKD', palavra)
		palavraSemAcento = u''.join([c for c in nfkd if not unicodedata.combining(c)])
		q = re.sub('[^a-zA-Z0-9 \\\]',' ',palavraSemAcento)

		clean_text.append(q.lower().strip())

	tokens = [t for t in clean_text if len(t)>2 and not t.isdigit()]

	frase_tratada = ' '.join(tokens)
	return frase_tratada


for x in texto:
	texto_tratado = processa_texto(x[0])
	arquivo_tratado = open('reclamacoes_claro_tratado.csv', 'a')
	arquivo_tratado.write(texto_tratado + '\n' )
	print(texto_tratado + ';')
	arquivo_tratado.close()

#nltk.download()


