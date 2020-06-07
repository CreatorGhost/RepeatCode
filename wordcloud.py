Libraries
'''
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
import nltk
from matplotlib import rcParams
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.cm as cm
import numpy as np
import collections
%matplotlib inline
'''
## Simple Pyplot
rcParams["figure.figsize"] = 5,8
data["Age"].value_counts()[:20].plot(kind="pie")




'''
Fucntion TO Generate Word Cloud
'''
def plotCloud(word):
  stwords = STOPWORDS
  word=' '.join(word)  ## Used When List of words are passed . Remove if ugoing string
  wordcloud = WordCloud(stopwords=stwords,width = 3000,height = 2000, background_color="black", max_words=10).generate(word)
  rcParams['figure.figsize'] = 20, 50
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.show()
'''
Plotting Words Frequecny

'''
def wordCountPlot(filtered_words):
  
  counted_words = collections.Counter(filtered_words)
  words,counts=[],[];
  for letter, count in counted_words.most_common(10):
    words.append(letter)
    counts.append(count)
  colors = cm.rainbow(np.linspace(0, 1, 10))
  rcParams['figure.figsize'] = 20, 10
  plt.title('Top words vs their count')
  plt.xlabel('Count')
  plt.ylabel('Words')
  plt.barh(words, counts, color=colors)


## netflix_titles = netflix_movies.Title[:500].values  ## To Convert data frame cloumn into array
generate_word_cloud(netflix_titles)
'''
