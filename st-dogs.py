import streamlit as st
import pandas as pd
import datetime

# Initialize session state
if 'dogs_counter' not in st.session_state:
    st.session_state.dogs_counter = 0
if 'other_counter' not in st.session_state:
    st.session_state.other_counter = 0
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Dogs', 'Other', 'Percentage'])

# Function to update counters
def update_counter(button_type):
    if button_type == 'dogs':
        st.session_state.dogs_counter += 1
    else:
        st.session_state.other_counter += 1

    # Calculate percentage
    total_clicks = st.session_state.dogs_counter + st.session_state.other_counter
    dogs_percentage = (st.session_state.dogs_counter / total_clicks) * 100 if total_clicks > 0 else 0

    # Update the data table
    new_row = {'Date': datetime.datetime.now().strftime('%Y-%m-%d'),
               'Dogs': st.session_state.dogs_counter,
               'Other': st.session_state.other_counter,
               'Percentage': f"{dogs_percentage:.2f}%"}
    st.session_state.data = st.session_state.data.append(new_row, ignore_index=True)

# Function to reset everything
def reset_everything():
    st.session_state.dogs_counter = 0
    st.session_state.other_counter = 0
    st.session_state.data = pd.DataFrame(columns=['Date', 'Dogs', 'Other', 'Percentage'])

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

# Reset button
if st.button('Reset Everything'):
    reset_everything()

# Display counters
st.metric(label="Dogs Counter", value=st.session_state.dogs_counter)
st.metric(label="Other Counter", value=st.session_state.other_counter)

# Display ratio
total_clicks = st.session_state.dogs_counter + st.session_state.ot
