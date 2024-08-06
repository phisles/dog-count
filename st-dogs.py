import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'dogs_counter' not in st.session_state:
    st.session_state.dogs_counter = 0
if 'other_counter' not in st.session_state:
    st.session_state.other_counter = 0

# Function to update counters
def update_counter(button_type):
    if button_type == 'dogs':
        st.session_state.dogs_counter += 1
    else:
        st.session_state.other_counter += 1

# Function to reset everything
def reset_everything():
    st.session_state.dogs_counter = 0
    st.session_state.other_counter = 0

# Reset counters every day
today = datetime.datetime.now().strftime('%Y-%m-%d')
if 'last_reset' not in st.session_state or st.session_state.last_reset != today:
    reset_everything()
    st.session_state.last_reset = today

st.title('Button Click Counter')

# Buttons
if st.button('WHERE ARE THE DOGS?'):
    update_counter('dogs')
if st.button('OTHER'):
    update_counter('other')

# Display counters
st.metric(label="Dogs Counter", value=st.session_state.dogs_counter)
st.metric(label="Other Counter", value=st.session_state.other_counter)

# Display ratio
total_clicks = st.session_state.dogs_counter + st.session_state.other_counter
if total_clicks > 0:
    dogs_percentage = (st.session_state.dogs_counter / total_clicks) * 100
    other_percentage = (st.session_state.other_counter / total_clicks) * 100
    st.metric(label="Dogs Percentage", value=f"{dogs_percentage:.2f}%")
    st.metric(label="Other Percentage", value=f"{other_percentage:.2f}%")
else:
    st.metric(label="Dogs Percentage", value="0.00%")
    st.metric(label="Other Percentage", value="0.00%")

# Add a small "Reset" link
if st.button('Reset'):
    reset_everything()
