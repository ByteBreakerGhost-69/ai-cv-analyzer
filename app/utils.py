import os
import re
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_file_extension(filename: str, allowed_extensions: list = ['.pdf']) -> bool:
    """Memvalidasi apakah ekstensi file diperbolehkan."""
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_extensions

def format_currency(value: float) -> str:
    """Contoh fungsi utilitas untuk memformat mata uang (jika nanti ada fitur gaji)."""
    return f"Rp {value:,.2f}"

def sanitize_filename(filename: str) -> str:
    """Membersihkan nama file dari karakter berbahaya."""
    return re.sub(r'[^\w\s.-]', '', filename).strip().replace(' ', '_')

def get_env_variable(key: str, default: str = None) -> str:
    """Mengambil environment variable dengan aman."""
    return os.getenv(key, default)
