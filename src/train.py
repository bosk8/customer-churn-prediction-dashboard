from src.data import load_data, prepare_data, get_column_types
from src.model import create_preprocessor, train_model, save_artifacts
from src.config import ARTIFACTS

def main():
    """
    Main function to run the training pipeline.
    """
    ARTIFACTS.mkdir(exist_ok=True, parents=True)

    df = load_data()
    X, y = prepare_data(df)
    num_cols, cat_cols = get_column_types(X)

    preprocessor = create_preprocessor(num_cols, cat_cols)
    model, auc = train_model(X, y, preprocessor)

    save_artifacts(model, auc)

    print(f"\nBest AUC: {auc:.4f}")
    print(f"Model saved to {ARTIFACTS / 'model.joblib'}")
    print(f"Metrics saved to {ARTIFACTS / 'metrics.json'}")

if __name__ == "__main__":
    main()
