def recommendations(name, cos_sim = cos_sim):
    
    recommended_hotel = []
    
    # Mengambil nama hotel berdasarkan variabel indicies
    idx = indices[indices == name].index[0]

    # Membuat series berdasarkan skor kesamaan
    score_series = pd.Series(cos_sim[idx]).sort_values(ascending = False)

    # mengambil index dan dibuat 10 baris rekomendasi terbaik
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    for i in top_10_indexes:
        recommended_hotel.append(list(df.index)[i])
        
    return recommended_hotel