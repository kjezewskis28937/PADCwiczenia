import streamlit as st
import pandas as pd
import time

st.title("Praca Domowa 06 – Streamlit")

# SIDEBARS
st.sidebar.header("ZAKLADKI")
page = st.sidebar.selectbox('WYBIERZ STRONE',['ANKIETA','STATY']) 

if page == 'ANKIETA':

    # ANKIETA
    st.header('ZAKLADKA - ANKIETA')

    imie = st.text_input("WPISZ SWOJE IMIE:", "")
    nazwisko = st.text_input("WPISZ SWOJE NAZWISKO:", "")
    if st.button("ZAPISZ"):
        imieResult = imie.title()
        nazwiskoResult = nazwisko.title()
        if(imieResult != '' and nazwiskoResult != ''):
            st.success("POMYSLNIE ZAPISANO DANE - IMIE: " + imieResult + " NAZWISKO: " + nazwiskoResult)
        else: 
            st.error('ŻADNE Z PÓL NIE MOŻE BYĆ PUSTE - UZUPEŁNIJ DANE')

else :

    #STATY
    st.header('ZAKLADKA - STATY') 

    #SYMULACJA OCZEKIWANIA
    def symulacjaSpin():
        with st.spinner("CZEKAJ..."):
            time.sleep(3)
            st.success("WCZYTANO PLIK")
            

    data = st.file_uploader("ZALADUJ PLIK CSV:", type=['csv'], on_change=symulacjaSpin)


    if data is not None:
        df = pd.read_csv(data)
    
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("WYBIERZ KOLUMNY DO WYKRESU:", all_columns_names)
        selected_chart_type = st.selectbox("WYBIERZ TYP WYKRESU:",["BAR CHART", "LINE CHART"])
                
        if len(selected_column_names) > 0:
            plot_data = df[selected_column_names]

            if (selected_chart_type == "BAR CHART"):
                st.bar_chart(plot_data)
            
            if (selected_chart_type == "LINE CHART"):
                st.line_chart(plot_data)

