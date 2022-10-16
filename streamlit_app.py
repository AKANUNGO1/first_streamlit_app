
import streamlit,pandas
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#lets use to pick fruits by fruitname instead of index 
my_fruit_list = my_fruit_list.set_index('Fruit')
#lets put a index to pick up fruits so that user can choose there own fruits by using multiselect
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
#lets put a picklist here so that they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#lets put the selected above two fruits in a variable 
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
#display the csv table on the page
#streamlit.dataframe(my_fruit_list)
#display only the fruits selected in the page 
streamlit.dataframe(fruits_to_show)
