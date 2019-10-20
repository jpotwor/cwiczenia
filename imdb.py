import pandas as pd


df = pd.read_csv('movie_metadata.csv', index_col='movie_title')
# print(df.isnull().sum())
df.drop_duplicates(inplace=True)
# to samo
df = df.drop_duplicates()
# print(df.shape)

# print(df.columns)

budget = df['budget'].dropna()
# print(budget.mean())
#
# print(df['genres'].value_counts().head(20))


ridley_movies = df[df['director_name'] == 'Ridley Scott']
# print(ridley_movies.head())

print(df.columns)
print(df['actor_1_facebook_likes'].max())

likes_mean = df['actor_1_facebook_likes'].mean()
most_facebook_likes_actors = df[df['actor_1_facebook_likes'] > likes_mean]
print(most_facebook_likes_actors['actor_1_facebook_likes'].count())



most_liked_actors_long_movies = df[
    (df['actor_1_facebook_likes'] > likes_mean) &
    (df['duration'] > 60)
]
print(most_liked_actors_long_movies['actor_1_facebook_likes'].count())

# movies between 2005, 2010 with imdb_score (without nans, 0) more than it's median
median = df['imdb_score'].dropna().median()
df_movies = df[
    (df['title_year'] >= 2005) &
    (df['title_year'] <= 2010) &
    (df['imdb_score'] > median)
]

columns = ['imdb_score', 'title_year']
print(df_movies[columns])

print(df_movies.groupby('title_year').count()['imdb_score'])


def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"


# count good and bad movies
rated_movies = df_movies['imdb_score'].apply(rating_function)
print(rated_movies.value_counts())

# get title of the max rated movie
max_rated_movie_index = df_movies['imdb_score'].values.argmax()
print(df_movies.ix[max_rated_movie_index])


import matplotlib.pyplot as plt
df_2 = df[df['budget'] < 500000]
# df.plot(kind='scatter', x='imdb_score', y='budget', title='rating vs budget')
# df['imdb_score'].plot(kind='hist', title='Score')
# df['imdb_score'].plot(kind='box')
# plt.show()


# plot histograms for movies from 2008, 2009, 2010 in subplots
def plot_histograms():
    hist_2008 = df[df['title_year'] == 2008]['imdb_score']
    hist_2009 = df[df['title_year'] == 2009]['imdb_score']
    hist_2010 = df[df['title_year'] == 2010]['imdb_score']
    hist_2011 = df[df['title_year'] == 2011]['imdb_score']

    fig, axes = plt.subplots(nrows=2, ncols=2)

    hist_2008.plot(ax=axes[0, 0], kind='hist')
    hist_2009.plot(ax=axes[0, 1], kind='hist')
    hist_2010.plot(ax=axes[1, 0], kind='hist')
    hist_2011.plot(ax=axes[1, 1], kind='hist')

    plt.show()

# plot_histograms()


# plot genres count as bar plot
genres = df['genres'].value_counts()
# genres.plot(kind='bar')
# plt.show()

df_genres_split = df['genres'].str.split('|', expand=True)[0].value_counts()
print(df_genres_split)

# TODO calculate splited genres counts
df_genres_split = df['genres'].str.split('|', expand=True)
