import pandas as pd
import argparse

def process_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    limite_nulos = 0.6
    colunas_para_remover = df.columns[df.isnull().mean() > limite_nulos]

    df = df.drop(columns=colunas_para_remover)

    colunas_irrelevantes = ['Id', 'ContentLicense', 'OwnerDisplayName','OwnerUserId','LastEditorUserId']
    colunas_para_remover = [col for col in colunas_irrelevantes if col in df.columns]

    # Remover colunas irrelevantes
    df = df.drop(columns=colunas_para_remover)

    df['AcceptedAnswerId'] = df['AcceptedAnswerId'].fillna(0)


    # Converter colunas de data para datetime
    datas = ['CreationDate', 'LastEditDate', 'LastActivityDate']
    for coluna in datas:
        df[coluna] = pd.to_datetime(df[coluna])

    ## Criar novas features baseadas nas datas
    df['CreationYear'] = df['CreationDate'].dt.year
    df['CreationMonth'] = df['CreationDate'].dt.month
    df['CreationDay'] = df['CreationDate'].dt.day


    # Remover os '<>' e transformar em listas
    df['Tags'] = df['Tags'].str.replace('<', '').str.split('>')[:-1]
        
    df.to_csv(output_csv, index=False)
    print(f"Dados processados salvos em: {output_csv}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processar dados para o pipeline")
    parser.add_argument("input_csv", help="Caminho do arquivo CSV de entrada")
    parser.add_argument("output_csv", help="Caminho do arquivo CSV de saída")
    args = parser.parse_args()

    process_data(args.input_csv, args.output_csv)    