# Rotina Diária de Fechamento de FIDC

A rotina diária de fechamento de [[FIDC_Conceitos|FIDC]] consolida posição, caixa, eventos, provisões e despesas para produzir informação confiável sobre PL, cota e risco.

## Etapas típicas
1. carregar arquivos de carteira e caixa
2. conciliar movimentos
3. reconhecer eventos e provisões
4. recalcular PL e cota
5. revisar indicadores e exceções

## Contas críticas do fechamento
- atualização da carteira por [[Accrual_Pro_Rata_em_Direitos_Creditorios|accrual]], liquidação e marcação
- reconciliação de caixa contra eventos realizados
- ajuste de provisão e perdas esperadas
- cálculo do [[Calculo_de_PL_e_Cota_em_FIDC|PL e da cota]]
- leitura de [[Excesso_de_Spread|spread]], subordinação e gatilhos

## Perguntas que o fechamento precisa responder
- o valor da carteira está coerente com os eventos do dia
- o caixa bate com a liquidação efetiva dos recebíveis
- houve deterioração suficiente para exigir ajuste de provisão
- o PL mudou por resultado econômico ou apenas por movimentação entre caixa e carteira

## Onde erros surgem
Falhas de interface, atraso de arquivos, documentos inconsistentes e tratamento inadequado de eventos extraordinários são fontes comuns de desvio.

## Relação com os casos numéricos
Os casos de [[Exemplo_Numerico_de_Precificacao_de_Recebiveis_em_FIDC|precificação]], [[Mini_Caso_de_Fechamento_Diario_em_FIDC|fechamento diário]] e [[Exemplo_Numerico_de_PL_Cota_e_Amortizacao_em_FIDC|PL, cota e amortização]] mostram como as contas se encadeiam da compra do ativo até a leitura da estrutura.

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Contabilidade_e_Controle/Conciliacao_de_Caixa_e_Posicao_em_FIDC|Conciliação de Caixa e Posição em FIDC]]
- [[Calculo_de_PL_e_Cota_em_FIDC|Cálculo de PL e Cota em FIDC]]
- [[Contabilidade_e_Controle/Marcacao_e_Provisionamento_em_FIDC|Marcação e Provisionamento em FIDC]]
- [[Accrual_Pro_Rata_em_Direitos_Creditorios|Accrual Pro Rata em Direitos Creditórios]]
- [[Exemplo_Numerico_de_Precificacao_de_Recebiveis_em_FIDC|Exemplo Numérico de Precificação de Recebíveis em FIDC]]
- [[Mini_Caso_de_Fechamento_Diario_em_FIDC|Mini Caso de Fechamento Diário em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #fechamento #rotina #pl #cota
