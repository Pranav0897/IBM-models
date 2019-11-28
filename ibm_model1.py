from collections import Counter

en_corpus=[]
es_corpus=[]
with open('corpus.en') as f1:
    while True:
        en = f1.readline()
        if en =='' or en is None:
            break
        en_corpus.append(['NULL']+[w for w in en.strip().split()])
        
with open('corpus.es') as f2:
    while True:
        es = f2.readline()
        if es=='' or es is None:
            break
        es_corpus.append([w for w in es.strip().split()])

print("Created corpus.\n")
en_vocab=Counter([w for s in en_corpus for w in s])
es_vocab=Counter([w for s in es_corpus for w in s])
print("Created vocabulary.\n")
t=Counter()
for en_sent in en_corpus:
    for es_sent in es_corpus:
        for e in en_sent:
            for f in es_sent:
                t[(f,e)]=1/en_vocab[e]

print("Initialised t.\n")
n_iter=5
for iterno in range(n_iter):
    print("Iteration #{}".format(iterno))
    c=Counter()
    for k in range(len(en_corpus)):
        for i in range(len(es_corpus[k])):
            sum1=0
            for w in en_corpus[k]:
                sum1+=t[(es_corpus[k][i],w)]
            sum1+=t[(es_corpus[k][i],'NULL')]
            if sum1 == 0:
                print(es_corpus[k],en_corpus[k])
            for j in range(len(en_corpus[k])):
                delta_kij= t[(es_corpus[k][i],en_corpus[k][j])] / sum1
                c[(en_corpus[k][j],es_corpus[k][i])]+= delta_kij
                c[en_corpus[k][j]] += delta_kij
                c[(j,i,len(en_corpus[k]),len(es_corpus[k]))] += delta_kij
                c[(i,len(en_corpus[k]),len(es_corpus[k]))] += delta_kij
            if sum1!=0:
                delta_kij= t[(es_corpus[k][i],'NULL')] / sum1
                c[('NULL',es_corpus[k][i])]+= delta_kij
                c['NULL'] += delta_kij
                c[(-1,i,len(en_corpus[k]),len(es_corpus[k]))] += delta_kij
                c[(i,len(en_corpus[k]),len(es_corpus[k]))] += delta_kij

    for k in range(len(en_corpus)):
        for f in es_corpus[k]:
            for e in en_corpus[k]:
                t[(f,e)]=c[(e,f)]/c[e]
            t[(f,'NULL')]=c[(f,'NULL')]/c['NULL']
print("Done with EM iterations. Storing data in JSON file.\n")
import json
with open('t.json', 'w') as fp:
    json.dump(t, fp)

print("Completed.")