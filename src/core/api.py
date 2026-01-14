from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.graph import create_email_graph

app = FastAPI(title="EmailAssistant API", description="Backend for AI-powered Email Management")

class EmailRequest(BaseModel):
    content: str

class EmailResponse(BaseModel):
    category: str
    draft_reply: str

@app.post("/process-email", response_model=EmailResponse)
async def process_email(request: EmailRequest):
    try:
        graph = create_email_graph()
        initial_state = {
            "email_content": request.content,
            "messages": [],
            "category": "",
            "draft_reply": "",
            "context": []
        }
        
        # Run the graph synchronously for simplicity in this demo
        result = graph.invoke(initial_state)
        
        return EmailResponse(
            category=result["category"],
            draft_reply=result["draft_reply"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
