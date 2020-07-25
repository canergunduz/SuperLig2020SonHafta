# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:29:56 2020

@author: caner.gunduz
"""

import plotly.express as px
from plotly.offline import plot
import pandas as pd

data = pd.read_excel(r'C:\Users\caner.gunduz\Desktop\Dusme.xlsx', sheet_name = 'Sheet3')


df = px.data.tips()
fig = px.sunburst(data, path=['Takım', 'Sonuc','Kural'], values='Adet')
plot(fig)


