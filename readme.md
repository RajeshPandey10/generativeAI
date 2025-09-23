langchain components:

1. Model
   This component in LangChain is a core part of the framework, designed to facilitate interaction with various language models and embedding models.

   There are two types of models:
   1.Language Models(text input -> AI model -> text output)
    ├── LLMs(free-form text generation,no memory)
    └── Chat Models(optimized for multi-tun conversations, supports conversations history)

   2. Embedding Models (text input -> embedding model->[set of number which contain the meaning of text])

2.prompts:
   prompts are the input intructions or queries given to a model to guide its output.

