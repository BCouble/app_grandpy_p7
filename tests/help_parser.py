test = "Bonjour, je suis un texte d'exemple pour le cours d'Openclassrooms. Soyez attentifs à ce cours !"

nltk.word_tokenize(test)

tokenizer = nltk.RegexpTokenizer(r'\w+')
tokenizer.tokenize("Bonjour, je suis un texte d'exemple pour le cours d'Openclassrooms. Soyez attentifs à ce cours !")


tokenizer = nltk.RegexpTokenizer(r'\w+')

def freq_stats_corpora():
corpora = defaultdict(list)

# Création d'un corpus de tokens par artiste
for artiste,sentence_id in artistes.iteritems():
for sentence_id in sentence_id:
corpora[artiste] += tokenizer.tokenize(db[sentence_id]['text'].decode('utf-8').lower())

stats, freq = dict(), dict()

for k, v in corpora.iteritems():
freq[k] = fq = nltk.FreqDist(v)
stats[k] = {'total': len(v)}
return (freq, stats, corpora)

# Récupération des comptages
freq, stats, corpora = freq_stats_corpora()
df = pd.DataFrame.from_dict(stats, orient='index')

# Affichage des fréquences
df.sort(columns='total', ascending=False)
df.plot(kind='bar', color="#f56900", title='Top 50 Rappeurs par nombre de mots')


def freq_stats_corpora():
    corpora = defaultdict(list)


for artiste, sentence_ids in artistes.iteritems():
    for sentence_id in sentence_ids:
        corpora[artiste] += tokenizer.tokenize(db[sentence_id]['text'].decode('utf-8').lower())

    stats, freq = dict(), dict()

for k, v in corpora.iteritems():
    freq[k] = fq = nltk.FreqDist(v)
    stats[k] = {'total': len(v), 'unique': len(fq.keys())}

return (freq, stats, corpora)