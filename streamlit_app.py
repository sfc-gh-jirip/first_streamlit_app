import streamlit as str
import pandas as pa

str.title('My Parents New Healthy Diner')

str.header('Breakfast menu')
str.text('🥣 Omega 3 & Blueberry Cereal')
str.text('🥗 Kale, spinach and rocket smoothie')
str.text('🐔 Hard-boiled egg')
str.text('🥑🍞 Avocado toast')
str.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pa.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = str.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
str.dataframe(fruits_to_show)
