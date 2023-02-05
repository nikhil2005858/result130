import streamlit  as st
st.header(" WELCOME TO POLYTECHNIC  GOVERNMENT CHAMARAJANAGAR ")
st.image("govtpolychamraj01.jpg")
st.container()
st.write("[FRIST SEM RESULTS](https://nikhil2005858-fristsem-result-1sem-5idq7n.streamlit.app/)")
st.write("SECOND SEM RESULTS")
button=st.button("GET RESULT")
data=open("results1.html","r")
x=data.read()
if button==True:
   st.markdown(x,unsafe_allow_html=True)
