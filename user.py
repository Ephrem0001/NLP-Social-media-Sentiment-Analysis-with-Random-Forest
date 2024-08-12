import streamlit as st
import sqlite3
import time
import pickle
import sys

sys.path.insert(1, "c:\users\graphics\pycharmprojects\myproject\.venv\lib\site-packages")

from streamlit_option_menu import option_menu

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable (username TEXT , password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username,password) VALUES(?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_user():
    c.execute("SELECT * FROM usertable")
    data = c.fetchall()
    return data


def main():
    st.title("Social media App")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":

        option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            )
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")
        if st.sidebar.checkbox("Login"):
            # if password=="12345"

            create_usertable()
            result = login_user(username, password)
            if result:
                st.success("Logged In as {}".format(username))

                # load the model
                model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

                st.title('Social media Sentiment Analysis')

                tweet = st.text_input('Enter your tweet')

                submit = st.button('Predict')

                if submit:
                    start = time.time()
                    prediction = model.predict([tweet])
                    end = time.time()
                    st.write('Prediction time taken: ', round(end - start, 2), 'seconds')

                    print(prediction[0])
                    st.write(prediction[0])
            else:
                st.warning("Incorrect Username or Password")

    elif choice == "SignUp":
            st.subheader("Create New Account")
            new_user = st.text_input("User Name")
            new_password = st.text_input("Password", type='password')

            if st.button("SignUp"):
                create_usertable()
                add_userdata(new_user, new_password)
                st.success("you have successfully created a valid account")
                st.info("Go to Logon Menu To Login")
main()