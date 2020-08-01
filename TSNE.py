import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls


from sklearn.preprocessing import MinMaxScaler
from sklearn.manifold import TSNE
dfp_subsampled = data[0:5000]
X = MinMaxScaler().fit_transform(dfp_subsampled[['vintage', 'gender', 'dependents', 'city','customer_nw_category', 'branch_code', 'days_since_last_transaction','current_balance', 'previous_month_end_balance', 'average_monthly_balance_prevQ', 'average_monthly_balance_prevQ2','current_month_credit', 'previous_month_credit', 'current_month_debit','previous_month_debit', 'current_month_balance', 'previous_month_balance' ]])
y = dfp_subsampled['churn'].values


tsne2d = TSNE(
    n_components=2,
    init='random', # pca
    random_state=101,
    method='barnes_hut',
    n_iter=1000,
    verbose=2,
    angle=0.5
).fit_transform(X)


sns.set(rc={'figure.figsize':(11.7,8.27)})

df = pd.DataFrame({'x':tsne2d[:,0], 'y':tsne2d[:,1] ,'label':y})

palette = sns.color_palette("bright", 2)
# draw the plot in appropriate place in the grid
sns.scatterplot(data=df, x='x', y='y', hue='label',legend='full', palette=palette)
plt.title("perplexity : {} and max_iter : {}".format(30, 1000))
plt.show()




tsne3d = TSNE(
    n_components=3,
    init='random', # pca
    random_state=101,
    method='barnes_hut',
    n_iter=1000,
    verbose=2,
    angle=0.5
).fit_transform(X)


import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

trace1 = go.Scatter3d(
    x=tsne3d[:,0],
    y=tsne3d[:,1],
    z=tsne3d[:,2],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        color = y,
        colorscale = 'Portland',
        colorbar = dict(title = 'churn'),
        line=dict(color='rgb(255, 255, 255)'),
        opacity=0.75
    )
)

data=[trace1]
layout=dict(height=800, width=800, title='3d embedding with Scalled features')
fig=dict(data=data, layout=layout)
py.iplot(fig, filename='3DBubble')
