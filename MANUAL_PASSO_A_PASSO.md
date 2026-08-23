# Manual completo — Trilha 3 da Vitrine Aurora

Este manual foi escrito para uma pessoa iniciante. Faça as etapas na ordem e execute um comando de cada vez.

## 1. O que foi acrescentado nesta trilha

A Trilha 3 completa o projeto com:

- página de login;
- criação de conta;
- encerramento da sessão;
- proteção das páginas internas;
- senhas armazenadas com hash;
- menu responsivo;
- formulários, tabelas, alertas e botões do Bootstrap;
- preparação para publicação no PythonAnywhere.

## 2. Páginas públicas e protegidas

Ficaram públicas somente as páginas que uma pessoa precisa ver antes de entrar:

- `/` — página inicial;
- `/login` — entrada no sistema;
- `/cadastro` — criação de conta.

Exigem login:

- `/usuarios` e suas operações;
- `/categorias` e suas operações;
- `/anuncios` e suas operações;
- `/perguntas` e suas operações;
- `/compras` e suas operações;
- `/favoritos` e suas operações;
- `/relatorios/compras`;
- `/relatorios/vendas`;
- `/logout`.

Em cada rota protegida foi utilizado `@login_required`. Se uma pessoa tentar abrir uma dessas páginas sem login, o Flask-Login envia essa pessoa para `/login`.

## 3. Copiar a atualização para a pasta ligada ao GitHub

1. Baixe e extraia o ZIP da Trilha 3.
2. Pare o servidor antigo com `Ctrl + C`.
3. Abra a pasta extraída `Anna_Ecommerce_Flask`.
4. Selecione os arquivos com `Ctrl + A` e copie com `Ctrl + C`.
5. Abra a pasta antiga do projeto, a mesma que foi usada nas Trilhas 1 e 2.
6. Cole com `Ctrl + V`.
7. Quando o Windows perguntar, escolha **Substituir os arquivos no destino**.

Não apague a pasta antiga antes da cópia. A pasta oculta `.git` existente nela guarda a ligação com o repositório correto.

## 4. Abrir o projeto no VS Code

1. Abra o Visual Studio Code.
2. Clique em **File > Open Folder**.
3. Selecione a pasta antiga `Anna_Ecommerce_Flask`, agora atualizada.
4. Clique em **Select Folder**.
5. Clique em **Terminal > New Terminal**.
6. Confira se o caminho do terminal termina em `Anna_Ecommerce_Flask`.

## 5. Ativar o ambiente virtual

No PowerShell do VS Code:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se a pasta `.venv` ainda não existir, crie-a primeiro:

```powershell
py -m venv .venv
```

Depois, execute novamente o comando de ativação. Quando funcionar, aparecerá `(.venv)` no começo da linha.

Se o PowerShell bloquear a ativação, abra um terminal do tipo **Command Prompt** e use:

```cmd
.venv\Scripts\activate.bat
```

## 6. Instalar as dependências novas

Com `(.venv)` aparecendo no terminal, execute:

```powershell
py -m pip install -r requirements.txt
```

Além do Flask e do Flask-SQLAlchemy, será instalado o Flask-Login, responsável por controlar o usuário autenticado e a sessão.

## 7. Executar no computador

Digite:

```powershell
py app.py
```

Abra no Chrome:

```text
http://127.0.0.1:5000
```

Esse é o endereço local do computador. Ele pode ser igual ao endereço usado nas trilhas anteriores e não é o link público do PythonAnywhere.

## 8. Testar o login

Use o usuário de demonstração:

```text
E-mail: anna@email.com
Senha: 123456
```

1. Na página inicial, clique em **Entrar no sistema**.
2. Digite o e-mail e a senha acima.
3. Clique em **Entrar**.
4. Confira se aparece a mensagem de boas-vindas.
5. Confira se o menu passa a mostrar as áreas de usuários, categorias, anúncios, perguntas, favoritos, compras e relatórios.

## 9. Testar uma senha incorreta

1. Clique em **Sair**.
2. Informe `anna@email.com`.
3. Digite uma senha diferente de `123456`.
4. Clique em **Entrar**.
5. O sistema deve informar que o e-mail ou a senha estão incorretos.

## 10. Testar a proteção das páginas

1. Sem estar conectado, escreva no navegador:

```text
http://127.0.0.1:5000/anuncios
```

2. Pressione Enter.
3. O sistema deve abrir a página de login e exibir o aviso para entrar.
4. Faça o login.
5. Abra novamente a página de anúncios.
6. A lista deve aparecer normalmente.

Repita com `/usuarios`, `/compras` ou `/relatorios/vendas` se quiser conferir outras áreas.

## 11. Testar a criação de conta

1. Saia do sistema.
2. Clique em **Criar conta**.
3. Informe um nome, um e-mail ainda não usado e uma senha com pelo menos seis caracteres.
4. Clique em **Cadastrar**.
5. Faça login com a conta criada.

A senha é transformada em hash antes de ser gravada no banco. Isso evita deixar a senha original visível no arquivo SQLite.

## 12. Conferir o Bootstrap

1. Observe o menu superior, os botões, alertas, formulários e tabelas.
2. Diminua a largura da janela do Chrome.
3. Em uma tela menor, o menu deve virar um botão.
4. Clique nesse botão e confira os links.
5. Abra uma tabela em tela pequena. Ela deve permitir rolagem horizontal sem quebrar a página.

O Bootstrap está salvo na pasta `static`, por isso o layout não depende de uma conexão externa para carregar.

## 13. Atualizar o Git com o nome e o e-mail da Anna

Antes do commit, execute:

```powershell
git config user.name "Anna Julia Torres Martins de Deus"
git config user.email "anninhamt2605@gmail.com"
git config --get user.name
git config --get user.email
```

Os dois últimos comandos devem mostrar o nome e o e-mail da Anna. Essa configuração é feita somente neste projeto.

## 14. Conferir e enviar ao GitHub

O repositório continua sendo:

```text
https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git
```

Execute um comando por vez:

```powershell
git status
git add .
git status
git commit -m "Finaliza login, sessoes e interface Bootstrap"
git push origin main
```

No segundo `git status`, os arquivos devem aparecer em verde. Depois do `git push`, abra o repositório no Chrome, pressione `Ctrl + F5` e confira o novo commit.

O endereço do repositório não muda quando o conteúdo é atualizado.

## 15. Criar ou acessar a conta do PythonAnywhere

1. Abra `https://www.pythonanywhere.com`.
2. Clique em **Sign up** para criar a conta ou **Log in** se já possuir uma.
3. Escolha e anote o nome de usuário. Ele fará parte do endereço público.
4. Entre no painel do PythonAnywhere.

Não envie a senha da conta por mensagem. Se alguma tela de login for necessária, faça essa parte diretamente no navegador.

## 16. Clonar o repositório no PythonAnywhere

1. No painel, abra **Consoles**.
2. Clique em **Bash**.
3. No terminal preto, execute:

```bash
git clone https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git
cd vitrine-aurora-flask
ls
```

O comando `ls` deve mostrar `app.py`, `requirements.txt`, `templates` e `static`.

## 17. Criar o ambiente virtual no PythonAnywhere

No mesmo terminal Bash, execute:

```bash
mkvirtualenv --python=/usr/bin/python3.13 vitrine-aurora
cd ~/vitrine-aurora-flask
pip install -r requirements.txt
```

Quando o ambiente estiver ativo, o começo da linha mostrará `(vitrine-aurora)`.

Se abrir outro terminal em outro momento, reative com:

```bash
workon vitrine-aurora
```

## 18. Criar a aplicação Web

1. Abra a guia **Web** no painel.
2. Clique em **Add a new web app**.
3. Avance na tela do domínio.
4. Escolha **Manual configuration**.
5. Escolha **Python 3.13**, a mesma versão usada no ambiente virtual.
6. Aguarde a criação da aplicação.

## 19. Informar a pasta e o ambiente virtual

Na guia **Web**, localize a seção **Code** e informe:

```text
Source code: /home/SEU_USUARIO/vitrine-aurora-flask
Working directory: /home/SEU_USUARIO/vitrine-aurora-flask
```

Troque `SEU_USUARIO` pelo nome da conta do PythonAnywhere.

Na seção **Virtualenv**, informe:

```text
vitrine-aurora
```

Depois de confirmar, o painel deve mostrar o caminho completo do ambiente virtual.

## 20. Configurar o arquivo WSGI

1. Ainda na guia **Web**, clique no link do arquivo WSGI.
2. Apague o exemplo que estiver no arquivo.
3. Cole o conteúdo abaixo, trocando `SEU_USUARIO`:

```python
import os
import sys

path = "/home/SEU_USUARIO/vitrine-aurora-flask"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ["SECRET_KEY"] = "troque-por-uma-chave-diferente"

from app import app as application
```

4. Clique em **Save**.

O arquivo WSGI permite que o servidor do PythonAnywhere importe a variável `app` existente em `app.py`. O `app.run()` não é usado na hospedagem.

## 21. Recarregar e abrir o sistema

1. Volte para a guia **Web**.
2. Clique no botão verde **Reload**.
3. Aguarde alguns segundos.
4. Clique no endereço mostrado no alto da página.

Em uma conta gratuita do sistema americano, o formato normalmente será:

```text
https://SEU_USUARIO.pythonanywhere.com
```

Em uma conta do sistema europeu, poderá ser:

```text
https://SEU_USUARIO.eu.pythonanywhere.com
```

Use exatamente o endereço exibido na guia **Web**.

## 22. Testar o sistema publicado

No endereço público:

1. confira a página inicial;
2. faça login com `anna@email.com` e `123456`;
3. abra anúncios, categorias e compras;
4. abra os dois relatórios;
5. clique em **Sair**;
6. tente abrir `/anuncios` sem login e confirme o redirecionamento;
7. diminua a janela para conferir o menu responsivo.

Se ocorrer erro, abra a guia **Web** e consulte os links de **Error log** e **Server log**.

## 23. Como atualizar o PythonAnywhere depois de outro commit

Abra um Bash no PythonAnywhere e execute:

```bash
cd ~/vitrine-aurora-flask
git pull origin main
workon vitrine-aurora
pip install -r requirements.txt
```

Depois, volte à guia **Web** e clique em **Reload**. Alterações no código precisam desse recarregamento.

## 24. Justificativas para a atividade

- A página inicial ficou pública para apresentar a plataforma; cadastros, alterações, exclusões e relatórios ficaram protegidos porque trabalham com informações internas.
- O Flask-Login foi utilizado para identificar o usuário da sessão e aplicar `@login_required` nas rotas protegidas.
- O logout encerra a sessão, evitando que outra pessoa continue usando o acesso no mesmo navegador.
- As senhas são salvas com hash para não manter o texto original no banco de dados.
- O Bootstrap foi aplicado ao menu, formulários, tabelas, alertas e botões para melhorar a organização e adaptar as páginas a computadores e celulares.
- O SQLite foi mantido por ser suficiente para este projeto acadêmico e funcionar no computador e no PythonAnywhere.
- O GitHub registra o histórico de commits e mantém o código-fonte público para avaliação.
- O PythonAnywhere foi escolhido conforme o enunciado para deixar o sistema acessível por um endereço público.

## 25. Checklist final

- [ ] Login correto entra no sistema.
- [ ] Login incorreto mostra mensagem.
- [ ] Logout encerra a sessão.
- [ ] Rotas internas redirecionam visitantes para o login.
- [ ] Cadastro cria uma nova conta.
- [ ] Menu funciona no computador e no celular.
- [ ] Formulários e tabelas usam Bootstrap.
- [ ] CRUDs e relatórios continuam funcionando.
- [ ] Commit está no GitHub com nome e e-mail da Anna.
- [ ] Repositório está público.
- [ ] Sistema abre no endereço do PythonAnywhere.
- [ ] Link público foi colocado no PDF.
- [ ] PDF está com o nome Anna Julia Torres Martins de Deus.

## 26. Links do trabalho

Repositório:

```text
https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git
```

Sistema implantado:

```text
https://SEU_USUARIO.pythonanywhere.com
```

Substitua o último endereço pelo link real mostrado na guia **Web** antes de gerar o PDF final.
