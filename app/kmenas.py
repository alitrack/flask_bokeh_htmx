
# https://panel.holoviz.org/gallery/simple/iris_kmeans.html
# import panel as pn
from bokeh.embed import components
import hvplot.pandas

from sklearn.cluster import KMeans
from bokeh.sampledata import iris

import holoviews as hv

def disable_logo(plot, element):
    plot.state.toolbar.logo = None
hv.extension('bokeh')
hv.plotting.bokeh.ElementPlot.hooks.append(disable_logo)



# pn.extension(sizing_mode="stretch_width")

flowers = iris.flowers.copy()
cols = list(flowers.columns)[:-1]

# x = pn.widgets.Select(name='x', options=cols)
# y = pn.widgets.Select(name='y', options=cols, value='sepal_width')
# n_clusters = pn.widgets.IntSlider(name='n_clusters', start=1, end=5, value=3)

# @pn.depends(x.param.value, y.param.value, n_clusters.param.value)
def get_clusters(x, y, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    est = kmeans.fit(iris.flowers.iloc[:, :-1].values)
    flowers['labels'] = est.labels_.astype('str')
    centers = flowers.groupby('labels').mean()
    xx= (flowers.sort_values('labels').hvplot.scatter(x, y, c='labels', size=100, height=500) *
            centers.hvplot.scatter(x, y, marker='x', color='black', size=400,
                                   padding=0.1, line_width=5))
    return components(hv.render(xx))

# pn.Column(
#     '# Iris K-Means Clustering',
#     pn.Row(pn.WidgetBox(x, y, n_clusters), get_clusters)
# )

# pn.template.FastListTemplate(
#     site="Panel", title="Iris Kmeans", 
#     sidebar=[x, y, n_clusters],
#     main=[
#         "This app provides an example of **building a simple dashboard using Panel**.\n\nIt demonstrates how to take the output of **k-means clustering on the Iris dataset** using scikit-learn, parameterizing the number of clusters and the variables to plot.\n\nThe entire clustering and plotting pipeline is expressed as a **single reactive function** that responsively returns an updated plot when one of the widgets changes.\n\n The **`x` marks the center** of the cluster.""",
#         get_clusters
#         ]
# ).servable();