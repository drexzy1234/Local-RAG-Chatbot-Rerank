
# Local RAG Chatbot with Rerank

A internal Retrieval-Augmented Generation (RAG) assistant that answers your questions using a local Embedding model and LLM model pulled via [Ollama](https://ollama.com), Rerank model downloaded from [Hugging Face](https://huggingface.co/) and run on [vLLM](https://docs.vllm.ai/en/latest/). 

This version is trained on community-sourced cooking tips, but you can customize it to your own content easily.

## Features

- Fully local RAG setup (no need for cloud api)
- Uses Ollama-compatible models for both embedding and generation
- Incorporate huggingface.co rerank model, run on vLLM
- Built with Python, using LangChain and FAISS library
- Utilized the power of embedding models and rerank models to enhance knowledge retrieval accuracy
- Interactive terminal interface
- Fallback to general knowledge if answer isn't found in local data

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- pull LLM model and Embedding model from Ollama to local (after pulling, update line 18 and 22 of the code accordingly)
- [vLLM](https://docs.vllm.ai/en/latest/) installed and running
- install huggingface_hub
- download the reranker model 'bge-reranker-v2-m3' from huggingface.co with huggingface-cli command

Install Python library dependencies:
```bash
pip install langchain langchain-community langchain-ollama faiss-cpu requests json
```

Check if the knowledge base file is in the same directory as "internal-rag-cookbot.py". I have named mine "cooking-tips-comments.txt", the name and contents of the file can be changed. 

## How It Works

This project uses Retrieval-Augmented Generation (RAG), which combines a embedding vector database created from your content, a reranker to rank relevance of content, along with a language model to provide more accurate and contextual answers.

### Embedding the Content

- The text file (cooking-tips-comments.txt) is our knowledge base file.

- The contents of the file is converted by projecting the **high-dimensional space of initial data vectors** into a **lower-dimensional space** using a local embedding model (in the code provided, we used 'snowflake-arctic-embed:335m' from Ollama).

- These vectors capture the semantic meaning of the text — two similar tips will have similar embeddings. 

### Storing in a Vector Database

- The vectors are stored in FAISS, a fast, in-memory vector store that supports efficient similarity search.

- This lets the system quickly find the most relevant chunks of text when a new question is asked.

### Retrieving Context from Embedding

- When you ask a question, it is also embedded into a vector on the spot for the LLM model to actully understand your question.

- FAISS compares this vector to the ones in the vector database and returns the top matching text chunks. The specific phrase we use here is **"top-k"**.

- **top-k** is the number of top matching entries we retrieve from the embedding using a fast but rough similarity search. If the number k is too small, we might miss out on some relevant information; if it's too large, we're likely getting too much unrelated content. In the code provided we are using **"top-k 10"**, which is a good number compared to our data size. In the case for using a much larger knowledge base, a bigger k is prefered (some knowledge bases are so big that they use k = 100). 

### Rerank Top-K Content

- These chunks are sent to a rerank API using 'bge-reranker-v2-m3' to reorder them by relevance.

- Only the top result is used as context for generation.

### Generate The Answer

- The contxt is passed to the LLM (in the provided code we used 'gemma3:12b') along with our question.

- The LLM uses this context to generate a more accurate, grounded, and helpful response.

## Usage

Run the following command in the directory of the python file. 
```bash
python internal-rag-cookbot.py
```

Type in what you want to ask when the prompt "Your question: " shows up. 

Example use of the code:
```bash
<some-user-directory>:~$ python chatbot-rerank.py
    Internal RAG Q&A Bot    
Ask questions about cooking hacks and kitchen tips.
This assistant is powered by a local language model and a custom knowledge base built from community-sourced cooking advice.
Type 'exit' to quit.

Your question:
```

Here we enter our question:
```bash
Your question: i am trying to make chocolate chip cookies
```

The answer responded is:
```bash
Top relevant chunk:
 Not mine, but my wife browns the butter before she adds it to chocolate chip cookie dough and they're the best freakin' cookies I've ever eaten! ...


Answer: That's great! My wife browns the butter before adding it to her chocolate chip cookie dough, and it makes a huge difference – they're amazing! You should try it! 

Your question: 
```

Now we can type "exit" to close this chatbot: 

```bash
Your question: exit
Goodbye!
```




