from db_connection import *
import datetime
import pandas
from similarity import *

def get_ranked_posts_from_tokens(user_id, tokens):
    #TODO
    pass

def get_tokens_from_posts(user_id, dataframe):
    #TODO
    pass

def metrics_per_posts(user_id):
    
    conn = db_connect()
    
    delta_time = (datetime.datetime.today() - datetime.timedelta(7)).strftime('%Y-%m-%d')    
    response = db_consume(conn, f"SELECT * FROM quero_collab.posts where date(created_at) >= '{delta_time}' and user_id != {user_id}")
    #response_lastpost = db_consume(conn, f"SELECT ")
    postsDF = pandas.DataFrame(response, columns=['post_id', 'text', 'user_id', 'created_at', 'updated_at'])
    
    print(postsDF)
    print("get model")
    model_post = get_model_posts(postsDF['text'])
    print("get sims")
    metricsDF = get_posts_sims(model_post, postsDF)
    print(metricsDF) 
        
    conn.close()
    








def metrics_per_interests(user_id):
    conn = db_connect()
    
    query_interests = f"""select interest, user_id
                        from quero_collab.profiles 
                        where user_id != {user_id};"""
    
    response = db_consume(conn, query_interests)
    profiles_df = pandas.DataFrame(response, columns=['interest', 'user_id'])

    
    print("get model")
    model_post = get_model_interests(profiles_df['interest'])
    print("get sims")
    metricsDF = get_users_sims(model_post, profiles_df)
    print(metricsDF) 
        
    conn.close()






# print("get model")
# model_post = get_model(postsDF['text_data'])
# print("get sims")
# metricsDF = get_posts_sims(model_post, postsDF)
# print(metricsDF)

metrics_per_posts(1)
#metrics_per_interests(1)

