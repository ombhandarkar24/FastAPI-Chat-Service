# FastAPI Chat Service

This is a backend service built with FastAPI for processing URLs and PDF documents, and providing a chat interface to query the processed content.

## Features
- Scrape and store content from a URL.
- Extract and store content from a PDF file.
- Query the stored content via a chat interface.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn app.main:app --reload`
4. Open `http://127.0.0.1:8000` in your browser.
