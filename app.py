import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime


# Firebase connect

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase-key.json"
    )

    firebase_admin.initialize_app(
        cred
    )


db = firestore.client()



st.title("💬 Online Chat")



# Login

name = st.text_input(
    "Enter your name"
)


if name:


    st.success(
        f"Welcome {name}"
    )



    message = st.text_input(
        "Message"
    )



    if st.button("Send"):


        db.collection(
            "messages"
        ).add({

            "user":name,

            "message":message,

            "time":
            datetime.now()

        })



    st.subheader(
        "Messages"
    )


    messages = db.collection(
        "messages"
    ).order_by(
        "time"
    ).stream()



    for msg in messages:

        data = msg.to_dict()

        st.write(
            f"""
            **{data['user']}**
            : {data['message']}
            """
        )
