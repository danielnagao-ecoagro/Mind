# Caso Numérico de FIDC Consignado com Averbação, Fluxo e Inadimplência

Este caso mostra como um [[FIDC_Consignado|FIDC de consignado]] combina previsibilidade de fluxo com risco operacional de averbação, desligamento e quebra do canal de desconto.

## Premissas do caso
- carteira adquirida: 2.000.000
- prazo médio remanescente: 18 meses
- retorno bruto projetado da carteira no período: 480.000
- perda líquida esperada por desligamento, fraude e falha operacional: 120.000
- despesa operacional total: 60.000
- arrasto de caixa e descasamentos: 20.000
- custo econômico da classe sênior no período: 210.000

## Passo 1: resultado bruto da carteira

`Resultado_bruto = 480.000`

Esse é o excesso econômico antes de perdas e custo de estrutura.

## Passo 2: resultado líquido após fricções

`Resultado_liquido = 480.000 - 120.000 - 60.000 - 20.000 = 280.000`

## Passo 3: comparação com a classe sênior

`Spread_residual = 280.000 - 210.000 = 70.000`

Nesse cenário-base, ainda existe folga econômica para remunerar a subordinada e preservar proteção.

## Cenário de estresse operacional
Agora suponha uma falha relevante de averbação que eleva a perda líquida esperada para 220.000.

`Resultado_liquido_estresse = 480.000 - 220.000 - 60.000 - 20.000 = 180.000`

`Spread_residual_estresse = 180.000 - 210.000 = -30.000`

A estrutura sai de folga positiva para déficit econômico apenas pela piora operacional.

## O que este caso ensina
- consignado não é risco zero só porque o fluxo é recorrente
- averbação e vínculo empregatício afetam diretamente a matemática do fundo
- spread pode parecer robusto até o canal de desconto falhar
- o risco operacional precisa entrar na precificação e no monitoramento

## Perguntas de controle
- qual parte da perda vem de crédito e qual parte vem de operação
- a taxa de compra considera risco de mudança de convênio
- há concentração relevante em um único consignante
- o modelo separa atraso temporário de perda estrutural

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[FIDC_Consignado|FIDC de Consignado]]
- [[Matematica_Financeira_de_FIDC|Matemática Financeira de FIDC]]
- [[Modelagem_de_Cash_Flow_de_FIDC|Modelagem de Cash Flow de FIDC]]
- [[Excesso_de_Spread|Excesso de Spread]]
- [[Credito_e_Risco/Analise_de_Credito|Análise de Crédito]]
- [[Subordinacao_e_Reforco_Credito|Subordinação e Reforço de Crédito]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #consignado #averbacao #inadimplencia #spread
