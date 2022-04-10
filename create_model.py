from gensim.models.doc2vec import Doc2Vec, TaggedDocument


d2v = Doc2Vec(dm=0, vector_size=50, window=2, min_count=1, workers=multiprocessing.cpu_count(), 
              sample=6e-5, alpha=0.03, min_alpha=0.0007)

text = ['']
posts_tokens
tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(posts_tokens)] #matriz de documentos com as tags, cada linha é um vetor dos tokens de cada doc


#nilc = KeyedVectors.load_word2vec_format('/content/drive/My Drive/hackathon2022/skip_s50.txt')
#tagged_nilc = [TaggedDocument(w, [i]) for i, w in enumerate(nilc.vocab.keys())]


d2v.build_vocab(documents=tagged_posts)
total = d2v.corpus_count
#vocab = [TaggedDocument(w, [i]) for i, w in enumerate(nilc.vocab.keys())]
#d2v.build_vocab(vocab, update=True)

d2v.train(tagged_posts, total_examples=total, epochs=100)
d2v.save('../d2v_pretreined')


