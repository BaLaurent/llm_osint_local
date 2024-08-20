from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel

LLMModel = BaseChatModel

# I use a fixed name for the models to use so you can change it by simply recreating a model from a file using ollama create
default_fast_llm_options = dict(base_url="http://localhost:11434/v1", api_key="bidon" ,model_name="llm_osint_fast", request_timeout=120, max_retries=10, temperature=0.7)
default_llm_options = dict(base_url="http://localhost:11434/v1", api_key="bidon", model_name="llm_osint", request_timeout=120, max_retries=10, temperature=0.7)


def get_default_fast_llm() -> LLMModel:
    chat = ChatOpenAI(**default_fast_llm_options)
    return chat


def get_default_llm() -> LLMModel:
    chat = ChatOpenAI(**default_llm_options)
    return chat
