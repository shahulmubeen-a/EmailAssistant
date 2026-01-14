# EmailAssistant: AI-Powered Email Management for Construction

## Project Overview

EmailAssistant is an intelligent email management system designed to streamline communication within the construction industry. Leveraging advanced AI techniques, particularly Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), it automates the categorisation of incoming emails and drafts professional, context-aware replies. This project showcases expertise in building scalable AI agents, MLOps practices, and domain-specific AI applications, aligning with the requirements for a modern AI Engineer role.

## Features

*   **Intelligent Email Categorisation**: Automatically classifies emails into construction-specific categories such as Procurement, Safety, Planning, and General.
*   **Context-Aware Reply Drafting**: Utilises a RAG system with a FAISS vector database to retrieve relevant information from a knowledge base (e.g., policy documents, vendor lists) to inform email replies.
*   **Stateful Multi-Agent Orchestration**: Built with **LangGraph** to manage complex email processing workflows, demonstrating the ability to design and implement scalable AI agents.
*   **FastAPI Backend**: Provides a robust and asynchronous API for integrating EmailAssistant into various applications.
*   **Command-Line Interface (CLI)**: Offers a simple way to process emails directly from the terminal.
*   **Construction Domain Focus**: Includes sample data and categorisation logic tailored for construction-related communications, highlighting domain-specific AI application development.
*   **CI/CD Integration**: Includes GitHub Actions workflows for automated linting, formatting checks, and testing.
*   **Containerisation**: Fully Dockerised for consistent deployment across different environments.

## Architecture

The EmailAssistant employs a modular architecture, with key components including:

1.  **EmailAssistantAgents**: A collection of AI agents responsible for specific tasks:
    *   **Categorisation Agent**: Determines the subject matter of an email.
    *   **Retrieval Agent**: Fetches relevant context from the knowledge base.
    *   **Drafting Agent**: Generates a reply based on the email content and retrieved context.
2.  **LangGraph Workflow**: Orchestrates the interaction between these agents, defining the flow of email processing from categorisation to final draft.
3.  **EmailRAG (Retrieval-Augmented Generation)**: Manages the FAISS vector store, enabling efficient retrieval of domain-specific information.
4.  **FastAPI**: Serves as the backend API, providing endpoints for email processing.
5.  **CLI**: A command-line interface for direct interaction and testing.

```mermaid
graph TD
    A[Incoming Email]
    B{Categorise Email}
    C{Retrieve Context (FAISS)}
    D[Draft Reply]
    E[Outgoing Draft]

    A --> B
    B --> C
    C --> D
    D --> E

    subgraph LangGraph Workflow
        B
        C
        D
    end

    subgraph Backend/CLI
        A
        E
    end
```

## Setup and Installation

To set up EmailAssistant, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/EmailAssistant.git
    cd EmailAssistant
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -e .
    ```
    Alternatively, you can install from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

5.  **Initialise the FAISS database**:
    The `data/faiss_index` directory contains a mock FAISS index for demonstration purposes. In a real-world scenario, you would generate this index using your own data and an OpenAI API key.

    To generate a real FAISS index with sample construction domain knowledge, ensure your `OPENAI_API_KEY` is set in the `.env` file and run:
    ```bash
    python scripts/init_db.py
    ```
    If you wish to re-generate the mock index (e.g., after cleaning the `data` folder), you can run:
    ```bash
    python scripts/mock_init_db.py
    ```


## CI/CD and Deployment

### GitHub Actions
The project includes a `.github/workflows/ci.yml` file that automatically runs:
- **Linting**: Using `flake8` to ensure code quality.
- **Formatting**: Using `black` to maintain consistent code style.
- **Testing**: Using `pytest` to verify application functionality.

### Docker
To run the application using Docker:

1. **Build the image**:
   ```bash
   docker build -t email-assistant .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 --env-file .env email-assistant
   ```

## Usage

### Command-Line Interface (CLI)

To process an email using the CLI:

```bash
emailassistant --email "The latest steel order from Project Alpha is delayed by two days. Please advise on the impact to the schedule."
```

### FastAPI Backend

1.  **Run the FastAPI application**:
    ```bash
    uvicorn src.core.api:app --host 0.0.0.0 --port 8000
    ```

2.  **Access the API**: The API will be available at `http://localhost:8000`.
    You can interact with it using tools like `curl` or Postman, or through the automatically generated OpenAPI documentation at `http://localhost:8000/docs`.

    Example `curl` request:
    ```bash
    curl -X POST "http://localhost:8000/process-email" \
         -H "Content-Type: application/json" \
         -d 
    ```

## Future Enhancements

**Note on `data/faiss_index`**: For this demonstration, a mock FAISS index is included in the repository to ensure the project is immediately runnable. In a production environment, this directory would typically be excluded from version control (`.gitignore`) and generated as part of the deployment process using actual data and secure API keys.

*   Integration with Gmail API for real-time email fetching and sending.
*   Advanced user authentication and authorisation.
*   Web-based UI for enhanced user experience.
*   Support for additional domain-specific knowledge bases.
*   Deployment to cloud platforms (e.g., AWS, Azure, GCP) with CI/CD pipelines.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any queries or suggestions, please contact [Your Name/Email].
