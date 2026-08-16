# Manual completo — Trilha 2 da Vitrine Aurora

Este manual foi escrito para quem está começando. Faça tudo na ordem e não pule etapas.

## 1. O que mudou nesta trilha

Na Trilha 1, as páginas e rotas do projeto foram criadas com dados demonstrativos. Na Trilha 2, o projeto passou a possuir:

- banco de dados SQLite;
- cadastro de registros (Create);
- listagem dos registros (Read);
- edição dos registros (Update);
- exclusão com confirmação (Delete);
- relatórios calculados usando os registros do banco.

Os CRUDs foram feitos para Usuário, Categoria, Anúncio, Pergunta, Compra e Favorito, que são as entidades definidas no MER.

## 2. Baixar e descompactar a atualização

1. Baixe o arquivo `Entrega_Trilha2_Vitrine_Aurora_Anna.zip`.
2. Abra a pasta **Downloads** do Windows.
3. Clique com o botão direito sobre o arquivo ZIP.
4. Clique em **Extrair Tudo**.
5. Escolha um local fácil, como a Área de Trabalho.
6. Clique em **Extrair**.
7. Dentro da pasta extraída estará a pasta `Anna_Ecommerce_Flask`.

## 3. Manter a ligação com o GitHub da Trilha 1

Como a atividade exige o mesmo repositório, o jeito mais simples é copiar os arquivos atualizados para dentro da pasta usada na Trilha 1:

1. Feche o servidor antigo pressionando `Ctrl + C` no terminal.
2. Abra a nova pasta `Anna_Ecommerce_Flask` que foi extraída.
3. Pressione `Ctrl + A` para selecionar os arquivos.
4. Pressione `Ctrl + C` para copiar.
5. Abra a pasta antiga do projeto que já foi enviada ao GitHub.
6. Pressione `Ctrl + V`.
7. Quando o Windows perguntar, escolha **Substituir os arquivos no destino**.

Não apague a pasta antiga antes de copiar. Ela contém a pasta oculta `.git`, responsável por manter a ligação com o repositório correto.

## 4. Abrir o projeto no VS Code

1. Abra o Visual Studio Code.
2. Clique em **File > Open Folder**.
3. Selecione a pasta antiga `Anna_Ecommerce_Flask`, agora com os arquivos atualizados.
4. Clique em **Select Folder**.
5. Se aparecer uma pergunta sobre confiar nos arquivos, confirme.
6. No Explorer devem aparecer `app.py`, `requirements.txt`, `README.md`, `templates` e `static`.

## 5. Abrir o terminal

1. No menu superior do VS Code, clique em **Terminal > New Terminal**.
2. O terminal aparecerá na parte inferior.
3. Confira se o caminho termina com `Anna_Ecommerce_Flask`.

Se o terminal estiver em outra pasta, feche-o e abra novamente depois de abrir a pasta correta no VS Code.

## 6. Ativar o ambiente virtual

Se a pasta `.venv` já existe por causa da Trilha 1, ative-a no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear, clique na seta ao lado do botão `+` do terminal, selecione **Command Prompt** e use:

```cmd
.venv\Scripts\activate.bat
```

Se a pasta `.venv` não existir, crie primeiro:

```bash
python -m venv .venv
```

Depois, use um dos comandos de ativação mostrados acima. Quando funcionar, aparecerá `(.venv)` no começo da linha do terminal.

## 7. Instalar a nova dependência

Mesmo que o Flask já esteja instalado, execute novamente:

```bash
python -m pip install -r requirements.txt
```

Esse comando instalará o Flask e o Flask-SQLAlchemy. O SQLAlchemy é usado para trabalhar com o banco de dados.

## 8. Executar o sistema

No terminal, digite:

```bash
python app.py
```

Deve aparecer um endereço parecido com:

```text
http://127.0.0.1:5000
```

Segure `Ctrl` e clique no endereço ou copie e cole no Chrome. Esse endereço local é normal e pode ser igual ao da Trilha 1.

Na primeira execução, o arquivo `vitrine_aurora.db` será criado automaticamente. Ele guardará os registros cadastrados.

## 9. Testar o CRUD de usuários

1. Clique em **Usuários** no menu.
2. Confira se a lista aparece.
3. Clique em **+ Novo usuário**.
4. Preencha nome, e-mail e senha.
5. Clique em **Salvar**.
6. Confira se o novo usuário apareceu na lista.
7. Clique em **Editar**, altere o nome e salve.
8. Confira se o nome foi atualizado.
9. Clique em **Excluir**.
10. Confira a página de confirmação.
11. Clique em **Sim, excluir** apenas se quiser remover o registro.

Isso demonstra Create, Read, Update e Delete.

## 10. Testar o CRUD de categorias

1. Clique em **Categorias**.
2. Clique em **+ Nova categoria**.
3. Informe o nome e a descrição.
4. Salve o cadastro.
5. Use **Editar** para alterar a descrição.
6. Use **Excluir** e confira a tela de confirmação.

## 11. Testar o CRUD de anúncios

Antes de criar um anúncio, deve existir pelo menos um usuário e uma categoria.

1. Clique em **Anúncios**.
2. Clique em **+ Novo anúncio**.
3. Preencha título, descrição, preço e data.
4. Selecione o anunciante.
5. Selecione a categoria.
6. Clique em **Salvar**.
7. Teste os botões **Editar** e **Excluir**.

## 12. Testar perguntas e respostas

Antes deste teste, deve existir um usuário e um anúncio.

1. Clique em **Perguntas**.
2. Clique em **+ Nova pergunta**.
3. Digite a pergunta e escolha o usuário e o anúncio.
4. A resposta e a data da resposta podem ficar vazias no primeiro cadastro.
5. Salve.
6. Na lista, a pergunta aparecerá como **Pendente**.
7. Clique em **Editar**.
8. Digite a resposta do anunciante e informe a data.
9. Salve novamente.
10. A situação mudará para **Respondida**.
11. O botão **Excluir** abre a confirmação antes da remoção.

## 13. Testar o CRUD de compras

1. Clique em **Compras**.
2. Clique em **+ Nova compra**.
3. Informe data, quantidade e valor total.
4. Selecione o comprador e o anúncio.
5. Clique em **Salvar**.
6. Teste a edição do valor ou da quantidade.
7. Teste a exclusão com confirmação.

Não existe carrinho de compras porque o enunciado informa que a compra é feita diretamente em um anúncio.

## 14. Testar o CRUD de favoritos

1. Clique em **Favoritos**.
2. Clique em **+ Novo favorito**.
3. Selecione um usuário e um anúncio.
4. Informe a data e salve.
5. Teste **Editar** e **Excluir**.

O mesmo anúncio não pode ser adicionado duas vezes aos favoritos do mesmo usuário. Essa regra evita registros repetidos.

## 15. Conferir os relatórios

1. Passe o mouse sobre **Relatórios** no menu.
2. Clique em **Minhas compras**.
3. Confira produto, comprador, data, valor e total.
4. Volte ao menu **Relatórios**.
5. Clique em **Minhas vendas**.
6. Confira o vendedor de cada anúncio e o total.

Os relatórios são atualizados automaticamente quando uma compra é cadastrada, editada ou excluída.

## 16. Entender a estrutura

```text
Anna_Ecommerce_Flask/
|-- app.py
|-- requirements.txt
|-- README.md
|-- MANUAL_PASSO_A_PASSO.md
|-- vitrine_aurora.db              criado automaticamente
|-- static/
|   `-- style.css
`-- templates/
    |-- base.html
    |-- index.html
    |-- formulario.html
    |-- confirmar_exclusao.html
    |-- relatorio.html
    |-- usuarios/lista.html
    |-- categorias/lista.html
    |-- anuncios/lista.html
    |-- perguntas/lista.html
    |-- compras/lista.html
    `-- favoritos/lista.html
```

- `app.py`: modelos do banco, rotas e operações CRUD.
- `vitrine_aurora.db`: banco de dados SQLite.
- `base.html`: menu e estrutura comum das páginas.
- `formulario.html`: formulário usado para cadastrar e editar.
- `confirmar_exclusao.html`: confirmação antes da exclusão.
- pastas das entidades: tabelas de listagem.
- `style.css`: cores e layout da Vitrine Aurora.

## 17. Como o CRUD aparece no código

- **Create:** rotas terminadas em `/novo` ou `/nova`, usando `db.session.add()`.
- **Read:** rotas de listagem, como `/usuarios` e `/anuncios`, usando consultas ao banco.
- **Update:** rotas terminadas em `/editar`, que carregam e alteram um registro existente.
- **Delete:** rotas terminadas em `/excluir`, com confirmação e `db.session.delete()`.
- `db.session.commit()` confirma e salva a alteração no SQLite.

## 18. Parar e abrir novamente

Para parar o sistema, volte ao terminal e pressione:

```text
Ctrl + C
```

Para abrir outra vez em outro dia:

1. Abra a pasta no VS Code.
2. Abra o terminal.
3. Ative `.venv`.
4. Execute `python app.py`.
5. Abra `http://127.0.0.1:5000`.

## 19. Atualizar o mesmo repositório no GitHub

O repositório correto é:

```text
https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git
```

Com o terminal dentro da pasta antiga do projeto, execute um comando por vez:

```bash
git status
git add .
git commit -m "Implementa CRUDs completos com banco de dados"
git push origin main
```

O primeiro comando apenas mostra as mudanças. O segundo prepara os arquivos. O terceiro cria o histórico solicitado pela atividade. O quarto envia a atualização ao mesmo repositório.

Se aparecer `nothing to commit`, confirme se os arquivos novos foram realmente copiados para dentro da pasta antiga ligada ao GitHub.

Se aparecer erro 403 mencionando outra conta, faça login no GitHub com a conta `anninhamt2605-pixel` e tente novamente.

## 20. Conferir o GitHub

1. Abra https://github.com/anninhamt2605-pixel/vitrine-aurora-flask no Chrome.
2. Atualize a página com `Ctrl + F5`.
3. Confira se `app.py` mostra as classes do banco de dados.
4. Confira se as novas pastas de templates aparecem.
5. Confira se o commit **Implementa CRUDs completos com banco de dados** está visível.
6. Confirme que o repositório continua como **Public**.

## 21. Justificativas usadas na atividade

- O SQLite foi escolhido porque é simples e suficiente para um projeto acadêmico, além de salvar os dados em um arquivo local.
- O Flask-SQLAlchemy foi utilizado para representar as entidades do MER como classes e facilitar as operações no banco.
- Cada entidade recebeu rotas de cadastro, listagem, edição e exclusão para cumprir o CRUD completo.
- A confirmação de exclusão foi criada para evitar remoções acidentais.
- Os formulários possuem campos obrigatórios e valores mínimos para diminuir erros de preenchimento.
- Os relacionamentos do MER foram preservados por meio das chaves estrangeiras.
- Os relatórios consultam as compras armazenadas, por isso refletem os dados reais do sistema.

## 22. Checklist antes de entregar

- [ ] O sistema abre com `python app.py`.
- [ ] O banco `vitrine_aurora.db` foi criado.
- [ ] As seis entidades possuem cadastro, lista, edição e exclusão.
- [ ] Toda exclusão pede confirmação.
- [ ] Os relatórios carregam sem erro.
- [ ] O código foi enviado ao mesmo repositório da Trilha 1.
- [ ] O novo commit aparece no histórico do GitHub.
- [ ] O repositório está público.
- [ ] O nome Anna Julia Torres Martins de Deus está correto no PDF.
- [ ] O PDF da Trilha 2 foi anexado no AVA.
