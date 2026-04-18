# Riscos em Renda Fixa

Renda fixa não significa retorno certo em qualquer horizonte ou ausência de perda. Os títulos de renda fixa estão expostos a riscos de mercado, crédito, liquidez, reinvestimento e estrutura contratual, e o peso de cada um depende do emissor, do prazo, da indexação e das garantias.

## Principais riscos
### Risco de taxa de juros
É o risco de perda causado por oscilações na curva de juros. Quando a taxa de mercado sobe, o preço de títulos prefixados e de papéis marcados a mercado tende a cair.

Esse risco é mais relevante em ativos com prazo mais longo e maior [[Mercado_Financeiro/Duration_e_Convexidade|duration]]. Por isso, dois títulos com o mesmo emissor podem reagir de forma muito diferente a uma mesma mudança de taxa.

### Risco de crédito
É a possibilidade de perdas por inadimplência, reestruturação, piora de rating ou alargamento de spread. Em crédito privado, o investidor não analisa apenas se haverá calote, mas também se o prêmio recebido compensa a deterioração potencial do emissor ou da estrutura.

Esse risco se conecta diretamente com [[Credito_e_Risco/Analise_de_Credito|análise de crédito]], [[Credito_e_Risco/Rating_e_Score|rating]] e [[Mercado_Financeiro/Curva_de_Juros_e_Spread|spread de crédito]].

### Risco de liquidez
Mesmo sem evento de crédito, pode ser difícil vender o título no preço teórico. Em momentos de estresse, o investidor pode aceitar desconto relevante para sair da posição.

Esse risco costuma ser mais alto em papéis privados, emissões pequenas, estruturas complexas e ativos com mercado secundário pouco profundo.

### Risco de reinvestimento
Surge quando fluxos recebidos antes do vencimento precisam ser reinvestidos a taxas menores do que as originalmente esperadas. Títulos com cupom são mais expostos a esse risco do que títulos zero cupom.

Há um trade-off clássico:
- títulos com cupom reduzem o risco de preço ao encurtar a duration
- mas aumentam o risco de reinvestimento

### Risco de spread
Além da curva-base, títulos privados sofrem com mudanças no spread de crédito. Mesmo que a taxa livre de risco fique estável, piora de percepção do emissor pode reduzir o preço do ativo.

### Risco de opcionalidade
Alguns papéis possuem call, put, pré-pagamento ou amortização extraordinária. Essas cláusulas alteram os fluxos esperados e mudam a sensibilidade do título a juros, crédito e liquidez.

## Como os riscos interagem
Na prática, os riscos raramente aparecem isolados. Um evento de crédito pode reduzir a liquidez. Uma abertura de spread pode ser acompanhada de aumento de volatilidade. Uma queda de juros pode valorizar o papel, mas piorar o reinvestimento dos cupons.

Por isso, a gestão de renda fixa precisa combinar:
- análise do emissor e da estrutura
- monitoramento de preço e sensibilidade
- limites de concentração e liquidez
- acompanhamento de covenants, garantias e eventos de crédito

## Ferramentas de controle
### Medidas de sensibilidade
- [[Mercado_Financeiro/Duration_e_Convexidade|duration]]
- convexidade
- spread duration
- key rate duration

### Medidas de crédito
- análise de balanço e fluxo de caixa
- classificação de risco
- acompanhamento de garantias
- métricas de concentração por emissor, setor e sacado

### Medidas de portfólio
- diversificação
- matching de duration contra benchmark ou passivos
- limites por classe e liquidez
- hedge com derivativos, quando permitido e economicamente justificável

## Aplicações práticas
- avaliar se um título privado remunera adequadamente o risco adicional sobre o soberano
- definir prazo adequado para a carteira diante de expectativa de juros
- montar estratégia de imunização em carteiras com passivos
- evitar concentração excessiva em emissores, cedentes ou setores

## Leituras usuais em prova e no mercado
- duration maior implica maior risco de taxa de juros
- cupom maior reduz duration, mas aumenta risco de reinvestimento
- piora de rating tende a elevar retorno exigido e derrubar preço do título
- liquidez ruim pode ampliar perdas mesmo sem default

## Referências e Links
- [[Mercado_Financeiro/Indice_Mercado|Mercado Financeiro]]
- [[Mercado_Financeiro/Precificacao_de_Titulos_de_Renda_Fixa|Precificação de Títulos de Renda Fixa]]
- [[Mercado_Financeiro/Duration_e_Convexidade|Duration e Convexidade]]
- [[Mercado_Financeiro/Curva_de_Juros_e_Spread|Curva de Juros e Spread]]
- [[Credito_e_Risco/Tipos_de_Risco|Tipos de Risco]]
- [[Credito_e_Risco/Analise_de_Credito|Análise de Crédito]]
- [[Gestao_de_Carteiras/Gestao_de_Passivos|Gestão de Passivos]]

---
[[Mercado_Financeiro/Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#renda_fixa #risco #credito #liquidez #duration
