Deskripsi Proyek

AI Resume / CV Analyzer adalah sebuah aplikasi berbasis Python yang dirancang untuk membantu pencari kerja dan perekrut dalam menganalisis Curriculum Vitae (CV) atau resume secara otomatis. Dengan memanfaatkan Natural Language Processing (NLP) dan Large Language Model (LLM), proyek ini mampu mengekstrak informasi kunci dari CV, memberikan skor kualitas, menawarkan saran perbaikan yang dipersonalisasi, serta merekomendasikan pekerjaan yang sesuai.Proyek ini dibangun dengan tujuan untuk menjadi alat yang komprehensif dan profesional, cocok untuk portofolio teknis yang menunjukkan kemampuan dalam pengembangan AI, NLP, dan integrasi LLM


```
ai_resume_analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application entry point
│   ├── parser.py           # CV text extraction from PDF
│   ├── analyzer.py         # NLP-based skill, education extraction, and scoring
│   ├── llm_service.py      # LLM integration for advanced analysis and suggestions
│   └── utils.py            # Utility functions (currently empty)
├── data/                   # Placeholder for sample data or datasets
├── models/                 # Placeholder for custom NLP models (if any)
├── tests/                  # Placeholder for unit and integration tests
├── docs/                   # Placeholder for additional documentation
├── cli.py                  # Command Line Interface for direct usage
├── generate_sample.py      # Script to generate a sample PDF CV
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables (e.g., API keys)
