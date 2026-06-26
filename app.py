import streamlit as st
import sqlite3
from datetime import datetime


# database
conn = sqlite3.connect(
    "chat.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    time TEXT
)
""")

conn.commit()



st.title("💬 Online Messaging App")


# username

username = st.text_input(
    "Enter your name"
)



if username:


    st.success(
        "Logged in as " + username
    )


    msg = st.text_input(
        "Type message"
    )


    if st.button("Send"):

        cursor.execute(
            """
            INSERT INTO messages
            (username,message,time)
            VALUES(?,?,?)
            """,
            (
                username,
                msg,
                datetime.now().strftime(
                    "%H:%M:%S"
                )
            )
        )

        conn.commit()

        st.rerun()



    st.subheader(
        "Messages"
    )


    data = cursor.execute(
        """
        SELECT username,message,time
        FROM messages
        ORDER BY id DESC
        """
    ).fetchall()



    for user,text,time in data:

        st.write(
            f"""
            **{user}**  
            {text}  
            🕒 {time}
            """
        )
