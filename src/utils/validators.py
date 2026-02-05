def validate_pdf(file, max_size_mb):
    if file.size > max_size_mb * 1024 * 1024:
        return False, "File exceeds size limit"
    if not file.name.lower().endswith(".pdf"):
        return False, "Only PDF files allowed"
    return True, None
