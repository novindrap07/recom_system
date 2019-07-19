df.set_index('name', inplace=True)
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df['desc_clean'])
cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cos_sim