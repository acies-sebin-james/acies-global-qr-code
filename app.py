import streamlit as st

# Page configuration
st.set_page_config(page_title="Acies Global Social Media Links", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital,wght@1,700&display=swap');

        body {
            font-family: 'DM Serif Display', serif;
        }

        .Name {
            margin-left: auto;
            margin-right: auto;
            display: flex;
#           justify-content: center;
        }

        .center-text {
            text-align: center;
            font-family: 'DM Serif Display', serif;
            font-size: 24px;
            font-weight: bold;
            font-style: italic;
            margin: 20px 0;
        }
        
        .acies {
            text-align: center;
            font-family: 'DM Serif Display', serif;
            font-size: 28px;
            font-weight: bold;
            margin: 20px 0;        
        }

        .link-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 2px solid #000;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            width: 80%;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            background-color: #fdd764;            
        }

        .link-box a {
            font-family: 'DM Serif Display', serif;
            font-size: 20px;
            font-weight: bold;
            font-style: italic;
            text-decoration: none;
            color: #007BFF;
            margin: 10px 0

        }

        .link-box a:hover {
            color: #0056b3;
        }

        @media (max-width: 768px) {
            .center-text {
                font-size: 20px;
            }

            .link-box a {
                font-size: 18px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Social media and website links
st.markdown('<div class="acies">Acies Global</div>', unsafe_allow_html=True)
st.markdown('<div class="center-text">Follow us on social media and visit our website!</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="link-box">
        <a href="https://www.aciesglobal.com/home" target="_blank">Website</a>
        <a href="https://www.linkedin.com/company/acies-global" target="_blank">LinkedIn</a>
        <a href="https://www.instagram.com/acies__global" target="_blank">Instagram</a>

    </div>
    """,
    unsafe_allow_html=True
)

# # Center align the image
# col1, col2, col3 = st.columns([1, 1, 1])
# # Company logo
# with col2:
#     st.image("Acies-Original-Black.png",channels='RGB')
