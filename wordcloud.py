Libraries
'''
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import nltk
import plotly.express as px
from wordcloud import WordCloud

'''
## Simple Pyplot
rcParams["figure.figsize"] = 5,8
data["Age"].value_counts()[:20].plot(kind="pie")




'''
Fucntion TO Generate Word Cloud
'''
def generate_word_cloud(text):
    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        background_color = 'black').generate(str(text))
    fig = plt.figure(
        figsize = (40, 30),
        facecolor = 'k',
        edgecolor = 'k')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
'''

netflix_titles = netflix_movies.Title[:500].values  ## Creating numpy array of all word from data frame
generate_word_cloud(netflix_titles)
'''
