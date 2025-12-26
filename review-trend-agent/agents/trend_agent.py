import pandas as pd

class TrendAggregationAgent:
    def aggregate(self, records):
        df = pd.DataFrame(records)
        trend = pd.pivot_table(
            df,
            index="topic",
            columns="date",
            aggfunc="size",
            fill_value=0
        )
        return trend
