import os
import pickle


def create_mock_faiss():
    """
    Creates a mock FAISS index structure so the data folder isn't empty.
    In a real scenario, the user would run init_db.py with their API key.
    """
    data_dir = "data/faiss_index"
    os.makedirs(data_dir, exist_ok=True)

    # FAISS usually creates an index.faiss and index.pkl
    # We'll create dummy files to show the structure
    with open(os.path.join(data_dir, "index.faiss"), "wb") as f:
        f.write(b"MOCK_FAISS_INDEX_DATA")

    with open(os.path.join(data_dir, "index.pkl"), "wb") as f:
        pickle.dump({"mock": "data"}, f)

    print(f"Mock FAISS index created at {data_dir}")


if __name__ == "__main__":
    create_mock_faiss()
