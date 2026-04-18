# Duration e Convexidade

[[Mercado_Financeiro/Duration_e_Convexidade|Duration]] e convexidade são medidas de sensibilidade usadas para estimar como o preço de um título de renda fixa reage a mudanças nas taxas de juros. Elas são essenciais para [[Mercado_Financeiro/Precificacao_de_Titulos_de_Renda_Fixa|precificação]], gestão de risco e construção de carteiras alinhadas a benchmarks ou passivos.

## Duration
### O que a duration mede
A duration resume o prazo econômico do título, levando em conta não apenas o vencimento final, mas também o momento em que os fluxos de caixa são recebidos.

Em termos práticos, ela ajuda a responder: se a taxa de juros mudar, quanto o preço do título tende a variar?

### Duration de Macaulay
A duration de Macaulay representa o prazo médio ponderado dos fluxos de caixa descontados do título. Ela é útil para entender a estrutura temporal do papel e serve de base para outras medidas.

Em títulos zero cupom, a duration coincide com o vencimento. Em títulos com cupom, a duration tende a ser menor do que o prazo final, porque parte do dinheiro volta antes.

### Duration modificada
A duration modificada traduz a sensibilidade do preço em termos percentuais.

Uma aproximação clássica é:
$$
\Delta P \approx - D_{mod} \times \Delta y
$$

Ou seja, para pequenas variações de taxa, o preço do título muda na direção oposta à taxa, em magnitude aproximada pela duration modificada.

## Relações importantes
### Relação direta
- prazo maior tende a elevar a duration

### Relação inversa
- taxa de juros maior tende a reduzir a duration
- cupons maiores tendem a reduzir a duration
- maior frequência de pagamento de cupom tende a reduzir a duration

Essas relações ajudam a entender por que títulos longos e zero cupom são mais sensíveis a juros.

## Convexidade
### Por que a duration sozinha não basta
A duration supõe relação linear entre preço e taxa. Isso funciona bem para pequenas mudanças, mas perde precisão quando a oscilação de juros é maior.

Na realidade, a curva preço versus taxa é convexa. A convexidade mede justamente essa curvatura.

### Interpretação prática
Títulos com convexidade positiva:
- caem menos do que a duration sugeriria quando os juros sobem
- sobem mais do que a duration sugeriria quando os juros caem

Por isso, a convexidade melhora a estimativa de variação de preço e é especialmente relevante em títulos longos, com baixa taxa de cupom ou estruturas mais sensíveis à curva.

## Aplicações em carteira
### Gestão de risco
O gestor usa duration e convexidade para controlar exposição a juros e comparar papéis com sensibilidades distintas.

### Imunização
Em gestão de passivos, uma regra central é aproximar a duration dos ativos à duration dos passivos. Isso reduz o descasamento entre variação do valor presente dos ativos e obrigações futuras.

### Benchmarking
Na gestão relativa de renda fixa, é comum buscar compatibilidade de duration, key rate duration e exposição a spread com o índice de referência.

## Limitações
- a duration é uma aproximação local, não uma verdade exata para grandes choques
- mudanças não paralelas na curva exigem medidas mais refinadas, como key rate duration
- títulos com opcionalidades embutidas podem exigir effective duration

## Leituras úteis
- duration maior implica maior risco de taxa de juros
- títulos sem cupom têm duration maior do que títulos com cupom de mesmo vencimento
- convexidade positiva melhora o comportamento do preço tanto em queda quanto em alta de juros, relativamente à aproximação linear

## Referências e Links
- [[Mercado_Financeiro/Indice_Mercado|Mercado Financeiro]]
- [[Mercado_Financeiro/Precificacao_de_Titulos_de_Renda_Fixa|Precificação de Títulos de Renda Fixa]]
- [[Mercado_Financeiro/Riscos_em_Renda_Fixa|Riscos em Renda Fixa]]
- [[Mercado_Financeiro/Curva_de_Juros_e_Spread|Curva de Juros e Spread]]
- [[Gestao_de_Carteiras/Gestao_de_Passivos|Gestão de Passivos]]
- [[Gestao_de_Carteiras/Benchmark_e_Gestao_Relativa|Benchmark e Gestão Relativa]]

---
[[Mercado_Financeiro/Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#renda_fixa #duration #convexidade #juros #sensibilidade
