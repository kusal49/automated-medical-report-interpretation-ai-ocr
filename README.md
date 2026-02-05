# 🧠 Automated Medical Report Interpretation Using AI and OCR

An AI-powered system that automatically interprets **medical test reports** from both **PDF documents and scanned images**, providing structured health insights and responsible recommendations on whether to consult a medical professional.

This project focuses on **real-world healthcare AI challenges** such as OCR reliability, safe AI usage, performance optimization, and user trust.

---

## 🚀 Key Features

- 📄 Supports **PDF medical reports**
- 🖼️ Supports **scanned / photographed medical reports (OCR)**
- 🤖 Automated medical report interpretation using AI
- ⚠️ Risk-aware insights with **doctor consultation recommendations**
- 🚫 Blocks oversized images to ensure fast and reliable OCR
- 🌙 Clean, dark-themed UI using Streamlit
- 🧩 Modular and scalable project architecture

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **AI / LLM Integration:** Groq (LLaMA-based models)  
- **OCR Engine:** PaddleOCR  
- **PDF Processing:** pdfplumber  
- **Image Processing:** Pillow, NumPy  
- **Language:** Python 3.11  

---

## 📂 Project Structure

src/
├── agents/ # AI agent orchestration and analysis logic
├── components/ # Streamlit UI components
│ └── analysis_form.py
├── utils/ # OCR, PDF parsing, risk assessment
│ ├── image_ocr.py
│ ├── pdf_extractor.py
│ └── risk_assessor.py
├── config/ # App configuration and AI prompts
├── services/ # AI service layer
├── main.py # Application entry point


---

## 🧠 How It Works

1. User uploads a **PDF or scanned image** of a medical report  
2. Text is extracted using **PDF parsing or OCR**
3. AI models interpret the extracted medical data
4. A risk assessment layer determines if medical attention may be required
5. Results are presented in a clear, user-friendly format

---

## ⚠️ Medical Disclaimer

This application provides **AI-assisted educational insights only**.  
It **does not provide medical diagnosis or treatment advice**.

Users are strongly encouraged to consult a **qualified healthcare professional** for any medical concerns.

---
