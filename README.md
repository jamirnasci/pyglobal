## Propósito:
Este script em Python realiza o alinhamento de sequências em pares usando o algoritmo Needleman-Wunsch entre uma sequência de consulta e um conjunto de sequências de assunto. Os resultados são gravados em um arquivo CSV chamado 'report.csv', incluindo identificadores de pares de sequências, pontuações de alinhamento e similaridades.

## Uso:
O script utiliza argumentos de linha de comando para especificar a sequência de consulta e uma ou mais sequências de assunto. As opções de linha de comando são as seguintes:

-q: Especifica o caminho para o arquivo de sequência de consulta no formato FASTA.
-s: Especifica o(s) caminho(s) para o(s) arquivo(s) de sequência(s) de assunto no formato FASTA. Vários caminhos de assunto podem ser fornecidos.
## Exemplo de Comando:
python script.py -q query.fasta -s subject1.fasta subject2.fasta subject3.fasta
