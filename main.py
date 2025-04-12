# -*- coding: utf-8 -*-

import streamlit as st

if "user" not in st.session_state:
    st.session_state.user=None
if "api_key" not in st.session_state:
    st.session_state.api_key=None
    
if "limit_chars" not in st.session_state:
    st.session_state.limit_chars=10*1000



if st.session_state.user:
    if st.session_state.user==1:
        pg=st.navigation([st.Page("page3.py",title="Home Page"),st.Page("page4.py",title="Resume Analysis"),
                          st.Page("page5.py",title="Interview Practice"),st.Page("page6.py",title="Logout"),
                          st.Page("pages/settings.py",title="Settings")])
    else:
        pg=st.navigation([st.Page("page2.py",title="Register")])
        
else:
    pg=st.navigation([st.Page("app.py",title="Welcome")])
pg.run()