import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(input_csv, output_model):
    df = pd.read_csv(input_csv)

    # features e  target
    X = df[['ViewCount', 'AnswerCount', 'CommentCount']].fillna(0)
    y = (df['Score'] > df['Score'].mean()).astype(int)  # 1 para pontuação alta, 0 caso contrário

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {accuracy:.2f}")

    # Salvar o modelo
    joblib.dump(model, output_model)
    print(f"Modelo salvo em: {output_model}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Treinar modelo com dados processados")
    parser.add_argument("input_csv", help="Caminho do arquivo CSV de entrada")
    parser.add_argument("output_model", help="Caminho do arquivo de saída do modelo")
    args = parser.parse_args()

    train_model(args.input_csv, args.output_model)
