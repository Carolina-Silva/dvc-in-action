# 🚀 DVC in Action  
Este repositório contém experimentos e pipelines de Machine Learning utilizando **DVC (Data Version Control)**. 



## 📌 O que foi testado?

### ✅ 1. Versionamento de Dados e Modelos  
- Uso de `dvc init` para iniciar o controle de versões.  
- Rastreamento de arquivos grandes com `dvc add`.  
- Armazenamento e recuperação de dados em um **storage remoto** (Google Drive).  

### ✅ 2. Construção de Pipelines Reprodutíveis  
- Definição de um fluxo de Machine Learning usando `dvc.yaml`.  
- Automação com `dvc repro`
- Cache inteligente para evitar reprocessamento desnecessário.  

### ✅ 3. Comparação de Experimentos  
- Uso de `dvc exp run` para rodar diferentes experimentos
- Comparação de métricas com `dvc exp show` e `dvc exp diff`.  
- Armazenamento dos resultados em `metrics.json`.  

### ✅ 4. Visualização de Resultados  
- Geração automática de gráficos a partir das métricas.  
- Armazenamento de gráficos no DVC para versionamento.  

### ✅ 5. Data Registry e Reutilização  
- Conceito de **Data Registry** para compartilhar datasets e modelos entre projetos.  
- Uso de `dvc import` e `dvc get` para acessar dados versionados em outros repositórios.  




## ⚡ Como rodar o projeto  
1. Clone o repositório e instale as dependências:  
   ```bash
   git clone https://github.com/Carolina-Silva/dvc-in-action
   cd dvc-in-action
   pip install -r requirements.txt

1. Baixe os dados rastreados pelo DVC: 
   ```bash
   dvc pull

1. Baixe os dados rastreados pelo DVC: 
   ```bash
   dvc repro
  
1. Compare experimentos:
   ```bash
   dvc exp show


## 📊 Exemplos de Gráficos
Aqui estão algumas visualizações geradas durante os experimentos:

## 🌟 Próximos Passos
 *  Melhorar a comparação entre experimentos
 *  Criar integração com CI/CD para experimentos automáticos
 *  Expandir o uso do Data Registry

##  📌 Referências
 [Documentação DVC](https://dvc.org/doc/use-cases)

 [Curso Iterative Tools for Data Scientists and Analysts](https://learn.dvc.ai/)