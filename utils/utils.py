from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


load_dotenv()

# gemini llm
def get_llm():
    return ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("api_key")
)

# Output Parser
str_parse=StrOutputParser()

# prompt
def get_prompt():
    return PromptTemplate(
    template="""
    You are a helpful and polite AI assistant that always replies **only in Hindi**.
    No matter what the user asks — even if it's in English — your response must be fully in Hindi.
    Keep the tone natural, respectful, and conversational.
    The assistant should sound calm, warm, and empathetic in tone.

    User's query: {user_query}

    Chat History: {chat_history}

    Your response (in Hindi only):
    """,
    input_variables=['user_query','chat_history']
    )