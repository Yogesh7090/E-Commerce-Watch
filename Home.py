import streamlit as st
# from streamlit_extras.app_logo import add_logo
from logo import add_logo

st.set_page_config(
    page_title="VOC",
    
)
add_logo()
st.markdown(
    """
    <style>
    .custom-title {
        color: #005F7B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class in the title
st.markdown('<h1 class="custom-title">Welcome to VOC!</h1>', unsafe_allow_html=True)

# st.write("# Welcome to E-Commerce Watch!")



st.markdown(
    """
    Discover how you can transform Macmillan e learning platform  customer interactions with the power of AI and GenAI technology. From boosting 
    customer satisfaction and retention to driving higher sales and loyalty, innovative strategies are revolutionizing the way 
    businesses connect with their clients. VoC offers a seamless solution to these challenges, providing real-time insights from customer 
    reviews to enhance strategic decision-making and customer satisfaction.
 
    - An improved and simplified visualization of feedback and trends.
    - Tailored actions that can be taken to improve customer experience.
    - New root cause identification and breakdown to provide a summarized version of the customer feedback.
    - Identify and prioritise what customers want most with Topics  
""",
 unsafe_allow_html=True
)
# st.markdown(
#     """
#     - Check out [Ecommerce](https://catalyticsdatum.com/Home/ECommerce)
#     - Check out our other [products](https://catalyticsdatum.com/Home/Solution)
# """
# )

# Add custom CSS to hide the full-screen button
st.markdown(
    """
    <style>
    button[title="View fullscreen"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# url = "https://i.ibb.co/zf4Qh6b/catalytics-logo.png"
# with st.sidebar:
#     st.markdown(
#         f"""
#         <style>
#             [data-testid="stSidebarNav"] + div {{
#                 position: absolute;
#                 bottom: 0;
#                 width: 100%;
#                 text-align: center;
#                 padding-bottom: 15px;
#                 overflow: hidden;
#             }}
#             .sidebar-footer {{
#                 display: flex;
#                 flex-direction: column;
#                 align-items: center;
#             }}
#             .sidebar-footer img {{
#                 max-width: 80%;
#                 height: auto;
#                 max-height: 100px;
#             }}
#             .sidebar-footer p {{
#                 margin: 0;
#                 font-style: italic; 
#             }}
#         </style>
#         <div class="sidebar-footer">
#             <p><em>Powered by</em></p>
#             <img src="{url}" alt="Logo">
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )












# url="https://i.ibb.co/zf4Qh6b/catalytics-logo.png"
# st.write("Powered by")
# st.markdown(
#         f"""
#         <style>
#             [data-testid="stSidebarNav"] + div {{
#                 position:absolute;
#                 bottom: 0;
#                 height:40%;
#                 background-image: url({url});
#                 background-size: 85% auto;
#                 background-repeat: no-repeat;
#                 background-position-x: center;  
#                 background-position-y: bottom;
#             }}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# with st.sidebar:
#     st.write("")


# Add custom CSS to hide the full-screen button and adjust sidebar content


# with st.sidebar:
#     # Content at the top of the sidebar
#     st.write("Powered by")

#     # Spacer to push content to the bottom
#     # st.write("")

#     # Add logo at the bottom with a specified width
#     st.image("C:\\Users\\KavyaSabu\\Downloads\\catalytics-logo.png", width=150)  # Adjust the width as needed

# with st.sidebar:
    
    
#     # Add CSS to fix the position and size of the logo
#     st.markdown(
#         """
#         <style>
#         .sidebar .sidebar-content {
#             display: flex;
#             flex-direction: column;
#             height: 100%;
#             justify-content: flex-end;
#         }
#         .sidebar .sidebar-content > *:nth-last-child(2) {
#             margin-top: auto;
#         }
#         .sidebar .sidebar-content img {
#             max-width: 20px;
#             height: auto;
#             margin: 0 auto;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
    
    # st.write("Powered by")
    # # Add logo at the bottom
    # st.image("C:\\Users\\KavyaSabu\\Downloads\\catalytics-logo.png", width=150,)

# st.image("C:\\Users\\KavyaSabu\\Downloads\\catalytics-logo.png")