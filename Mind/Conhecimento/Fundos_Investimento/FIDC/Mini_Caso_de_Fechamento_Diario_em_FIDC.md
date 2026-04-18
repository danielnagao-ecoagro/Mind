# Mini Caso de Fechamento Diário em FIDC

Este mini caso ilustra como uma combinação de caixa, eventos da carteira, provisão e despesas se transforma no fechamento diário de um [[FIDC_Conceitos|FIDC]].

## Dados do dia
- caixa inicial: 300.000
- carteira marcada no início do dia: 4.800.000
- apropriação de accrual do dia: 12.000
- liquidação de recebíveis em caixa: 90.000
- baixa econômica por atraso e piora de risco: 25.000
- despesa do dia: 7.000
- ajuste adicional de provisão: 18.000

## Passo 1: atualizar carteira
A carteira parte de 4.800.000.

Com os eventos do dia:
- soma accrual: +12.000
- retira ativos liquidados: -90.000
- reconhece deterioração econômica: -25.000
- reforça provisão adicional: -18.000

`Carteira_final = 4.800.000 + 12.000 - 90.000 - 25.000 - 18.000 = 4.679.000`

## Passo 2: atualizar o caixa
O caixa recebe a liquidação e paga as despesas:

`Caixa_final = 300.000 + 90.000 - 7.000 = 383.000`

## Passo 3: calcular ativos e passivos
Supondo que não houve outras obrigações novas além da despesa já apropriada:

`Ativos_finais = 4.679.000 + 383.000 = 5.062.000`

Se as provisões e despesas já foram refletidas economicamente na carteira e no caixa, o PL do dia fecha em 5.062.000.

## Leitura do resultado
Mesmo com entrada de caixa, o PL não cresce automaticamente. A piora de risco e o ajuste de provisão podem mais do que compensar o accrual do dia.

## Objetivo
O caso ajuda a visualizar a passagem do dado operacional para o cálculo final de [[Calculo_de_PL_e_Cota_em_FIDC|PL e cota]].

## O que o caso ensina
- caixa não é igual a resultado
- accrual positivo pode coexistir com queda de PL
- liquidação melhora caixa, mas reduz saldo da carteira
- provisão e marcação importam tanto quanto recebimento

## Ponte para a rotina completa
Na prática, esse cálculo é repetido com muito mais granularidade e controles, incluindo arquivos do custodiante, eventos de cessão, conciliação documental e revisão de exceções.

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Rotina_Diaria_de_Fechamento_de_FIDC|Rotina Diária de Fechamento de FIDC]]
- [[Calculo_de_PL_e_Cota_em_FIDC|Cálculo de PL e Cota em FIDC]]
- [[Accrual_Pro_Rata_em_Direitos_Creditorios|Accrual Pro Rata em Direitos Creditórios]]
- [[Contabilidade_e_Controle/Conciliacao_de_Caixa_e_Posicao_em_FIDC|Conciliação de Caixa e Posição em FIDC]]
- [[Contabilidade_e_Controle/Marcacao_e_Provisionamento_em_FIDC|Marcação e Provisionamento em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #caso #fechamento #pl #didatico
