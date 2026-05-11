import os
from openai import OpenAI
from typing import Dict, Any

class LLMService:
    def __init__(self):
        # Menggunakan environment variable untuk API Key
        # Di Manus, OPENAI_API_KEY sudah tersedia secara default
        self.client = OpenAI()

    def get_suggestions_and_recommendations(self, cv_text: str, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Menggunakan LLM untuk memberikan saran perbaikan dan rekomendasi pekerjaan."""
        
        prompt = f"""
        Anda adalah seorang HR Expert dan Career Coach. 
        Analisis CV berikut dan berikan saran perbaikan serta rekomendasi pekerjaan.
        
        ISI CV:
        {cv_text[:2000]}
        
        DATA EKSTRAKSI AWAL:
        - Skill terdeteksi: {', '.join(analysis_data['skills'])}
        - Pendidikan: {', '.join(analysis_data['education'])}
        - Skor Awal: {analysis_data['score']}/100
        
        FORMAT OUTPUT HARUS JSON:
        {{
            "suggestions": ["saran 1", "saran 2", ...],
            "job_recommendations": ["pekerjaan 1", "pekerjaan 2", ...],
            "executive_summary": "ringkasan singkat profil"
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "Anda adalah asisten AI yang ahli dalam analisis CV dan rekrutmen. Berikan output dalam format JSON."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            import json
            result = json.loads(response.choices[0].message.content)
            return result
        except Exception as e:
            # Fallback jika API gagal
            return {
                "suggestions": ["Gunakan poin-poin (bullet points) untuk pengalaman kerja.", "Pastikan menyertakan angka pencapaian (misal: meningkatkan efisiensi 20%)."],
                "job_recommendations": ["Software Engineer", "Data Analyst"],
                "executive_summary": f"Analisis mendalam gagal dilakukan: {str(e)}"
                  }
