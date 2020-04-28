import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, dates as mdates, ticker

from io import BytesIO
import base64

plt.style.use("seaborn")

def plt_to_png(fig):
  img = BytesIO()
  fig.savefig(img, format='png', dpi=72)
  img.seek(0)
  graph_url = base64.b64encode(img.getvalue()).decode()
  return 'data:image/png;base64,{}'.format(graph_url)

def graph_county_df(df):
  df['Sum'] = df['FREQUENCY'].cumsum()
  df.head()
  return_val={}

  f1, ax1 = plt.subplots(figsize=(10, 7.5), constrained_layout=True, dpi=72)
  ax1.plot(df.index, df['Sum'], marker='.', markersize=12)
  locator = mdates.AutoDateLocator(minticks=4, maxticks=10)
  formatter = mdates.ConciseDateFormatter(locator)
  formatter.offset_formats = ['', '', '', '', '', '', ]
  ax1.set_xlabel('')
  ax1.xaxis.set_minor_locator(ticker.NullLocator())
  ax1.xaxis.set_major_locator(locator)
  ax1.xaxis.set_major_formatter(formatter)
  xmin, xmax = ax1.get_xlim()
  ax1.set_xlim(xmin-1.0,xmax+1.0)
  ax1.tick_params(axis='both', which='major', labelsize=16)

  return_val['sum'] = plt_to_png(f1)

  f2, ax2 = plt.subplots(figsize=(10, 7.5), constrained_layout=True, dpi=72)
  ax2.bar(df.index, df['FREQUENCY'])
  locator = mdates.AutoDateLocator(minticks=4, maxticks=10)
  formatter = mdates.ConciseDateFormatter(locator)
  formatter.offset_formats = ['', '', '', '', '', '', ]
  ax2.set_xlabel('')
  ax2.xaxis.set_minor_locator(ticker.NullLocator())
  ax2.xaxis.set_major_locator(locator)
  ax2.xaxis.set_major_formatter(formatter)
  ax2.tick_params(axis='both', which='major', labelsize=16)

  return_val['count'] = plt_to_png(f2)

  return return_val