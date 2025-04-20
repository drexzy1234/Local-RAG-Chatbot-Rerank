
# Import necessary libraries
import requests
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS


# Read comments from the file
file_path = "Reddit-cooking-tips-comments.txt"

with open(file_path, "r", encoding="utf-8") as file:
    all_texts = file.readlines()

# Split content into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
all_chunks = [chunk for text in all_texts for chunk in text_splitter.split_text(text)]

# Initialize Ollama embeddings and FAISS vector store
embeddings = OllamaEmbeddings(model="snowflake-arctic-embed:335m")
vector_store = FAISS.from_texts(all_chunks, embeddings)

# Initialize Ollama LLM
llm = OllamaLLM(model="gemma3:12b", temperature=0.3)



# rerank function, sends request to API endpoint
def rerank_documents(query, docs):
    url = "http://<some-address>:<some-port-number>/v1/rerank"
    headers = {
        'Authorization': 'Bearer 123456',
        'Content-Type': 'application/json'
    }

    documents = [doc.page_content for doc in docs]

    data = {
        "model": "bge-reranker-v2-m3",
        "query": query,
        "documents": documents
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        results = response.json().get("results", [])
        # Sort documents based on the reranked relevance score
        sorted_docs = sorted(results, key=lambda x: x["relevance_score"], reverse=True)
        return [documents[res["index"]] for res in sorted_docs]
    else:
        print(f"Rerank API failed: {response.status_code}")
        return documents  # fallback to unordered original list

# Question-answering function with fallback
def ask_question_with_fallback(query):
    docs = vector_store.similarity_search(query, k=10)

    if not docs:
        return use_general_knowledge(query)

    reranked_chunks = rerank_documents(query, docs)

    # only give context that is most relevant
    context = reranked_chunks[0]
    print("\nTop relevant chunk:\n", context[:300], "...\n")

    rag_prompt = f"""
        You're a friendly cooking assistant. Use the context below to help answer the question. If the context doesn't help, just say: 'I don't know.'

        Context:
        {context}

        Question: {query}
        """

    rag_answer = llm.invoke(rag_prompt)

    if "NO_ANSWER_FOUND" in rag_answer or "don't know" in rag_answer.lower():
        return use_general_knowledge(query)

    return {"answer": rag_answer}

# General knowledge fallback
def use_general_knowledge(query):
    general_prompt = f"""
        You're a friendly kitchen expert. The user asked a question that wasn't in your notes, so you're using general knowledge.

        Begin with: 'General Knowledge:'

        Question: {query}
        """

    general_answer = llm.invoke(general_prompt)
    return {"answer": general_answer}




# Continuous interaction loop
print("    Internal RAG Q&A Bot    ")
print("Ask questions about cooking hacks and kitchen tips.")
print("This assistant is powered by a local language model and a custom knowledge base built from community-sourced cooking advice.")
print("Type 'exit' to quit.\n")


while True:
    query = input("Your question: ").strip()
    if query.lower() == "exit":
        print("Goodbye! ")
        break

    result = ask_question_with_fallback(query)
    print("\nAnswer:", result["answer"], "\n")







