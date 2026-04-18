# Exemplo Numérico de PL, Cota e Amortização em FIDC

Esta nota conecta os conceitos de [[Calculo_de_PL_e_Cota_em_FIDC|PL e cota]] com o efeito de uma [[Amortizacao_de_Cotas_em_FIDC|amortização]] em uma estrutura simples de [[FIDC_Conceitos|FIDC]].

## Caso-base antes da amortização
Considere a seguinte fotografia do fundo:
- carteira marcada: 9.700.000
- caixa disponível: 500.000
- despesas provisionadas: 80.000
- outras obrigações: 20.000

Logo:

`Ativos = 9.700.000 + 500.000 = 10.200.000`

`Passivos = 80.000 + 20.000 = 100.000`

`PL_total = 10.200.000 - 100.000 = 10.100.000`

## Estrutura de cotas
Suponha:
- classe sênior: 8.000.000
- classe subordinada: 2.100.000
- quantidade de cotas sênior: 8.000
- quantidade de cotas subordinadas: 2.100

Então:

`Cota_senior = 8.000.000 / 8.000 = 1.000`

`Cota_subordinada = 2.100.000 / 2.100 = 1.000`

## Evento de amortização
O fundo decide amortizar 400.000 da classe sênior com caixa já disponível.

Após o pagamento:
- caixa cai de 500.000 para 100.000
- PL total cai de 10.100.000 para 9.700.000
- saldo econômico da classe sênior cai de 8.000.000 para 7.600.000
- quantidade de cotas sênior permanece 8.000, se a amortização for em dinheiro por cota

Amortização por cota:

`Amortizacao_por_cota_senior = 400.000 / 8.000 = 50`

Se o valor da cota antes do evento era 1.000, depois da amortização o investidor recebe 50 em caixa e a cota econômica remanescente cai para aproximadamente 950, assumindo que o resto da estrutura não mudou no mesmo dia.

## Efeito sobre a proteção
Antes da amortização, a subordinação econômica era:

`2.100.000 / 10.100.000 = 20,8%`

Depois da amortização da sênior, a subordinada segue em 2.100.000 e o PL total cai para 9.700.000:

`2.100.000 / 9.700.000 = 21,6%`

Nesse caso, a amortização da sênior aumenta a participação relativa da classe subordinada no PL total.

## O que observar no exemplo
- composição do ativo e passivo
- cálculo do patrimônio líquido
- separação por classe de cota
- efeito da amortização sobre o saldo remanescente
- mudança indireta na subordinação econômica

## Utilidade
O exemplo ajuda a interpretar como eventos de caixa alteram o valor das cotas e a proteção estrutural.

## Erros comuns
- tratar amortização como rendimento
- esquecer de ajustar o caixa após o pagamento
- analisar a cota sem olhar a nova relação entre classes
- ignorar que despesas e marcação da carteira podem mudar no mesmo fechamento

## Referências e Links
- [[Indice_FIDC|FIDC]]
- [[Calculo_de_PL_e_Cota_em_FIDC|Cálculo de PL e Cota em FIDC]]
- [[Amortizacao_de_Cotas_em_FIDC|Amortização de Cotas em FIDC]]
- [[Waterfall_e_Ordem_de_Pagamentos|Waterfall e Ordem de Pagamentos]]
- [[Subordinacao_e_Reforco_Credito|Subordinação e Reforço de Crédito]]
- [[Mini_Caso_de_Fechamento_Diario_em_FIDC|Mini Caso de Fechamento Diário em FIDC]]

---
[[Indice_FIDC|Voltar para FIDC]]
[[Mind/Conhecimento/indice|Índice Principal]]

#fidc #exemplo #pl #cota #amortizacao
