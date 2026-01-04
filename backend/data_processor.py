import pandas as pd
import hashlib
import json

class DataProcessor:

    def load_csv(self, path):
        return pd.read_csv(path)

    def clean(self, df):
        df.columns = df.columns.str.strip()
        df = df.fillna(0)
        return df

    def calculate_carbon(self, area, sequestration):
        # Simple MRV logic
        return area * sequestration

    def generate_hash(self, data):
        data_string = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def process_sites(self, df):
        sites = []

        for _, row in df.iterrows():
            total_carbon = self.calculate_carbon(
                row["area_ha"], row["annual_sequestration"]
            )

            site = (
                str(row["site_id"]),
                str(row["measurement_date"]),
                str(row["species"]),
                float(row["area_ha"]),
                float(row["annual_sequestration"]),
                float(total_carbon)
            )

            sites.append(site)

        return sites
