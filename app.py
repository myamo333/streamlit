import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'    

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)

# if st.checkbox('Show Image'):
#     img = Image.open('denki.jpg')
#     st.image(img, caption='denki group', use_column_width=True)

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここはカラムです')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')

# text = st.text_input('あなたが好きな趣味を教えてください。')

# text = st.text_input('あなたが好きな趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は、', text, 'です。'
# 'コンディション : ', condition
# st.table(df.style.highlight_max(axis=0))
#st.map(df)


