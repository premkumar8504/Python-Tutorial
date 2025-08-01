import streamlit as st
import pandas as pd
import numpy as np


# data = pd.read_csv("movies.csv")
# st.write(data)

st.write("# My cool Chart")

chart_data = pd.DataFrame(
  np.random.randn(20, 3),
  columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)

# data_2 = pd.read_csv("insurance.csv")
# st.write(data_2)