#!/usr/bin/env python
# coding: utf-8

# # _Dataviz Workshop_:_Dashboarding_ com _Dash_

# ## Objetivos do workshop
# 
# - Apresentar o ecossistema _Dash_ para criação de aplicações web para exploração e visualização de dados;
# - Compreender o processo básico de criação de um _dashboard_ utilizando _Dash_;
# - Desenvolver um _dashboard_ simples para exploração de dados sobre crimes violentos letais intencionais em João Pessoa.

# ## Ferramentas utilizadas
# 
# - Módulos Python    
#     - `dash`
#     - `dash_bootstrap_componentes`
#     - `plotly`
#     - `os`
#     - `pandas`
#     - `python` (interpretador)

# ## Sobre o _Dash_

# > _Dash is the original low-code framework for rapidly building data apps in Python._
# 
# - Ou seja, _Dash_ é um ecossistema que nos permite criar aplicações para exploração e visualização de dados para a web de forma rápida e totalmente em Python. 
# 
# - Basicamente, o _Dash_ é uma possui três componentes fundamentais:
#     - [_Flask_](https://flask.palletsprojects.com/en/2.3.x/): a ferramenta de _backend_;
#     - [_Plotly_](https://plotly.com/python/): a feramenta que provê as bibliotecas de plotagem (em nosso caso, usamos Python);
#     - [_React_](https://react.dev): a ferramenta que fornece o arcabouço interativo e de _frontend_;
# 
# - Uma vez que o Dash tem a vantagem de facilitar o desenvolvimento de aplicações puramente em Python, não é necessário conhecer profundamente HTML, CSS ou Javascript, por exemplo.
# 
# - Figuras feitas em matplotlib podem ser convertidas para _Dash_ com 
# `plotly.tools.mpl_to_plotly` (checar)

# ### Instalação
# 
# É recomendável instalar o _Dash_ através do _pip_: `pip install dash`.

# ### Pacotes essenciais
# 
# O _Dash_ contém alguns pacotes essenciais dedicados a funcionalidades específicas, a saber:
# - `Dash`: pacote principal e _backbone_ de qualquer aplicação a ser criada;
# - `Dash Core Components`: pacote de componentes interativas de manipulação (botões, _dropdowns_, _sliders_ etc.);
# - `Dash HTML Components`: pacote que fornece elementos HTML como classes Python;
# - `Dash Bootstrap Components`: pacote mantido por terceiros que cuida das opções _bootstrap_ (controle visual, opções de layout, interface etc.)

# ### Processo geral de criação de apps em Dash
# 
# - _Importações_ (_boilerplate_): receita básica de importação de módulos.
# - _Instanciamento_: criação do app via `Dash`;
# - _Chamada de layout_: formação dos contêineres e elementos básicos do _frontend_, principalmente via HTML. 
# - _Chamada de callbacks_: uso de decoradores Python que se aplicam a funções mais genéricas que tratam da disposição das representações visuais e da interatividade.
# - _Execução_: _deployment_ via comando Python.
# 

# ## Exemplos
# 
# Os exemplos são gerados por execução dos scripts acessórios localizados no diretório `dw`.
# 
# 
# - Demonstração básica: `python ../dw/dw1a.py`
# - Plataforma CVLI: `python ../dw/dw1b.py`

# ## Referência
# 
# [Dash User Guide](https://dash.plotly.com)
