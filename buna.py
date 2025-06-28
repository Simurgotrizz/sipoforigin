import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Sip Of Origin", layout="centered")

st.subheader("Sip Of Origin")
st.write("Taste the origin")


with st.sidebar: 
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "About us", "Brewing process", "Subscription", "Packs", "Terms and policy of privacy", "Contact"],
    )


if selected == "Home":
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://giphy.com/gifs/garden-ZuhhRTIUFF00U")
    }
 
    [data-testid=stHeader] {
    Background-color: rgba(0, 0, 0, 0);
    }

    [data-testid="stToolbar"] {
    right: 2rem;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True,)
    st.title("About:")
    st.write("Hello, :wave:")
    st.write("Here at Sip Of Origin as the name suggests we want you to sip on traditional buna which is coffee in Amaharic the native language of Ethiopia the birthplace of coffee")
    st.write("Our mission is simple: we want you to experience ")

    st.write("With PCportal, you can shop with confidence, knowing that each gaming desktop we feature has been carefully selected for its performance, reliability, and value. We're committed to delivering an exceptional shopping experience, from browsing our curated collection to making your final purchase.")

    st.write("Thank you for choosing PCportal. We're excited to help you find the perfect custom gaming rigs that are ready for action. Let's embark on this gaming journey together!")

    st.write("Warm regards,")
    st.write("Simur Samuel")
