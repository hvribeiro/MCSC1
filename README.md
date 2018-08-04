# MCSC1 - Material do curso de Métodos Computacionais em Sistemas Complexos I

- *Périodo de aulas:* 06/08 a 21/12 (20 aulas)
- *Local:* G68 - sala 11
- *Horário:* às quartas-feiras de 13:30 a 17:00
- *Forma de avaliação:* a definir
- Livro texto: José Unpingco, *Python for Probability, Statistics, and Machine Learning*, Springer (2016).
[![Alt Text](https://images.springer.com/sgw/books/medium/9783319307152.jpg)](http://library1.org/_ads/E844412DCACEB5A9BF29267FA244E908)


## Conteúdo do repositório
- */aulas* - .ipynb com as apresentações
- */refs* - referências que usamos
- */extras*

## Dicas e indicações

- [Think Python 2nd Edition by Allen B. Downey](http://greenteapress.com/thinkpython2/thinkpython2.pdf) 
- [SciPy 2018 Tutorial sobre numpy](https://www.youtube.com/watch?v=V0D2mhVt7NE)
- [SciPy 2018 Tutorial sobre pandas](https://www.youtube.com/watch?v=lkLl_QKLgcA)
- [SciPy 2018 Tutorial sobre matplotlib](https://www.youtube.com/watch?v=6gdNUDs6QPc)
- [SciPy 2016 Tutorial sobre sympy](https://www.youtube.com/watch?v=AqnpuGbM6-Q)
- [Lista de commandos do git](https://github.com/hvribeiro/MCSC1/blob/master/extras/zt_git_cheat_sheet.pdf)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Repositório do Unpingco com códigos e praticamente o livro todo em jupyter notebooks](https://github.com/unpingco/Python-for-Probability-Statistics-and-Machine-Learning)

#### Primeiros passos com o git

Para instalar
```sh
sudo apt-get install git-core
```
Para dizer quem você é
```sh
git config --global user.name "Seu Nome"
git config --global user.email seu_email@alguma_coisa.com
```
Se quiser deixar a senha salva para todos repositórios
```sh
git config --global credential.helper store
```
Sua senha fica gravada no arquivo de texto plano *.git-credentials* no seu %HOME%.

Para clonar esse repositório use
```sh
git clone https://github.com/hvribeiro/MCSC1.git 
```

#### Primeiros passos com a Anaconda

- Faça o download da versão 3.x em https://www.anaconda.com/download/ ou use o [link direto](https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh) para o .sh
- Siga as instruções em https://docs.anaconda.com/anaconda/install/linux

Basicamente é executar
```sh
sh Anaconda3-5.2.0-Linux-x86_64.sh
```
e seguir os passos do instalador.

Para atualizar todos os pacotes
```sh
conda update --all
```

Para instalar um pacote
```sh
pip install Nome_do_Pacote
```

