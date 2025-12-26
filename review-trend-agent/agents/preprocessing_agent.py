import re

class PreprocessingAgent:
    def clean(self, reviews):
        cleaned = []
        for r in reviews:
            text = r["text"].lower()
            text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
            if len(text.split()) > 3:
                cleaned.append({**r, "text": text})
        return cleaned
