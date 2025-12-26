class IssueExtractionAgent:
    def extract(self, review_text: str):
        """
        LLM PROMPT (conceptual):
        Extract all atomic issues, requests, or feedback.
        Return short phrases.
        """
        # Simulated output for demo
        issues = []
        if "rude" in review_text:
            issues.append("delivery partner rude")
        if "cold" in review_text:
            issues.append("food arrived cold")
        if "late" in review_text:
            issues.append("delivery delay")
        return issues
