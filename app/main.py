from fastapi import FastAPI, UploadFile, File, HTTPException
from .parser import ResumeParser
from .analyzer import ResumeAnalyzer
from .llm_service import LLMService
import uvicorn

app = FastAPI(title="AI Resume / CV Analyzer API")
parser = ResumeParser()
analyzer = ResumeAnalyzer()
llm_service = LLMService()

@app.get("/")
async def root():
    return {"message": "Welcome to AI Resume Analyzer API"}

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Hanya file PDF yang didukung saat ini.")
    
    try:
        # 1. Baca file
        content = await file.read()
        
        # 2. Ekstrak teks
        raw_text = parser.extract_text_from_pdf(content)
        clean_text = parser.clean_text(raw_text)
        
        # 3. Analisis dasar (NLP)
        base_analysis = analyzer.analyze(clean_text)
        
        # 4. Analisis lanjutan (LLM)
        llm_analysis = llm_service.get_suggestions_and_recommendations(clean_text, base_analysis)
        
        # 5. Gabungkan hasil
        result = {
            "filename": file.filename,
            "score": base_analysis["score"],
            "extracted_data": {
                "skills": base_analysis["skills"],
                "education": base_analysis["education"]
            },
            "ai_analysis": llm_analysis
        }
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
