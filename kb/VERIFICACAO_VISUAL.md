# Verificação da camada visual

Como funciona a prova: cada folha de quadros e cada folha de ilustrações recebeu, na própria imagem, um código de cinco caracteres derivado de uma chave secreta guardada fora da base. O código só pode ser obtido olhando a imagem. O agente que viu a folha anotou o código, e a conferência recalcula o código esperado e compara.

## Números

| Item | Valor |
|---|---|
| Vídeos com arquivo no site | 175 |
| Vídeos processados em folhas | 175 |
| Folhas de quadros | 3072 |
| Folhas conferidas | 3072 |
| Vídeos assistidos por inteiro | 175 |
| Unidades do HIG (páginas de ilustração e vídeos de demonstração) | 219 |
| Folhas do HIG conferidas | 552 de 552 |
| Códigos que não bateram | 0 |
| Sínteses visuais escritas | 175 de vídeo e 158 do HIG |
| Sínteses com divergência registrada entre imagem e descrição oficial | 222 |
| Vídeos sem arquivo no site, não assistidos | 13 |

## O que ficou incompleto

Nenhum vídeo processado ficou com folha sem conferir.

## Vídeos sem arquivo no site

Estes não têm vídeo nem transcrição na origem, então não foram assistidos nem receberam cartão:

- wwdc2019_801
- wwdc2022_10175
- wwdc2022_110484
- wwdc2022_110530
- wwdc2022_110531
- wwdc2022_110532
- wwdc2022_110533
- wwdc2023_10337
- wwdc2023_111243
- wwdc2023_111324
- wwdc2023_111484
- wwdc2023_111520
- wwdc2023_111522

## Limites do método

1. As folhas trazem um quadro por mudança de cena e pelo menos um a cada 12 segundos, não todos os quadros do vídeo. Movimento contínuo aparece como diferença entre quadros parados.
2. Efeitos rápidos podem não aparecer entre dois quadros. Quando isso ocorreu, está registrado na nota da folha.
3. As ilustrações do HIG foram vistas na versão clara; a versão escura entrou nas páginas de cor, modo escuro, materiais e ícones.
4. Miniaturas e ícones que a página só usa como link para outras páginas ficaram de fora.
