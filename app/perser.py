import io
from pypdf import PdfReader

class ResumeParser:
    @staticmethod
    def extract_text_from_pdf(file_content: bytes) -> str:
        """Mengekstrak teks dari file PDF bytes."""
        try:
            reader = PdfReader(io.BytesIO(file_content))
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Gagal mengekstrak teks dari PDF: {str(e)}")

    @staticmethod
    def clean_text(text: str) -> str:
        """Membersihkan teks dari karakter yang tidak perlu."""
        # Implementasi pembersihan teks sederhana
        import re
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
