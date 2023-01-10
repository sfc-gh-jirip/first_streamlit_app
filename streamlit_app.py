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

str.dataframe(my_fruit_list)
