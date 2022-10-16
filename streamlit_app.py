
import streamlit,pandas
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#lets put a index to pick up fruits so that user can choose there own fruits by using multiselect
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
#lets use to pick fruits by fruitname instead of index 
my_fruit_list = my_fruit_list.set_index('Fruit')
#display the csv table on the page
streamlit.dataframe(my_fruit_list)
