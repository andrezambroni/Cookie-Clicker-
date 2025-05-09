# Cookie Clicker Bot

Este projeto é um bot automatizado para o jogo [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/), desenvolvido em Python utilizando a biblioteca Selenium. O bot realiza cliques automáticos no cookie principal e compra upgrades automaticamente para maximizar a produção de cookies.

- **`Exemplo`**: ![Exemplo de Execução](image.png)

## Estrutura do Projeto


- **`cookie_clicker.py`**: Contém o código principal do bot.
- **`README.md`**: Este arquivo, com informações sobre o projeto.

## Funcionalidades

- **Clique Automático**: O bot clica continuamente no cookie principal.
- **Compra de Upgrades**: O bot identifica e compra os melhores upgrades disponíveis.
- **Aceitação de Cookies**: O bot aceita automaticamente os cookies do site.
- **Seleção de Idioma**: O bot seleciona o idioma "Português" ao carregar o site.

## Estrutura do Código

O código principal está no arquivo [`cookie_clicker.py`](cookie_clicker.py). Ele é dividido nas seguintes partes:

### Classe `CookieClicker`

- **`__init__`**: Configura o Selenium WebDriver e define os seletores XPath para os elementos do site.
- **`open_website`**: Abre o site do Cookie Clicker e aguarda o carregamento.
- **`accept_cookies`**: Aceita os cookies do site.
- **`select_language`**: Seleciona o idioma "Português".
- **`click_on_cookie`**: Realiza cliques no cookie principal.
- **`get_current_money`**: Obtém a quantidade atual de cookies.
- **`get_best_upgrade`**: Identifica o melhor upgrade disponível.
- **`comprar_upgrade`**: Compra o melhor upgrade identificado.

### Loop Principal

O loop principal realiza cliques contínuos no cookie e, a cada 500 iterações, tenta comprar upgrades.

## Personalização

Você pode personalizar o comportamento do bot alterando os seguintes parâmetros no código:

- **Intervalo de Compra de Upgrades**: Modifique o valor `500` no loop principal para ajustar a frequência de compra de upgrades.
- **Seletores XPath**: Atualize os seletores XPath em `SITE_MAP` caso o site do Cookie Clicker seja atualizado.

## Avisos

- **Uso Responsável**: Este bot foi criado para fins educacionais. Use-o com responsabilidade e respeite os termos de uso do site.
- **Manutenção**: O site do Cookie Clicker pode ser atualizado, o que pode exigir ajustes nos seletores XPath do código.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.7 ou superior
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (gerenciado automaticamente pelo `webdriver_manager`)
- Bibliotecas Python:
  - `selenium`
  - `webdriver_manager`

Você pode instalar as dependências Python executando:

```bash
pip install selenium webdriver-manager

pip install selenium
