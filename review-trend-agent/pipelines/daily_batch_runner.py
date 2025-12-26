from agents.ingestion_agent import ReviewIngestionAgent
from agents.preprocessing_agent import PreprocessingAgent
from agents.extraction_agent import IssueExtractionAgent
from agents.canonicalization_agent import TopicCanonicalizationAgent
from agents.trend_agent import TrendAggregationAgent

def run_daily_batch(reviews, date):
    ingest = ReviewIngestionAgent()
    prep = PreprocessingAgent()
    extract = IssueExtractionAgent()
    canon = TopicCanonicalizationAgent("ontology/topic_registry.json")

    ingested = ingest.ingest(reviews, date)
    cleaned = prep.clean(ingested)

    records = []
    for r in cleaned:
        issues = extract.extract(r["text"])
        for issue in issues:
            topic = canon.canonicalize(issue)
            records.append({
                "topic": topic,
                "date": date
            })

    return records
