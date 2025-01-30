import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_curve, auc

def save_metrics(metrics, output_path):
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"Métricas salvas em: {output_path}")

def save_plot(data, output_path):
    plt.figure()
    plt.plot(data["fpr"], data["tpr"], label=f"AUC = {data['auc']:.2f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("Taxa de Falsos Positivos")
    plt.ylabel("Taxa de Verdadeiros Positivos")
    plt.title("Curva ROC")
    plt.legend(loc="lower right")
    plt.savefig(output_path)
    print(f"Gráfico salvo em: {output_path}")

def train_model(input_csv, output_model, metrics_path, plot_path):
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

    # Calcular Curva ROC
    y_scores = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    roc_auc = auc(fpr, tpr)

    # Salvar métricas e gráfico
    metrics = {"accuracy": accuracy, "auc": roc_auc}
    save_metrics(metrics, metrics_path)

    roc_data = {"fpr": fpr.tolist(), "tpr": tpr.tolist(), "auc": roc_auc}
    save_plot(roc_data, plot_path)

    # Salvar o modelo
    joblib.dump(model, output_model)
    print(f"Modelo salvo em: {output_model}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Treinar modelo e salvar métricas e gráfico")
    parser.add_argument("input_csv", help="Caminho do arquivo CSV de entrada")
    parser.add_argument("output_model", help="Caminho do modelo treinado")
    parser.add_argument("metrics_path", help="Caminho do arquivo de métricas")
    parser.add_argument("plot_path", help="Caminho do gráfico ROC")
    args = parser.parse_args()

    train_model(args.input_csv, args.output_model, args.metrics_path, args.plot_path)
