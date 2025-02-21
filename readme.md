# Impacto de Uso de Expressões Gênicas com Maior Precisão e com Aplicação de Modelo de Redução de Ruído em Diferentes Embeddings para Geração de Moléculas 

Este repositório apresenta o desenvolvimento do Trabalho de Conclusão de Curso (TCC), cujo objetivo é explorar diferentes representações de Expressão Gênica e analisar sua performance na atividade de gerar moléculas.


## Resumo
O 'de novo' design possibilitou modelos de aprendizado de máquina a criarem compostos celuares com um alto nível de liberdade e acuracidade, sendo as moléculas um desses comostos. Para esta atividade, é necessária a informação de expressão gênica da molécula; entretanto, este dado apresenta grande quantidade de ruído em sua informação, o que atrapalha o processo generativo. Deste modo, este trabalho teve como objetivo explorar diferentes maneiras de representar a expressâo gênica no ambente da molécula, sendo isto feito feito através do uso de diferentes embeddings, diferentes pontos de casas decimais, e uso de modelo de redução de ruído.


## Estrutura do Projeto

O artigo TranGEM original teve partes adaptadas. O arquivo `gene_ex_encoder_upgraded.py` teve sua estrutura adaptada a fim de comportar valores diferentes de casas decimais, adaptando cada um de seus embeddings -- sendo capaz de suportar qualquer valor de ponto decimal. Os arquivos `Model.py` e `test.py` também foram adaptados para terem os valores de dimensões corretos.

Os arquivos de performance estão na pasta `out`, enquato os de resultados estão em `result`.

O arquivo de `enviroment.yaml` apresenta os pacotes necessários para rodar o programa.

## Como Reproduzir os Resultados

1. Clone o repositório:
   ```bash
   git clone [INSERIR REP]
   ```
2. Crie um ambiente virtual:
   ```sh
   conda env create -f environment.yaml
   ```

3. Ative o ambiente virtual:
   ```sh
   conda activate TransGEM
   ```
4. Obtenha os dados:
   Os datasets utilizados estão [disponíveis neste link](https://drive.google.com/drive/folders/1iNJ8dXJKPpoAQ5gFHMtXJL926_xyKEkr?usp=sharing).  Eles não puderam ser colocados diretamente no GitHub devido ao seu tamanho.

5. Treine o modelo:

No treinamento, os hiperparâmetros utilizados são:
- `data_path`: onde os dados se encontram;
- `dataset ([df_fame, df_fame_cl])`: o prefixo do nome do conjunto de dados;
- `gene_encoder ([values, one_hot, binary, tenfold_binary])`: o embedding de expressão gênica utilizado;
- `decimal_points`: o número de casas decimais a ser considerado;
- `gene_e_length`: tamanho de pontos de expressão gênica de entrada (`978` com a base de dados original, `64` para a base de dados com aplicação do modelo GED);
- `max_int`: valor de inteiro do ponto máximo dentro dos pontos de expressão gênica, usado para criar os embeddings (`10` para a base de dados original, `0` para a base de dados com aplicação do modelo GED);
- `epochs`: número de épocas de treinamento.

Segue o script de treinamento:

- Caso treine o modelo sem o GED:

   ```sh
   python train.py --data_path ./data/ --dataset df_fame --gene_encoder value --gpu cuda:0 --decimal_points 6 --gene_e_length 978 --max_int 10 --epochs 200
   ```

- Caso treine o modelo com o GED:
   ```sh
   python train.py --data_path ./data/ --dataset df_fame_cl --gene_encoder value --gpu cuda:0 --decimal_points 6 --gene_e_length 64 --max_int 0 --epochs 200
   ```

- Os hiperparâmetos de gene_encoder, decimal_points, e epochs pode ser alterado a fim realizar diferentes experimentos.

6. Teste o modelo:

- Caso teste o modelo sem o GED:

   ```sh
   python test.py --data_path ./data/ --dataset df_fame --gene_encoder value --gpu cuda:0 --decimal_points 6 --gene_e_length 978 --max_int 10
   ```

- Caso teste o modelo com o GED:

   ```sh
   python test.py --data_path ./data/ --dataset df_fame_cl --gene_encoder value --gpu cuda:0 --decimal_points 6 --gene_e_length 64 --max_int 0
   ```

## Referências
O código original do TransGEM pode ser encontrado no seguinte link: [código TransGEm](https://github.com/hzauzqy/TransGEM/tree/main)

O código original do FAME pode ser encontrado no seguinte link: [código FAME](https://github.com/pth1993/FAME)

## Contribuições

Contribuições são bem-vindas! Caso tenha sugestões ou melhorias, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto está licenciado sob a Licença MIT.

## Autor

Este projeto foi desenvolvido por Pedro como parte dos requisitos para conclusão do curso de Engenharia de Computação na Universidade Federal de São Carlos.
