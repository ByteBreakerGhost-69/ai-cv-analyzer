import sys
import os
import json
from app.parser import ResumeParser
from app.analyzer import ResumeAnalyzer
from app.llm_service import LLMService

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <path_to_pdf>")
        return

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} tidak ditemukan.")
        return

    print(f"--- Menganalisis CV: {pdf_path} ---")
    
    parser = ResumeParser()
    analyzer = ResumeAnalyzer()
    llm_service = LLMService()

    try:
        # Baca file
        with open(pdf_path, "rb") as f:
            content = f.read()
        
        # Ekstrak & Analisis
        raw_text = parser.extract_text_from_pdf(content)
        clean_text = parser.clean_text(raw_text)
        
        print("[1/3] Mengekstrak teks...")
        base_analysis = analyzer.analyze(clean_text)
        
        print("[2/3] Menganalisis dengan NLP...")
        llm_analysis = llm_service.get_suggestions_and_recommendations(clean_text, base_analysis)
        
        print("[3/3] Selesai!\n")
        
        # Tampilkan Hasil
        print("="*30)
        print(f"SKOR CV: {base_analysis['score']}/100")
        print("="*30)
        print(f"SKILL TERDETEKSI: {', '.join(base_analysis['skills'])}")
        print(f"PENDIDIKAN: {', '.join(base_analysis['education'])}")
        print("\nSARAN PERBAIKAN:")
        for s in llm_analysis.get('suggestions', []):
            print(f"- {s}")
        print("\nREKOMENDASI PEKERJAAN:")
        for j in llm_analysis.get('job_recommendations', []):
            print(f"- {j}")
        print("\nRINGKASAN EKSEKUTIF:")
        print(llm_analysis.get('executive_summary', ''))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
