import streamlit as st


tab1, tab2 = st.tabs(["TAB1", "TAB2"])

with tab1:
    col1, col2 = st.columns([3,3])
    with col1:
        text1 = st.text_input('Insert text')
    with col2:
        text2 = st.text_input('Insert another text')
