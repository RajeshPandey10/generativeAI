import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Clean black and white CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    .main-container {
        background: #ffffff;
        padding: 1rem;
        margin: 0;
        max-width: 100%;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-15px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .header-section {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 1px solid #e5e5e5;
        margin-bottom: 1rem;
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        color: #666666;
        font-weight: 400;
        margin-bottom: 1rem;
    }
    
    .header-description {
        font-size: 0.95rem;
        color: #666666;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    .stats-section {
        display: flex;
        gap: 0.5rem;
        justify-content: center;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    .stat-card {
        background: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 8px;
        padding: 1.2rem;
        text-align: center;
        min-width: 100px;
        transition: all 0.2s ease;
    }
    
    .stat-card:hover {
        border-color: #000000;
        transform: translateY(-2px);
    }
    
    .stat-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 0.3rem;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: #666666;
        font-weight: 500;
    }

    
    .chat-message {
        margin-bottom: 1.2rem;
        animation: slideIn 0.4s ease-out;
    }
    
    .user-message {
        display: flex;
        justify-content: flex-end;
        align-items: flex-start;
        gap: 0.8rem;
        margin-bottom: 1rem;
    }
    
    .ai-message {
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
        gap: 0.8rem;
        margin-bottom: 1rem;
    }
    
    .user-bubble {
        background: #000000;
        color: #ffffff;
        padding: 0.8rem 1.2rem;
        border-radius: 18px 18px 4px 18px;
        max-width: 70%;
        font-size: 0.95rem;
        line-height: 1.5;
        word-wrap: break-word;
    }
    
    .ai-bubble {
        background: #f8f8f8;
        color: #000000;
        padding: 0.8rem 1.2rem;
        border-radius: 18px 18px 18px 4px;
        max-width: 70%;
        font-size: 0.95rem;
        line-height: 1.5;
        border: 1px solid #e5e5e5;
        word-wrap: break-word;
    }
    
    .message-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        flex-shrink: 0;
        margin-top: 0.2rem;
    }
    
    .ai-avatar {
        background: #f0f0f0;
        border: 1px solid #e5e5e5;
        color: #000000;
    }
    
    .user-avatar {
        background: #000000;
        color: #ffffff;
    }
    
    .input-section {
        background: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stTextInput > div > div > input {
        border: 1px solid #e5e5e5 !important;
        border-radius: 8px !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.95rem !important;
        background: #ffffff !important;
        color: #000000 !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #000000 !important;
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stButton > button {
        background: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #000000 !important;
        border-radius: 8px !important;
        padding: 0.8rem 1.5rem !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        min-width: 80px !important;
    }
    
    .stButton > button:hover {
        background: #333333 !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }
    
    /* Specifically target form submit buttons */
    button[kind="formSubmit"] {
        background: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #000000 !important;
        border-radius: 8px !important;
        padding: 0.8rem 1.5rem !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        min-width: 80px !important;
    }
    
    button[kind="formSubmit"]:hover {
        background: #333333 !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }
    
    /* Additional targeting for Streamlit form submit buttons */
    div[data-testid="stForm"] button {
        background: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #000000 !important;
    }
    
    div[data-testid="stForm"] button:hover {
        background: #333333 !important;
        color: #ffffff !important;
    }
    
    /* Direct button text targeting */
    .stButton button p, .stButton button span, .stButton button div {
        color: #ffffff !important;
    }
    
    .typing-indicator {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        color: #666666;
        font-style: italic;
        padding: 0.8rem 1.2rem;
        background: #f8f8f8;
        border: 1px solid #e5e5e5;
        border-radius: 18px 18px 18px 4px;
        max-width: 200px;
    }
    
    .typing-dots {
        display: flex;
        gap: 3px;
    }
    
    .typing-dot {
        width: 4px;
        height: 4px;
        background: #666666;
        border-radius: 50%;
        animation: bounce 1.4s infinite;
    }
    
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes bounce {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-6px); }
    }
    
    .clear-button {
        background: #ffffff !important;
        color: #666666 !important;
        border: 1px solid #e5e5e5 !important;
        border-radius: 6px !important;
        padding: 0.5rem 1rem !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        margin-top: 1rem !important;
    }
    
    .clear-button:hover {
        border-color: #000000 !important;
        color: #000000 !important;
    }
    
    .success-message {
        background: #f8f8f8;
        color: #000000;
        border: 1px solid #e5e5e5;
        padding: 0.8rem;
        border-radius: 6px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    .error-message {
        background: #f8f8f8;
        color: #000000;
        border: 1px solid #e5e5e5;
        padding: 0.8rem;
        border-radius: 6px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    .chat-container::-webkit-scrollbar {
        width: 4px;
    }
    
    .chat-container::-webkit-scrollbar-track {
        background: #f8f8f8;
        border-radius: 2px;
    }
    
    .chat-container::-webkit-scrollbar-thumb {
        background: #cccccc;
        border-radius: 2px;
    }
    
    .chat-container::-webkit-scrollbar-thumb:hover {
        background: #999999;
    }
    
    .stDeployButton, .stDecoration, #MainMenu, footer {
        display: none !important;
    }
    
    .stApp > header {
        background-color: transparent !important;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-container {
            margin: 1rem;
            padding: 1rem;
        }
        
        .header-title {
            font-size: 2rem;
        }
        
        .user-bubble, .ai-bubble {
            max-width: 85%;
        }
        
        .stats-section {
            justify-content: center;
        }
        
        .stat-card {
            min-width: 80px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

model = load_model()

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful, friendly, and professional AI assistant.')
    ]
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'is_typing' not in st.session_state:
    st.session_state.is_typing = False

# Header section
st.markdown('''
<div class="header-section">
    <div class="header-title">AI Assistant</div>
    <div class="header-subtitle">Clean & Professional Chat Interface</div>
</div>
''', unsafe_allow_html=True)

# Stats section
user_messages = len([msg for msg in st.session_state.chat_history if isinstance(msg, HumanMessage)])
ai_messages = len([msg for msg in st.session_state.chat_history if isinstance(msg, AIMessage)])

st.markdown(f'''
<div class="stats-section">
    <div class="stat-card">
        <div class="stat-number">{st.session_state.message_count}</div>
        <div class="stat-label">Messages</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{user_messages}</div>
        <div class="stat-label">Questions</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{ai_messages}</div>
        <div class="stat-label">Responses</div>
    </div>
</div>
''', unsafe_allow_html=True)

# Chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.chat_history[1:]:  # Skip system message
    if isinstance(message, HumanMessage):
        st.markdown(f'''
        <div class="user-message">
            <div class="user-bubble">{message.content}</div>
            <div class="message-avatar user-avatar">U</div>
        </div>
        ''', unsafe_allow_html=True)
    elif isinstance(message, AIMessage):
        st.markdown(f'''
        <div class="ai-message">
            <div class="message-avatar ai-avatar">AI</div>
            <div class="ai-bubble">{message.content}</div>
        </div>
        ''', unsafe_allow_html=True)

# Show typing indicator
if st.session_state.is_typing:
    st.markdown('''
    <div class="ai-message">
        <div class="message-avatar ai-avatar">AI</div>
        <div class="typing-indicator">
            Thinking
            <div class="typing-dots">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)

# Create input form
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "",
            placeholder="Type your message...",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.form_submit_button("Send", use_container_width=True)

    # Handle form submission
    if send_button and user_input.strip():
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.message_count += 1
        st.session_state.is_typing = True
        st.rerun()

    elif send_button and not user_input.strip():
        st.markdown('<div class="error-message">Please enter a message</div>', unsafe_allow_html=True)

# Handle AI response
if st.session_state.is_typing:
    try:
        result = model.invoke(st.session_state.chat_history)
        ai_response = result.content
        
        st.session_state.chat_history.append(AIMessage(content=ai_response))
        st.session_state.is_typing = False
        
        st.markdown('<div class="success-message">Message sent</div>', unsafe_allow_html=True)
        time.sleep(0.3)
        st.rerun()
        
    except Exception as e:
        st.session_state.is_typing = False
        st.markdown(f'<div class="error-message">Error: {str(e)}</div>', unsafe_allow_html=True)

# Clear button
if st.button("Clear Chat", key="clear_chat"):
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful, friendly, and professional AI assistant.')
    ]
    st.session_state.message_count = 0
    st.session_state.is_typing = False
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Simple footer
st.markdown('''
<div style="text-align: center; padding: 0.5rem; color: #666666; font-size: 0.8rem;">
    Built with Streamlit • LangChain • OpenRouter
</div>
''', unsafe_allow_html=True)