from loja import biblioteca

def teste_da_função_cadastrar_livro():
    livro=biblioteca.livro()
    livro.cadastrar(título="As Aventuras de Tim-Tim" , código = "#i98$l")
    print(livro())

def teste_da_função_cadastrar_estante():
    estante=biblioteca.estante()
    estante.cadastrar(temática="infantiu" , qtd_de_prateleiras_cheias = "6")
    print(estante())

def teste_da_função_inclusão_de_livro_na_estante():
    estante=biblioteca.estante()
    estante.cadastrar(temática="infantiu" , qtd_de_prateleiras_cheias = "6")
    alocar_livros("#i98$l")

def exclusão_de_estante():
    pass

def inclusão_de_estante():
    pass

teste_da_função_cadastrar_livro()
teste_da_função_cadastrar_estante()

