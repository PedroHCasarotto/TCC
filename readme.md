# Impacto de Uso de Expressões Gênicas com Maior Precisão e com Aplicação de Modelo de Redução de Ruído em Diferentes Embeddings para Geração de Moléculas 

Este repositório apresenta o desenvolvimento do Trabalho de Conclusão de Curso (TCC), cujo objetivo é explorar diferentes representações de Expressão Gênica e analisar sua performance na atividade de gerar moléculas.


## Resumo
O 'de novo' design possibilitou modelos de aprendizado de máquina a criarem compostos celuares com um alto nível de liberdade e acuracidade, sendo as moléculas um desses comostos. Para esta atividade, é necessária a informação de expressão gênica da molécula; entretanto, este dado apresenta grande quantidade de ruído em sua informação, o que atrapalha o processo generativo. Deste modo, este trabalho teve como objetivo explorar diferentes maneiras de representar a expressâo gênica no ambente da molécula, sendo isto feito feito através do uso de diferentes embeddings, diferentes pontos de casas decimais, e uso de modelo de redução de ruído.


## Estrutura do Projeto

O artigo TranGEM original teve partes adaptadas. O arquivo `gene_ex_encoder_upgraded.py` teve sua estrutura adaptada a fim de comportar valores diferentes de casas decimais, adaptando cada um de seus embeddings. Os arquivos `Model.py` e `test.py` também foram adaptados para terem os valores de dimensões corretos.

Os arquivos de performance estão na pasta `out`, enquato os de resultados estão em `result`.


========================================================================================================
========================================================================================================
========================================================================================================



adaptado foi alterado para o seguinte:


O repositório está organizado da seguinte forma:



- **`Bases Tratadas/`**: Contém os conjuntos de dados utilizados para treinamentos e testes.
- **`Artigos/`**: Documentação e arquivos relacionados ao TCC.
- **`Resultados/`**: Relatórios e resultados gerados pelas implementações dos modelos.

- OBS. - O github não aceita arquivos muitos grandes. Então, baixe as bases nos seguintes links e as coloque em pastas chamadas (Olist, M5 e Favorita):
     - 'Olist' : https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
     - 'M5' : https://www.kaggle.com/competitions/m5-forecasting-accuracy
     - 'Favorita' : https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting

Se houver dúvidas confira os arquivos lidos no notebook `EDA.ipynb`

## Modelos Abordados

1. **ARIMA (Autoregressive Integrated Moving Average)**
   - Modelo clássico de séries temporais, focado em dependências lineares.
3. **Prophet**
   - Modelo flexível desenvolvido pelo Facebook, ideal para séries com sazonalidades.
4. **LSTM (Long Short-Term Memory)**
   - Rede neural recorrente projetada para capturar padrões de longo prazo.
5. **CNN (Convolutional Neural Network)**
   - Redes neurais convolucionais aplicadas à previsão de séries temporais.

## Tecnologias Utilizadas

- Linguagem: Python
- Bibliotecas: `pandas`, `numpy`, `statsmodels`, `scikit-learn`, `tensorflow`, `prophet`
- Ferramentas: Jupyter Notebook, Git, Matplotlib, Seaborn

## Como Reproduzir os Resultados

1. Clone o repositório:
   ```bash
   git clone [INSERIR REP]
   ```
2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute os notebooks para reproduzir os resultados na seguinte ordem

    1. EDA.ipynb  
    2. Todos os modelos
    3. Analise_resultados.ipynb

## Contribuições

Contribuições são bem-vindas! Caso tenha sugestões ou melhorias, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Autor

Este projeto foi desenvolvido por Brainer como parte dos requisitos para conclusão do curso de Engenharia de Computação na Universidade Federal de São Carlos.