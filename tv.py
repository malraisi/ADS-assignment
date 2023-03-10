import altair as alt
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px
import graphviz
page = st.sidebar.selectbox("Choose a page", ["Page 1", "Page 2", "Page 3", "Page 4"])


tv = pd.read_csv('data_TV.csv')



tv = tv.dropna()
sample1 = tv.head(30)


if page == "Page 1":

    alt.data_transformers.disable_max_rows()
    st.title('πππ ππΆπππΉ ππππ»ππΎπ ππ½πππ')
    st.markdown('**πΌπππππΉππΈππΎππ πΆπ·πππ πππ πΉπΆππΆπππ** ')
    st.write('The top Netflix movies dataset on Kaggle is a collection of information about the most popular and highly rated films that are available to stream on the popular entertainment platform, Netflix. The dataset includes a variety of details about each movie, such as its title, release year, cast, and IMDb rating. It also includes information about the genres and categories that each movie belongs to, as well as its runtime and the countries in which it was produced. ')
    st.write('This dataset is a valuable resource for anyone interested in exploring the most popular movies on Netflix and understanding the trends and preferences of the platforms users. It can be used for a variety of purposes, including data analysis, machine learning projects, and more.')
    st.markdown('**πΉπΎππΉπΎπππ**')
    st.write('the Top Rated TV Shows dataset on Kaggle also includes details on the genre of each show, the number of episodes, and the average runtime of each episode. This allows you to see which genres are most popular, how long the average episode is, and how much content each show has. You can also use this dataset to compare the ratings of different shows and see which ones have the highest overall scores. This can be a great way to discover new shows to watch or to see how your favorite shows stack up against the competition. Additionally, you can use this dataset to analyze trends in television over time and see how the industry has changed. For example, you might be able to see if certain genres are becoming more popular or if there is a trend toward shorter episode lengths. Overall, the Top Rated TV Shows dataset on Kaggle provides a wealth of information for anyone interested in television and its history.')
    st.markdown('**ππππΎππππππ πΈπππΆπππΉ π·π:** ')


    st.write('Mohammed Mahmood Al-Raisi - 16S161334')
    st.write('Ali Salim Al-Jardani - 16S17174')
    def convert_df(df):
        return df.to_csv().encode('utf-8')
  

    csv = convert_df(tv)

    st.download_button(
          label="Download data as CSV",
          data=csv,
          file_name='tv_dataset.csv',
          mime='text/csv',)
elif page == "Page 2":
    st.title('ππΈπΆππππ πΆππΉ ππΎππ')
    showname = st.selectbox("Select The Origin Country",sample1['origin_country'].unique())
    plot_type=st.radio("Select The Plot Type",['Scatter','Line'])
    if plot_type == 'Scatter':
      pl = alt.Chart(sample1[sample1['origin_country']==showname]).mark_circle().encode(
      x = 'vote_count:N',
      y ='popularity:N',
      color = 'name:N',
      tooltip = ['vote_count','popularity','name']).interactive()
    else:
      pl = alt.Chart(sample1[sample1['origin_country']==showname]).mark_line().encode(
        x = 'popularity:N',
        y ='vote_count:N',
        tooltip = ['origin_country','popularity','name']
    ).interactive()
    st.altair_chart(pl)
elif page == "Page 3":
    st.title('π΅πΆπ πΆππΉ ππΎπ')

    Bar_plot = st.checkbox("Bar plot")
    Pie_plot = st.checkbox("Pie plot")

    if Bar_plot:
      st.subheader('Bar chart')
      tv=tv.head(10)
      bar = alt.Chart(tv).mark_bar().encode(x = 'name',y = 'mean(popularity)',color = 'name:N')
      bar

    if Pie_plot:
      st.subheader('Pie chart')
      fig1, ax1 = plt.subplots()
      ax1.pie(tv['vote_count'].head(10), labels=tv['name'].head(10), autopct='%1.1f%%',shadow=True, startangle=90)
      ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
      st.pyplot(fig1)
      
elif page == "Page 4":
    st.title('π΅ππ·π·ππ πΆππΉ ππΎπππΆππΎππΆππΎππ')
    options = ['Bubble Plot', 'Graphviz Chart']

    selected_options = st.multiselect("Select charts to display", options)

    for option in selected_options:
       if option == 'Bubble Plot':
            fig = px.scatter(tv.head(40), x="vote_count",
                    y="popularity",
                    size="popularity",
                    color="name",
                    hover_name="name",
                    log_x=True,
                    size_max=60, )
            fig    
       elif option == 'Graphviz Chart':
            graph = graphviz.Digraph()
            graph.edge('movies', 'horror')
            graph.edge('horror', 'conjuring')
            graph.edge('conjuring', 'joker')
            graph.edge('movies', 'drama')
            graph.edge('drama', 'friends')
            graph.edge('friends', 'mom')


            st.graphviz_chart(graph)




   
  



   
    
