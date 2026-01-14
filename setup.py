from setuptools import setup, find_packages

setup(
    name="emailassistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "langchain",
        "langgraph",
        "openai",
        "faiss-cpu",
        "python-dotenv",
        "loguru",
        "google-api-python-client",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "google-auth",
    ],
    entry_points={
        "console_scripts": [
            "emailassistant=core.cli:main",
        ],
    },
)
