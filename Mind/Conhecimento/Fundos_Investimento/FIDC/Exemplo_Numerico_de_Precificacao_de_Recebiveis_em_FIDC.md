# Exemplo Numérico de Precificação de Recebíveis em FIDC

Esta nota serve como ponte didática para aplicar conceitos de [[Precificacao_de_Carteiras_de_Recebiveis|precificação]] em uma situação simples de [[FIDC_Conceitos|FIDC]].

## Caso-base
Considere um lote com as seguintes premissas:
- valor de face a receber em 60 dias: 100.000
- perda esperada do lote: 3.000
- custo operacional e de cobrança esperado: 1.000
- fluxo econômico esperado líquido: 96.000
- taxa de desconto requerida para o período: 4%

## Passo 1: estimar o fluxo esperado
O ponto de partida não é o valor de face, mas o fluxo econômico esperado:

`Fluxo_esperado = Valor_de_face - Perda_esperada - Custos_esperados`

Aplicando ao caso:

`Fluxo_esperado = 100.000 - 3.000 - 1.000 = 96.000`

## Passo 2: trazer o fluxo a valor presente
Com taxa de desconto de 4% para o período:

`PU_do_lote = 96.000 / 1,04 = 92.308`

Esse é o valor econômico aproximado que o fundo poderia pagar pelo lote para atingir a taxa desejada, dado o risco embutido nas premissas.

## Passo 3: calcular o deságio econômico
O deságio em relação ao valor de face é:

`Desagio = 100.000 - 92.308 = 7.692`

Esse deságio não representa lucro automático. Parte dele remunera o tempo, parte cobre perdas esperadas e parte compensa custos operacionais.

## Sensibilidades rápidas
### Se a perda esperada subir
Se a perda esperada aumentar para 5.000, mantendo o resto constante:
- novo fluxo esperado: 94.000
- novo PU: 94.000 / 1,04 = 90.385

### Se a taxa de desconto subir
Se o fluxo esperado continuar 96.000, mas a taxa subir para 6%:
- novo PU: 96.000 / 1,06 = 90.566

### Leitura
O preço do lote cai tanto quando o risco esperado piora quanto quando a taxa requerida pelo fundo aumenta.

## O que o exemplo ensina
- impacto da taxa de desconto
- efeito da perda esperada
- sensibilidade do preço a prazo e recuperação

## Onde o analista pode errar
- descontar o valor de face sem antes ajustar perda e custo
- comparar taxas em bases diferentes
- usar uma taxa única para lotes com perfis de risco muito distintos
- ignorar que atraso e recuperação alteram o fluxo esperado real

## Fechamento conceitual
Esse tipo de conta é a porta de entrada para [[Desagio_Cessao_PU_e_Taxa_Compra|deságio e taxa de compra]] e para a marcação econômica da carteira. Depois da compra, o próximo passo lógico é acompanhar o [[Accrual_Pro_Rata_em_Direitos_Creditorios|accrual]] e transformar esse lote em fluxo de caixa do fundo.

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Precificacao_de_Carteiras_de_Recebiveis|Precificação de Carteiras de Recebíveis]]
- [[PU_e_Valor_Presente_em_FIDC|PU e Valor Presente em FIDC]]
- [[Desagio_Cessao_PU_e_Taxa_Compra|Deságio, Cessão, PU e Taxa de Compra]]
- [[Accrual_Pro_Rata_em_Direitos_Creditorios|Accrual Pro Rata em Direitos Creditórios]]
- [[TIR_e_XIRR_em_FIDC|TIR e XIRR em FIDC]]
- [[Convencoes_de_Calculo_em_FIDC|Convenções de Cálculo em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #exemplo #precificacao #recebiveis #didatico
