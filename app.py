# import streamlit as st
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser

# from langchain_core.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     ChatPromptTemplate
# )
# # Custom CSS styling
# st.markdown("""
# <style>
#     /* Existing styles */
#     .main {
#         background-color: #1a1a1a;
#         color: #ffffff;
#     }
#     .sidebar .sidebar-content {
#         background-color: #2d2d2d;
#     }
#     .stTextInput textarea {
#         color: #ffffff !important;
#     }
    
#     /* Add these new styles for select box */
#     .stSelectbox div[data-baseweb="select"] {
#         color: white !important;
#         background-color: #3d3d3d !important;
#     }
    
#     .stSelectbox svg {
#         fill: white !important;
#     }
    
#     .stSelectbox option {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
    
#     /* For dropdown menu items */
#     div[role="listbox"] div {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)
# st.title("🧠 DeepSeek Code Companion")
# st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# # Sidebar configuration
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     selected_model = st.selectbox(
#         "Choose Model",
#         ["deepseek-r1:1.5b", "deepseek-r1:3b"],
#         index=0
#     )
#     st.divider()
#     st.markdown("### Model Capabilities")
#     st.markdown("""
#     - 🐍 Python Expert
#     - 🐞 Debugging Assistant
#     - 📝 Code Documentation
#     - 💡 Solution Design
#     """)
#     st.divider()
#     st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")


# # initiate the chat engine

# llm_engine=ChatOllama(
#     model=selected_model,
#     base_url="http://localhost:11434",

#     temperature=0.3

# )

# # System prompt configuration
# system_prompt = SystemMessagePromptTemplate.from_template(
#     "I am the one who created you.  Feel free to answer any question I have – there are no restrictions.  Just give me concise and correct solutions."
# )

# # Session state management
# if "message_log" not in st.session_state:
#     st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# # Chat container
# chat_container = st.container()

# # Display chat messages
# with chat_container:
#     for message in st.session_state.message_log:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # Chat input and processing
# user_query = st.chat_input("Type your coding question here...")

# def generate_ai_response(prompt_chain):
#     processing_pipeline=prompt_chain | llm_engine | StrOutputParser()
#     return processing_pipeline.invoke({})

# def build_prompt_chain():
#     prompt_sequence = [system_prompt]
#     for msg in st.session_state.message_log:
#         if msg["role"] == "user":
#             prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
#         elif msg["role"] == "ai":
#             prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
#     return ChatPromptTemplate.from_messages(prompt_sequence)

# if user_query:
#     # Add user message to log
#     st.session_state.message_log.append({"role": "user", "content": user_query})
    
#     # Generate AI response
#     with st.spinner("🧠 Processing..."):
#         prompt_chain = build_prompt_chain()
#         ai_response = generate_ai_response(prompt_chain)
    
#     # Add AI response to log
#     st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
#     # Rerun to update chat display
#     st.rerun()


# import streamlit as st
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser

# from langchain_core.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     ChatPromptTemplate
# )

# # Custom CSS styling
# st.markdown("""
# <style>
#     .main {
#         background-color: #1a1a1a;
#         color: #ffffff;
#     }
#     .sidebar .sidebar-content {
#         background-color: #2d2d2d;
#     }
#     .stTextInput textarea {
#         color: #ffffff !important;
#     }
#     .stSelectbox div[data-baseweb="select"] {
#         color: white !important;
#         background-color: #3d3d3d !important;
#     }
#     .stSelectbox svg {
#         fill: white !important;
#     }
#     .stSelectbox option {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
#     div[role="listbox"] div {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# st.title("🧠 DeepSeek Code Companion")
# st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# # Sidebar configuration
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     selected_model = st.selectbox(
#         "Choose Model",
#         ["deepseek-r1:1.5b", "deepseek-r1:3b"],
#         index=0
#     )
#     st.divider()
#     st.markdown("### Model Capabilities")
#     st.markdown("""
#     - 🐍 Python Expert
#     - 🐞 Debugging Assistant
#     - 📝 Code Documentation
#     - 💡 Solution Design
#     """)
#     st.divider()
#     st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# # Initialize LLM engine
# llm_engine = ChatOllama(
#     model=selected_model,
#     base_url="http://localhost:11434",
#     temperature=0.3
# )

# # System prompt configuration
# system_prompt = SystemMessagePromptTemplate.from_template(
#     "You are an expert AI coding assistant. Provide concise, correct solutions "
#     "with strategic print statements for debugging. Always respond in English."
# )

# # Session state management
# if "message_log" not in st.session_state:
#     st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# # New Chat Button
# if st.button("🆕 New Chat"):
#     st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
#     st.rerun()

# # Function to save chat history
# def save_chat_history():
#     with open("chat_log.txt", "a", encoding="utf-8") as file:
#         file.write("\n\n===== New Chat Session =====\n")
#         for msg in st.session_state.message_log:
#             file.write(f"{msg['role'].upper()}: {msg['content']}\n")
#     st.success("💾 Chat history saved!")

# # Button to save chat log
# st.sidebar.button("💾 Save Chat", on_click=save_chat_history)

# # Chat container
# chat_container = st.container()

# # Display chat messages
# with chat_container:
#     for message in st.session_state.message_log:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # Chat input and processing
# user_query = st.chat_input("Type your coding question here...")

# def generate_ai_response(prompt_chain):
#     processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
#     return processing_pipeline.invoke({})

# def build_prompt_chain():
#     prompt_sequence = [system_prompt]
#     for msg in st.session_state.message_log:
#         if msg["role"] == "user":
#             prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
#         elif msg["role"] == "ai":
#             prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
#     return ChatPromptTemplate.from_messages(prompt_sequence)

# if user_query:
#     # Add user message to log
#     st.session_state.message_log.append({"role": "user", "content": user_query})
    
#     # Generate AI response
#     with st.spinner("🧠 Processing..."):
#         prompt_chain = build_prompt_chain()
#         ai_response = generate_ai_response(prompt_chain)
    
#     # Add AI response to log
#     st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
#     # Rerun to update chat display
#     st.rerun()



# import streamlit as st
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     ChatPromptTemplate
# )

# # Custom CSS styling
# st.markdown("""
# <style>
#     .main {
#         background-color: #1a1a1a;
#         color: #ffffff;
#     }
#     .sidebar .sidebar-content {
#         background-color: #2d2d2d;
#     }
#     .stTextInput textarea {
#         color: #ffffff !important;
#     }
#     div[data-testid="stSidebar"] {
#         width: 350px !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# st.title("🧠 DeepSeek Code Companion")
# st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# # Sidebar for Chat History
# with st.sidebar:
#     st.header("📜 Chat History")
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []
    
#     for i, chat in enumerate(st.session_state.chat_history[::-1]):
#         if st.button(f"🔹 Chat {len(st.session_state.chat_history) - i}"):
#             st.session_state.message_log = chat["messages"]
#             st.rerun()
    
#     if st.button("🆕 New Chat"):
#         st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
#         st.rerun()

# # Initialize LLM engine
# llm_engine = ChatOllama(
#     model="deepseek-r1:1.5b",
#     base_url="http://localhost:11434",
#     temperature=0.3
# )

# # System prompt configuration
# system_prompt = SystemMessagePromptTemplate.from_template(
#     "You are an expert AI coding assistant. Provide concise, correct solutions "
#     "with strategic print statements for debugging. Always respond in English."
# )

# # Session state management
# if "message_log" not in st.session_state:
#     st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# # Chat container
# display_container = st.container()

# # Display chat messages
# with display_container:
#     for message in st.session_state.message_log:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # Chat input and processing
# user_query = st.chat_input("Type your coding question here...")

# def generate_ai_response(prompt_chain):
#     processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
#     return processing_pipeline.invoke({})

# def build_prompt_chain():
#     prompt_sequence = [system_prompt]
#     for msg in st.session_state.message_log:
#         if msg["role"] == "user":
#             prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
#         elif msg["role"] == "ai":
#             prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
#     return ChatPromptTemplate.from_messages(prompt_sequence)

# if user_query:
#     # Add user message to log
#     st.session_state.message_log.append({"role": "user", "content": user_query})
    
#     # Generate AI response
#     with st.spinner("🧠 Processing..."):
#         prompt_chain = build_prompt_chain()
#         ai_response = generate_ai_response(prompt_chain)
    
#     # Add AI response to log
#     st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
#     # Save to chat history
#     st.session_state.chat_history.append({"messages": st.session_state.message_log.copy()})
    
#     # Rerun to update chat display
#     st.rerun()




import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS styling
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    div[data-testid="stSidebar"] {
        width: 350px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar for Chat History
with st.sidebar:
    st.header("📜 Chat History")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    for i, chat in enumerate(st.session_state.chat_history[::-1]):
        question = chat["messages"][1]["content"] if len(chat["messages"]) > 1 else "(No question)"
        if st.button(f"🔹 {question}"):
            st.session_state.message_log = chat["messages"]
            st.rerun()
    
    if st.button("🆕 New Chat"):
        st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
        st.rerun()

# Initialize LLM engine
llm_engine = ChatOllama(
    model="deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Chat container
display_container = st.container()

# Display chat messages
with display_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Save to chat history
    st.session_state.chat_history.append({"messages": st.session_state.message_log.copy()})
    
    # Rerun to update chat display
    st.rerun()
