import spacy
import re
from typing import List, Dict, Any

class ResumeAnalyzer:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except:
            # Fallback jika model belum terdownload
            import os
            os.system("python3 -m spacy download en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")
            
        # Daftar skill sederhana sebagai referensi dasar
        self.common_skills = [
            "python", "java", "javascript", "react", "node.js", "sql", "nosql", 
            "docker", "kubernetes", "aws", "azure", "machine learning", "data science",
            "project management", "agile", "scrum", "git", "linux", "rest api", "fastapi"
        ]

    def extract_skills(self, text: str) -> List[str]:
        """Mengekstrak skill menggunakan pencocokan pola sederhana dan NLP."""
        text_lower = text.lower()
        found_skills = []
        for skill in self.common_skills:
            if re.search(rf"\b{re.escape(skill)}\b", text_lower):
                found_skills.append(skill)
        return list(set(found_skills))

    def extract_education(self, text: str) -> List[str]:
        """Mengekstrak informasi pendidikan (Sederhana)."""
        edu_keywords = ["Bachelor", "Master", "PhD", "University", "College", "Degree", "Sarjana", "Magister"]
        doc = self.nlp(text)
        education = []
        for sent in doc.sents:
            if any(kw.lower() in sent.text.lower() for kw in edu_keywords):
                education.append(sent.text.strip())
        return education[:3] # Ambil 3 teratas

    def calculate_score(self, extracted_data: Dict[str, Any]) -> int:
        """Menghitung skor kualitas CV (0-100)."""
        score = 0
        
        # Bobot scoring
        # 1. Skill (40%)
        num_skills = len(extracted_data.get("skills", []))
        score += min(num_skills * 5, 40)
        
        # 2. Education (20%)
        if extracted_data.get("education"):
            score += 20
            
        # 3. Panjang teks/Kelengkapan (20%)
        text_length = len(extracted_data.get("raw_text", ""))
        if text_length > 500:
            score += 20
        elif text_length > 200:
            score += 10
            
        # 4. Pengalaman (Asumsi sederhana jika ada kata kunci kerja) (20%)
        exp_keywords = ["experience", "work", "job", "intern", "pengalaman", "bekerja"]
        if any(kw in extracted_data.get("raw_text", "").lower() for kw in exp_keywords):
            score += 20
            
        return score

    def analyze(self, text: str) -> Dict[str, Any]:
        """Menjalankan analisis lengkap."""
        skills = self.extract_skills(text)
        education = self.extract_education(text)
        
        data = {
            "raw_text": text,
            "skills": skills,
            "education": education
        }
        
        score = self.calculate_score(data)
        
        return {
            "skills": skills,
            "education": education,
            "score": score
          }
