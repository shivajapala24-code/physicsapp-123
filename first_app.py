import streamlit as st

st.header('Energy calculator')

col1,col2 = st.columns(2)

with col1:
    m =  st.subheader(':red[kinetic energy]')
    m = st.number_input('mass: ',key = 'a')
    v = st.number_input('velocity: ',key = 'b')
    if st.button('calculate',key = 'abc'):
        st.write(f'the kinetic energy is {0.5*m*v**2}')

with col2:
    m =  st.subheader(':red[potential energy]')
    m = st.number_input('mass: ',key = 'c')
    h = st.number_input('height: ',key = 'd')
    if st.button('calculate',key = 'xyz'):
        st.write(f'the kinetic energy is {ma*10*h}')

