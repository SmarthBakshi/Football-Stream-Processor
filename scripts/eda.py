from football_stream_processor.utils.eda_utils import PassDataEDA, add_engineered_features
import pandas as pd

def main():
    df = pd.read_pickle(".pickle/pass_data.pkl")
    df = add_engineered_features(df)
    eda = PassDataEDA(df)
    eda.missing_values()
    eda.class_distribution()
    eda.data_types()
    df_clean = eda.remove_duplicates()
    eda.eda_visualizations()

if __name__ == "__main__":
    main()