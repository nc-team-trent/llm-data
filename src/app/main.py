"""
FastAPI app for LLM-based text transformation.
"""

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse, PlainTextResponse
from app.processor import transform_text

app = FastAPI(
    title="LLM Transformer API",
    description="API to summarize or describe raw text using OpenAI GPT models.",
    version="1.0.0"
)


@app.get("/transform/", response_class=PlainTextResponse)
async def transform_get_info():
    return (
        "📌 This API endpoint only accepts POST requests.\n\n"
        "To use it, send a POST request with the following form-data fields:\n\n"
        "  - file: a plain text (.txt) file to transform\n"
        "  - mode: 'summary' or 'description' (default: summary)\n\n"
        "Example via curl:\n\n"
        "curl -X POST http://localhost:8000/transform/ \\\n"
        "  -F \"file=@example.txt\" \\\n"
        "  -F \"mode=summary\"\n\n"
        "You can also test it interactively at: http://localhost:8000/docs"
    )



@app.post("/transform/")
async def transform(
    file: UploadFile = File(...),
    mode: str = Form("summary")
):
    """
    Transform uploaded text file using the selected mode.

    Args:
        file: Text file to process.
        mode: 'summary' or 'description'.

    Returns:
        JSON with list of transformed outputs.
    """
    try:
        contents = await file.read()
        text = contents.decode("utf-8")
        results = transform_text(text, mode=mode)
        return JSONResponse(content={"mode": mode, "results": results})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
