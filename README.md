**Update 14th November 2024**: Check the branch [`feature/optimization`](https://github.com/sankalp1999/code_qa/tree/feature/optimization) which runs 2.5x faster than this branch's code (what you saw in the demo video).
The optimized branch achieves 2.5x faster performance (10-20 seconds range) through two key improvements:

1. **Optimized Token Management** - Reduced HYDE max tokens to 400 and HYDE-v2 to 768. Keeps hallucinated output concise while maintaining relevance. Result: ~5-10 seconds saved

2. **Enhanced Context Processing** - Implemented SambaNova Llama 3.1 8b (1000 tok/s) for context filtering and changed gpt4o -> SambaNova Llama 3.1-70b (400 tok/s) for chat responses. Improved context relevance and processing speed. Result: ~20 seconds saved

Worst case scenario codeQA works under 20 seconds as compared to the previous 40 seconds.

## What is CodeQA?

A powerful code search and query system that lets you explore codebases using natural language. Ask questions about your code and get contextual answers powered by LanceDB, OpenAI gpt4o-mini/gpt4o and Answerdotai's colbert-small-v1 reranker. Supports Python, Rust, JavaScript and Java with a clean, minimal UI.

Blog Links:

[An attempt to build cursor's @codebase feature - RAG on codebases - part 1](https://blog.lancedb.com/rag-codebase-1/)

[An attempt to build cursor's @codebase feature - RAG on codebases - part 2](https://blog.lancedb.com/building-rag-on-codebases-part-2/)


CodeQA helps you understand codebases by:
- Extracting code structure and metadata using tree-sitter AST parsing
- Indexing the code chunks using OpenAI/Jina embeddings and storing them in LanceDB
- Enabling natural language searches across the codebase by using @codebase in queries
- Providing context-aware answers with references
- Supporting interactive chat-based code exploration


## Prerequisites

- Python 3.6 or higher
- Redis server running on `localhost:6379`

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sankalp1999/code_qa.git
   ```

2. Navigate to the project directory:

   ```bash
   cd code_qa
   ```

3. Set up a Python virtual environment:

 Treesitter is supported >=3.8 to 3.11

   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the redis server
```
redis-server
```

## Configuration
You only need to set the OpenAI API key. Jina API key is optional, if you want to use Jina embeddings instead of OpenAI.

Create a .env file and add the following:

```
OPENAI_API_KEY="your-openai-api-key"
JINA_API_KEY="your-jina-api-key"
```
## Building the Codebase Index

To build the index for the codebase, run the following script:


```
chmod +x index_codebase.sh
```

```bash
./index_codebase.sh <absolute_path_to_codebase>
```

This will parse the codebase to get the code chunks, generate embeddings, references and store them in LanceDB.

## Usage

To start the server

```bash
python app.py <folder_path>
```

For example, to analyze a JavaScript project located in `/Users/sankalp/Documents/code2prompt/twitter-circle`, run:

```bash
python app.py /Users/sankalp/Documents/code2prompt/twitter-circle
```

Once the server is running, open a web browser and navigate to `http://localhost:5001` to access the code search and query interface.

Use @codebase keyword in queries to fetch context via embeddings 
Enable re-ranking option to get more relevant results

## MCP Server Integration

The MCP server now supports storage, retrieval/search, and search completions. The following endpoints are available:

- `/mcp/store`: Endpoint for storing data.
- `/mcp/retrieve`: Endpoint for retrieving data.
- `/mcp/search`: Endpoint for search completions.

## Technologies Used

- Flask: server and UI
- Treesitter: parsing methods, classes, constructor declarations in a language agnostic way using the abstract syntax tree
- LanceDB: vector db for storing and searching code embeddings
- Redis: in-memory data store for caching and session management
- OpenAI, Jina for chat functionalities and colbert-small-v1 for reranker
- MCP: Model Context Protocol for server integration

## License

This project is licensed under the [MIT License](LICENSE).
