import streamlit as st
import pandas as pd

st.title('Dashboard')

df_products = pd.read_csv('products.csv')

st.write("Toto bude jednoduchý text!")

_data, _graph, _desc = st.tabs(['Ukázka dat', 'Grafické zobrazení', 'Poznámky'])
with _data:
    st.dataframe(df_products.head(), hide_index=True)
with _graph:
    st.line_chart(df_products['price'].head(10))
with _desc:
    st.write("Toto bude popis!")




_1, _2, _3 = st.columns(3)
with _1:
    st.success('Tohle je jasný úspěch!')
with _2:
    st.warning('Toto je varování!')
with _3:
    st.error('Takhle ukazuju chyby!')

_1, _2 = st.columns(2)
with _1:
    st.info('Toto bude informační kousek!')
with _2:
    st.code("print('Ahoj')", language='python')

st.code("""for i in range(10):
    print(i)""", language='python')


st.dataframe(df_products, hide_index=True)
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

text = st.text_input("Enter some text")

st.header(f"This page has run {st.session_state.counter} times and text is \"{text}\".")
st.button("Run it again")
"""import streamlit as st
import pandas as pd

st.title('Dashboard')

df_products = pd.read_csv('products.csv')

st.write("Toto bude jednoduchý text!")

_data, _graph, _desc = st.tabs(['Ukázka dat', 'Grafické zobrazení', 'Poznámky'])
with _data:
    st.dataframe(df_products.head(), hide_index=True)
with _graph:
    st.line_chart(df_products['price'].head(10))
with _desc:
    st.write("Toto bude popis!")




_1, _2, _3 = st.columns(3)
with _1:
    st.success('Tohle je jasný úspěch!')
with _2:
    st.warning('Toto je varování!')
with _3:
    st.error('Takhle ukazuju chyby!')

_1, _2 = st.columns(2)
with _1:
    st.info('Toto bude informační kousek!')
with _2:
    st.code("print('Ahoj')", language='python')

st.code('for i in range(10):
    print(i)', language='python')


st.dataframe(df_products, hide_index=True)
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

text = st.text_input("Enter some text")

st.header(f"This page has run {st.session_state.counter} times and text is \"{text}\".")
st.button("Run it again")"""