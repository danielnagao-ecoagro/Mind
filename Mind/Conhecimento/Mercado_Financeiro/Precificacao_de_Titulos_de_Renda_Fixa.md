# Precificação de Títulos de Renda Fixa

A precificação de títulos de renda fixa consiste em trazer a valor presente todos os fluxos de caixa prometidos pelo ativo, usando uma taxa de desconto compatível com o risco, o prazo, a liquidez e as condições de mercado. Esse processo é central para [[Mercado_Financeiro/Curva_de_Juros_e_Spread|curva de juros]], [[Mercado_Financeiro/Riscos_em_Renda_Fixa|gestão de risco em renda fixa]] e marcação a mercado.

## Lógica econômica da precificação
No mercado secundário, o investidor compra um fluxo futuro de cupons e principal. O preço justo do título é a soma dos valores presentes desses recebimentos.

Em termos práticos, o processo costuma seguir três etapas:
- projetar os fluxos de caixa do título
- definir a taxa de desconto exigida pelo mercado
- descontar os fluxos e somá-los para chegar ao preço

Quanto maior a taxa exigida, menor o preço do título. Quanto menor a taxa exigida, maior o preço. Essa relação inversa explica por que oscilações de juros afetam imediatamente o valor de mercado de títulos prefixados e indexados.

## Componentes que determinam o preço
### Fluxo de caixa
O fluxo depende da estrutura contratual do papel:
- títulos zero cupom concentram o pagamento no vencimento
- títulos com cupom distribuem juros periodicamente e devolvem principal no vencimento ou ao longo da amortização
- títulos com opção embutida podem alterar os fluxos esperados

### Taxa de desconto
A taxa usada na precificação precisa refletir o retorno exigido para aquele risco. Em prova e em prática, ela costuma embutir:
- taxa livre de risco ou curva-base
- spread de crédito do emissor ou da estrutura
- prêmio de liquidez
- prêmios associados a prazo, opcionalidades e assimetria de informação

Em renda fixa, a taxa interna de retorno do título é frequentemente tratada como [[Metodos_Quantitativos/Valor_do_Dinheiro_no_Tempo|TIR]] ou YTM, desde que o ativo seja carregado até o vencimento e os fluxos sejam reinvestidos de forma compatível com essa taxa.

## Conceitos que aparecem com frequência
### PU e valor presente
O preço unitário é o valor presente dos fluxos futuros. Em títulos sem cupom, o raciocínio é mais direto: desconta-se o valor de resgate pelo prazo e pela taxa requerida.

### Cupom
O cupom representa o juro periódico pago ao investidor. Em debêntures e outros papéis com cupom, a precificação exige separar cada pagamento intermediário e o principal final.

### Yield to Maturity
O YTM resume a taxa implícita do título para quem compra no preço atual e carrega o papel até o vencimento. Ele é útil para comparação entre ativos, mas depende de hipóteses de reinvestimento e adimplência dos fluxos.

### Current Yield
O current yield compara o cupom anual com o preço do título, mas ignora ganho ou perda de capital até o vencimento. Por isso, é menos completo do que o YTM.

## Fatores que deslocam o preço
### Mudança na curva de juros
Se a curva sobe, os títulos já emitidos com taxa menor tendem a cair de preço. Se a curva cai, esses títulos tendem a se valorizar.

### Mudança no spread de crédito
Mesmo sem alteração na curva-base, piora de percepção de risco do emissor aumenta o retorno exigido e reduz o preço do ativo. Melhora de rating ou compressão de spread faz o movimento oposto.

### Liquidez
Títulos pouco negociados geralmente exigem desconto adicional para compensar a dificuldade de saída. Em mercados estressados, esse componente pode ser tão relevante quanto o risco de crédito.

## Relação com duration e convexidade
A precificação e a sensibilidade caminham juntas. Depois de conhecer o preço-base, o gestor quer saber o quanto ele muda quando a taxa oscila.

[[Mercado_Financeiro/Duration_e_Convexidade|Duration]] fornece uma aproximação linear da variação percentual do preço para pequenas mudanças de taxa. [[Mercado_Financeiro/Duration_e_Convexidade|Convexidade]] melhora essa aproximação quando as mudanças são maiores ou quando o título tem perfil de fluxo menos linear.

## Aplicações práticas
- comparar títulos públicos e privados de mesmo prazo
- avaliar se um spread compensa adequadamente o risco de crédito
- decidir entre carregar até o vencimento ou negociar no mercado secundário
- acompanhar marcação a mercado de fundos e carteiras próprias
- estruturar imunização e gestão relativa contra benchmark

## Armadilhas comuns
- usar taxa de desconto incompatível com o risco do ativo
- comparar títulos só pelo cupom, sem olhar preço e yield
- ignorar opcionalidades embutidas, como call e put
- confundir rentabilidade contratada com preço de mercado
- desconsiderar o efeito de liquidez em papéis privados

## Referências e Links
- [[Mercado_Financeiro/Indice_Mercado|Mercado Financeiro]]
- [[Mercado_Financeiro/Curva_de_Juros_e_Spread|Curva de Juros e Spread]]
- [[Mercado_Financeiro/Duration_e_Convexidade|Duration e Convexidade]]
- [[Mercado_Financeiro/Riscos_em_Renda_Fixa|Riscos em Renda Fixa]]
- [[Mercado_Financeiro/Titulos_Publicos_Federais|Títulos Públicos Federais]]
- [[Mercado_Financeiro/Titulos_Privados_de_Renda_Fixa|Títulos Privados de Renda Fixa]]
- [[Contabilidade_e_Controle/Marcacao_a_Mercado_vs_Curva|Marcação a Mercado vs Curva]]

---
[[Mercado_Financeiro/Indice_Mercado|Voltar para Mercado Financeiro]]
[[Mind/Conhecimento/indice|Índice Principal]]

#renda_fixa #precificacao #juros #ytm #marcacaoamercado
