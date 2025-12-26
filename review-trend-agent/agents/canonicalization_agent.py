import json
from difflib import SequenceMatcher

class TopicCanonicalizationAgent:
    def __init__(self, registry_path):
        with open(registry_path) as f:
            self.registry = json.load(f)

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def canonicalize(self, issue):
        for topic in self.registry:
            if self.similarity(issue, topic["label"]) > 0.75:
                topic["aliases"].append(issue)
                return topic["label"]

        # New topic
        new_topic = {
            "label": issue,
            "aliases": [issue]
        }
        self.registry.append(new_topic)
        return issue
