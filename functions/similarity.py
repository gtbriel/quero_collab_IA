from datetime import date
import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from text_lib import preprocessing



def get_post_most_sims(model, row, post_ids):
    tokens = preprocessing(row['text'])
    vec = model.infer_vector(tokens) 
    sims = np.array(model.docvecs.most_similar([vec]))
    idx = sims[:,0].astype(int)
    #rows = df[df.index.isin(idx)]
    #print(rows)
    #most_sims = np.array(list(rows['post_id']))
    most_sims = np.array(post_ids)[idx]
    return [row['post_id'], most_sims, date.today().strftime("%d/%m/%Y")]

def get_user_most_sims(model, row, ids):
    tokens = [preprocessing(text) for text in row['interest']] #preprocessing(row['interest'])
    print(row)
    print(tokens)
    vec = [model.infer_vector(token) for token in tokens]
    sims = []
    for v in vec:
        sims.extend(model.docvecs.most_similar([v])[:4])

    sims = np.array(sims)
    idx = sims[:,0].astype(int)
    print('sims')
    print(idx)
    print(ids, )
    print(ids(idx))
    most_sims = np.array(ids(idx))
    return [id, most_sims]    

def get_model_posts(posts):
    #d2v = Doc2Vec.load('model/d2v_pretreined')
    d2v = Doc2Vec(dm=0, vector_size=50, window=2, min_count=1, sample=6e-5, alpha=0.03, min_alpha=0.0007)
    keywords = list(map(preprocessing, posts))
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)    
    return d2v

def get_model_interests(interests):
    #d2v = Doc2Vec.load('model/d2v_pretreined')
    d2v = Doc2Vec(dm=0, vector_size=50, window=2, min_count=1, sample=6e-5, alpha=0.03, min_alpha=0.0007)
    keywords = [preprocessing(text) for interest in interests for text in interest]
    tagged_posts = [TaggedDocument(doc, [i]) for i, doc in enumerate(keywords)] 
    d2v.build_vocab(documents=tagged_posts)
    total = d2v.corpus_count
    d2v.train(tagged_posts, total_examples=total, epochs=100)    
    return d2v

def get_posts_sims(model, df):
    post_ids = list(df['post_id'])
    print(post_ids)
    table_posts = []
    for _ , row in df.iterrows():
        table_posts.append(get_post_most_sims(model, row, post_ids))

    table_posts_df = pd.DataFrame(data=table_posts, columns=['post_id', 'most_ranked', 'date'])
    return table_posts_df


def get_users_sims(model, df):
    users_id = np.array(list(df['user_id']))
    print('users:', users_id)
    table_users = []
    for _ , row in df.iterrows():
        table_users.append(get_user_most_sims(model, row, users_id))

    table_users_df = pd.DataFrame(data=table_users, columns=['user_id', 'most_similaritys'])
    return table_users_df


    


    
