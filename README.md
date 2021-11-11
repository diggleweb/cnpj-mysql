[![Me pague um ☕ ](https://img.shields.io/badge/Buy%20me%20a%20%E2%98%95%20-%20Patreon%20-yellowgreen)](https://www.patreon.com/bePatron?u=46149384 "Paga um café para nos")
[![Github](https://img.shields.io/badge/creator-alexyucra-red)](https://github.com/diggleweb)

# Novo Layout para os DADOS ABERTOS do CNPJ

## download de arquivos

Este processo executará um processo para cada arquivo.

- copie o repositorio [git@github.com:diggleweb/cnpj-mysql.git](git@github.com:diggleweb/cnpj-mysql.git)
    > $ cd cnpj-mysql
- no arquivo `download.py` configure as pastas para download dos dados e logs
    > nano download.py

    ```
    path_download = '<path>/download'
    ```
- Instale librerias
    > $ python3 -m pip install bs4
    > $ python3 -m pip install requests
- run download
    > $ python3 download.py

## deploy in mysql
