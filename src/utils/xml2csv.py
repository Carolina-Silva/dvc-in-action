import pandas as pd
import argparse

def xml_to_csv(input_path, output_path):
    df= pd.read_xml(input_path)
    df.to_csv(output_path, index=False)
    
    print(f"Arquivo {input_path} foi convertido e esta salvo na pasta {output_path}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converter XML para CSV")
    parser.add_argument("input", help="Caminha para o XML de entrada")
    parser.add_argument("output", help="Caminho para salvar CSV")
    args = parser.parse_args()
    
    
    xml_to_csv(args.input, args.output)
    