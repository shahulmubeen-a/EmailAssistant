# EmailAssistant: AI-Powered Email Management for Construction

## Project Overview

EmailAssistant is an intelligent backend system designed to streamline communication within the construction industry. By leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), it automates the categorisation of incoming emails and drafts professional, context-aware replies. This project demonstrates expertise in building scalable AI agents, MLOps practices, and domain-specific AI applications, specifically tailored for an AI Engineer role.

## Core Features

*   **Intelligent Email Categorisation**: Automatically classifies emails into construction-specific categories such as Procurement, Safety, Planning, and General business communication.
*   **Context-Aware RAG System**: Utilises a **FAISS** vector database to retrieve relevant information from a construction knowledge base (e.g., site protocols, vendor lists) to inform and ground email replies.
*   **Stateful Agent Orchestration**: Built with **LangGraph** to manage multi-step email processing workflows, ensuring robust and scalable agentic behaviour.
*   **Production-Ready Backend**: A high-performance **FastAPI** service providing asynchronous endpoints for seamless integration.
*   **Robust CLI**: A dedicated command-line interface for direct interaction, testing, and rapid prototyping.
*   **CI/CD & MLOps**: Includes automated GitHub Actions for linting, formatting, and testing, alongside full Dockerisation for consistent deployment.

## Technical Architecture

The system is built with a modular approach to ensure maintainability and scalability:

1.  **LangGraph Workflow**: Orchestrates the logic between the Categorisation, Retrieval, and Drafting agents.
2.  **FAISS Vector Store**: Handles the storage and similarity search of domain-specific documents to provide accurate context for the LLM.
3.  **FastAPI Layer**: Exposes the agentic workflow as a RESTful API, supporting asynchronous processing of email requests.
4.  **CLI Utility**: Provides a direct entry point for processing individual emails via the terminal.

## Setup and Installation

### 1. Environment Setup
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your-username/EmailAssistant.git
cd EmailAssistant
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Dependency Installation
Install the package and its requirements:
```bash
pip install -e .
```

### 3. Configuration
Create a `.env` file in the root directory with your OpenAI API key:
```env
OPENAI_API_KEY="your_openai_api_key_here"
```

### 4. Data Initialisation
The `data/faiss_index` directory contains a mock index for immediate demonstration. To generate a real index with construction domain knowledge, run:
```bash
python scripts/init_db.py
```

## Usage

### Command-Line Interface (CLI)
Process an email directly from your terminal:
```bash
emailassistant --email "The site inspection for Project Alpha is scheduled for Tuesday. Please confirm the safety officer's attendance."
```

### FastAPI Backend
Start the API server:
```bash
uvicorn src.core.api:app --host 0.0.0.0 --port 8000
```
The API documentation will be available at `http://localhost:8000/docs`.

## CI/CD and Deployment

### GitHub Actions
The project includes automated workflows in `.github/workflows/ci.yml` for:
*   **Linting**: Ensuring code quality with `flake8`.
*   **Formatting**: Maintaining style consistency with `black`.
*   **Testing**: Verifying functionality with `pytest`.

### Docker
To containerise and run the application:
```bash
docker build -t email-assistant .
docker run -p 8000:8000 --env-file .env email-assistant
```

## Future Enhancements
*   Integration with the Gmail API for automated inbox monitoring.
*   Support for multi-modal RAG (e.g., processing construction site images or PDFs).
*   Advanced multi-agent coordination for complex procurement workflows.

## License
This project is licensed under the MIT License.
