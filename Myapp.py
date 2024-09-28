# myapp.py
import streamlit as st
import time
from create_label import get_label  # Modified import statement


def main():

    # Set page configuration
    st.set_page_config(
        page_title="News Category Application | News Classification CNN Indonesia", page_icon="📺"
    )

    # Two columns layout
    col1, col2 = st.columns(2)

    # Column 1: Display banner image
    with col1:
        st.image("assets/banner.png", use_column_width=True)

    # Column 2: Display subheader and description
    with col2:
        st.subheader("News Classification: Category Application for News")
        st.caption(
            "News is generally categorized into several types such as sports, economy, "
            "entertainment, and other categories. With this news classification, we can "
            "find the type of news category that corresponds to the content of the news."
        )

    # Text area for user input
    news_text = st.text_area("Enter News Content", key="input_text", height=250)

    # Button to trigger category identification
    if st.button("Find Category"):
        if news_text:
            # Get the predicted label/category
            text = get_label(news_text)

            # Display result in an expander
            with st.expander('Show Result'):
                st.write('The news you entered belongs to the category: ')

                # Handle each possible category
                if text == "education":
                    st.info(text, icon="🧑‍🏫")
                    url = "https://www.google.com/search?q=education+news+today"
                    st.write(f'Read the latest news related to education 🔎 [Education news today]({url})')

                elif text == "sports":
                    st.info(text, icon="🚣")
                    url = "https://www.google.com/search?q=sports+news+today"
                    st.write(f'Read the latest news related to sports 🔎 [Sports news today]({url})')

                elif text == "economy":
                    st.info(text, icon="💸")
                    url = "https://www.google.com/search?q=economy+news+today"
                    st.write(f'Read the latest news related to the economy 🔎 [Economy news today]({url})')

                elif text == "entertainment":
                    st.info(text, icon="🎥")
                    url = "https://www.google.com/search?q=entertainment+news+today"
                    st.write(f'Read the latest news related to entertainment 🔎 [Entertainment news today]({url})')

        else:
            # If no text is entered, show a toast message
            time.sleep(0.5)
            st.toast('Please enter some text first', icon='🤧')


# Main function call
if __name__ == "__main__":
    main()
