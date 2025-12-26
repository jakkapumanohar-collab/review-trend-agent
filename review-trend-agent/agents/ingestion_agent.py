class ReviewIngestionAgent:
    def ingest(self, reviews: list, date: str):
        return [
            {
                "review_id": r["id"],
                "date": date,
                "text": r["text"]
            } for r in reviews
        ]
