import streamlit as st
import streamlit.components.v1 as stc
import altair as alt

# Function to plot prediction probabilities (if needed in the future)
def plot_prediction_proba(pred_proba_df):
    c = alt.Chart(pred_proba_df).mark_bar().encode(
        x='Classes',
        y='Probabilities',
        color='Classes'
    )
    st.altair_chart(c)

# Professional UI Title
custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:10px;
border-radius:10px;border:5px solid #464e5f;text-align:center;">
    <span style='color:red'>🎬 Movies</span>
    <span style='color:black'> Database 📂</span>
</div>
"""

def main():
    stc.html(custom_title)

    menu = ["🏠 Home", "ℹ️ About"]
    choice = st.sidebar.selectbox("📌 Menu", menu)

    if choice == "🏠 Home":
        st.subheader("🏠 Home")
        with st.form(key='searchForm'):
            search_movie = st.text_input("🔍 Search Movie")
            submit_button = st.form_submit_button(label='🔎 Search')

        if submit_button:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.info(f"📽️ Showing Results For: {search_movie}")

            with col2:
                st.info("🎬 Results will be displayed here.")

    else:
        st.subheader("ℹ️ About")
        st.write("This is a simple movie search database application.")

if __name__ == '__main__':
    main()
