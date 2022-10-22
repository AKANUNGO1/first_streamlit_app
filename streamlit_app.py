
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
#create the repeatable code block called a Function -new change
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

#streamlit.text(fruityvice_response.json())#Just writess the json data onto the screen
#commented the streamlit.text part to stop the webpage from displaying the json directly 
try:
# before
#fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
#after
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
#after
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
  else:
     back_from_function =get_fruityvice_data(this_fruit_choice)
     streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error(e)
 
#dont run anything past here while we troubleshoot
#streamlit.stop()

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#Snowflake functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list
  streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')")
