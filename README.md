# Local RAG Chatbot Rerank 🤖

![GitHub release](https://img.shields.io/badge/release-v1.0.0-blue?style=flat-square&logo=github)

Welcome to the **Local RAG Chatbot Rerank** repository! This Python project deploys a Local Retrieval-Augmented Generation (RAG) chatbot using the Ollama API and vLLM API. The chatbot refines answers with an internal RAG knowledge base, employing both Embedding and Rerank models to enhance the accuracy of context provided to LLM models.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Local Deployment**: Run the chatbot on your local machine without the need for external servers.
- **Improved Accuracy**: Uses Embedding and Rerank models to ensure high-quality responses.
- **Flexible API Integration**: Leverages Ollama and vLLM APIs for robust performance.
- **User-Friendly Interface**: Simple command-line interface for easy interaction.
- **Open Source**: Fully open for contributions and enhancements.

## Technologies Used

- **Python**: The primary programming language for the project.
- **Ollama API**: For generating responses based on user input.
- **vLLM API**: For managing language model interactions.
- **Embeddings**: Techniques for converting text into numerical vectors.
- **Rerank Models**: Algorithms for refining and improving response accuracy.

## Installation

To get started with the Local RAG Chatbot Rerank, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/drexzy1234/Local-RAG-Chatbot-Rerank.git
   cd Local-RAG-Chatbot-Rerank
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   Visit the [Releases section](https://github.com/drexzy1234/Local-RAG-Chatbot-Rerank/releases) to download the latest version. Execute the necessary files as per the instructions provided there.

## Usage

After installation, you can start using the Local RAG Chatbot Rerank:

1. **Run the Chatbot**:
   ```bash
   python main.py
   ```

2. **Interact with the Chatbot**:
   Follow the prompts in the command line to ask questions and receive responses.

3. **Stop the Chatbot**:
   To stop the chatbot, simply press `Ctrl + C`.

## How It Works

The Local RAG Chatbot Rerank uses a combination of Retrieval-Augmented Generation techniques and local model deployment. Here’s a brief overview of the workflow:

1. **User Input**: The user provides a query through the command line interface.
2. **Embedding Generation**: The input is converted into embeddings using a pre-trained model.
3. **Retrieval**: The system retrieves relevant information from the internal RAG knowledge base.
4. **Reranking**: The retrieved answers are reranked based on relevance and accuracy.
5. **Response Generation**: The final response is generated using the Ollama and vLLM APIs, ensuring a coherent and contextually appropriate answer.

### Example Interaction

Here’s a quick example of how a conversation might look:

```
User: What is the capital of France?
Chatbot: The capital of France is Paris.
```

## Contributing

We welcome contributions from the community! If you want to help improve the Local RAG Chatbot Rerank, follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or suggestions, feel free to reach out:

- **Email**: your.email@example.com
- **GitHub**: [drexzy1234](https://github.com/drexzy1234)

---

Thank you for checking out the Local RAG Chatbot Rerank! We hope you find it useful. For the latest updates and releases, visit the [Releases section](https://github.com/drexzy1234/Local-RAG-Chatbot-Rerank/releases).