import sys
import argparse
from src.core.graph import create_email_graph

def main():
    parser = argparse.ArgumentParser(description="EmailAssistant: AI-powered Email Management for Construction")
    parser.add_argument("--email", type=str, help="The content of the email to process")
    args = parser.parse_args()

    if not args.email:
        print("Please provide email content using --email \"Your email content here\"")
        sys.exit(1)

    print("\n--- EmailAssistant Processing ---\n")
    
    graph = create_email_graph()
    initial_state = {
        "email_content": args.email,
        "messages": [],
        "category": "",
        "draft_reply": "",
        "context": []
    }

    final_state = graph.invoke(initial_state)

    print(f"Category: {final_state['category']}")
    print("-" * 30)
    print("Draft Reply:")
    print(final_state['draft_reply'])
    print("-" * 30)

if __name__ == "__main__":
    main()
