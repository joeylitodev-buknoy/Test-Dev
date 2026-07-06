from openai import OpenAI
import streamlit as st

st.set_page_config(page_title="Streamlit Chat", page_icon="💬")
st.title("Chatbot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.success("API Key Found")

prompt = st.chat_input("Your answer.")

if prompt:

    st.write("Step 1: Prompt received")

    st.chat_message("user").write(prompt)

    st.write("Step 2: User message displayed")

    try:

        st.write("Step 3: Calling OpenAI")

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.write("Step 4: OpenAI responded")

        answer = response.choices[0].message.content

        st.chat_message("assistant").write(answer)

        st.write("Step 5: Assistant displayed")

    except Exception as e:

        st.error(f"OpenAI Error: {e}")