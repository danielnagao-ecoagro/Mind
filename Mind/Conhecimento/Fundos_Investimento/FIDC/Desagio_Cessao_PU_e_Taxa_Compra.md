# Deságio, Cessão, PU e Taxa de Compra

Esta nota explica como o preço de aquisição de um recebível em [[FIDC_Conceitos|FIDC]] nasce da relação entre valor de face, [[PU_e_Valor_Presente_em_FIDC|valor presente]], prazo e taxa de compra negociada na [[Estruturacao_e_Operacoes/Cessao_de_Credito|cessão de crédito]].

## Intuição econômica
Em muitos FIDCs, o fundo compra um recebível por valor inferior ao valor de face. Esse desconto inicial é o deságio econômico da cessão e precisa ser lido junto com prazo, risco esperado, custo operacional e convenções de cálculo.

## Fórmula-base
Em uma leitura simplificada, o preço econômico do ativo pode ser pensado como:

`PU = Fluxo_esperado / (1 + i)^n`

Onde:
- `Fluxo_esperado` é o valor que o fundo espera receber no vencimento ou no conjunto de vencimentos
- `i` é a taxa de compra ou taxa de desconto compatível com o risco
- `n` é o prazo ajustado à convenção de dias do fundo

## Relação entre os componentes
- valor de face: montante contratual a receber no vencimento
- PU: preço unitário econômico do ativo na data da compra
- taxa de compra: taxa implícita usada para trazer o fluxo a valor presente
- deságio: diferença entre valor de face e preço pago

## Exemplo simples
Se um recebível paga 10.000 em 60 dias e o fundo exige retorno compatível com uma taxa de desconto de 2% no período, o preço de compra econômico fica abaixo de 10.000. Nesse caso:
- valor de face: 10.000
- PU aproximado: 10.000 / 1,02 = 9.804
- deságio aproximado: 196

Esse exemplo é simplificado. Na prática, o gestor ainda ajusta o fluxo esperado por atraso, perda, custo de cobrança e documentação.

## Leitura prática
Quanto maior a taxa requerida pelo fundo, maior tende a ser o deságio e menor o PU. Essa relação muda se houver atraso, pré-pagamento, recuperação parcial ou custos de cobrança embutidos na operação.

## Interpretação gerencial
O deságio não é sinônimo automático de ganho. Um PU muito baixo pode refletir risco alto, problema documental, baixa recuperabilidade ou estrutura operacional cara. O ponto correto é comparar o preço pago com o fluxo efetivamente realizável.

## Erros comuns
- usar valor de face como se fosse base de retorno do fundo
- comparar taxa de compra mensal com meta anual sem conversão
- ignorar que o fluxo esperado pode ser menor que o fluxo contratual
- esquecer que caixa parado e despesas reduzem o retorno líquido do veículo

## Por que isso importa no FIDC
Esse cálculo é a base de [[Precificacao_de_Carteiras_de_Recebiveis|precificação da carteira]], do reconhecimento de [[Accrual_Pro_Rata_em_Direitos_Creditorios|accrual]] e da leitura de [[Excesso_de_Spread|excesso de spread]] ao longo do carregamento.

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[PU_e_Valor_Presente_em_FIDC|PU e Valor Presente em FIDC]]
- [[Precificacao_de_Carteiras_de_Recebiveis|Precificação de Carteiras de Recebíveis]]
- [[Exemplo_Numerico_de_Precificacao_de_Recebiveis_em_FIDC|Exemplo Numérico de Precificação de Recebíveis em FIDC]]
- [[Estruturacao_e_Operacoes/Cessao_de_Credito|Cessão de Crédito]]
- [[Metodos_Quantitativos/Conversao_de_Taxas|Conversão de Taxas]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #desagio #cessao #pu #precificacao
