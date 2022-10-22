
import streamlit,pandas,requests
import snowflake.connector
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

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
#streamlit.text(fruityvice_response.json())#Just writess the json data onto the screen
#commented the streamlit.text part to stop the webpage from displaying the json directly 
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#In order to normalise the json data we can take the above json part from response & normalise it using pandas
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#the below will display the data 
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()-- to fetch only one row from the table
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
#streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
