class biblioteca:

    class livro: 
        def __init__(self): 
            self.título = None
            self.subtítulo = None
            self.capítulos = None
            self.páginas = None
            self.editora = None
            self.nome_do_autor = None
            self.data_de_publicação = None
            self.estrangeiro = None
            self.edição = None
            self.classificação_etária = None
            self.dipónivel = None
            self.título_oiginal = None
            self.revisão = None
            self.capa = None
            self.largura_do_livro = None
            self.altura_do_livro = None
            self.profundidade_do_livro = None
            self.código = None

        def cadastrar (self,título=None,subtítulo=None,capítulos=None,páginas=None,
        editora=None,nome_do_autor=None,data_de_publicação=None,estrangeiro=None,
        edição=None,classificação_etária=None,dipónivel=None,título_oiginal=None,
        revisão=None,capa=None,largura_do_livro=None,altura_do_livro = None,
        profundidade_do_livro=None, código=None): 
            self.título = título 
            self.subtítulo = subtítulo
            self.capítulos = capítulos
            self.páginas = páginas
            self.editora = editora
            self.nome_do_autor = nome_do_autor
            self.data_de_publicação = data_de_publicação
            self.estrangeiro = estrangeiro
            self.edição = edição
            self.classificação_etária = classificação_etária
            self.dipónivel = dipónivel
            self.título_oiginal = título_oiginal
            self.revisão = revisão
            self.capa = capa
            self.largura_do_livro = largura_do_livro
            self.altura_do_livro = altura_do_livro 
            self.profundidade_do_livro = profundidade_do_livro
            self.código = código

        def cod (self): 
            return self.código

        def __call__(self):
            return self.__dict__

    class estante:
        def __init__(self):
            self.temáticas = None
            self.largura_da_estante = None
            self.altura_da_estante = None
            self.profundidade_da_estante = None
            self.qtd_total_de_prateleiras = None
            self.qtd_de_prateleiras_vazias = None
            self.qtd_de_prateleiras_semipreenchidas = None
            self.qtd_de_prateleiras_cheias = None
            self.livros = []

        def cadastrar(self,temáticas = None,largura_da_estante = None,altura_da_estante = None,
        profundidade_da_estante = None,qtd_total_de_prateleiras = None,
        qtd_de_prateleiras_vazias = None,qtd_de_prateleiras_semipreenchidas = None,
        qtd_de_prateleiras_cheias = None):
            self.temáticas = temáticas
            self.largura_da_estante = largura_da_estante
            self.altura_da_estante = altura_da_estante
            self.profundidade_da_estante = profundidade_da_estante
            self.qtd_total_de_prateleiras = qtd_total_de_prateleiras
            self.qtd_de_prateleiras_vazias = qtd_de_prateleiras_vazias
            self.qtd_de_prateleiras_semipreenchidas = qtd_de_prateleiras_semipreenchidas
            self.qtd_de_prateleiras_cheias = qtd_de_prateleiras_cheias
            
        def alocar_livros(self,*código_do_livro):
            self.livros.append(código_do_livro)

        def desalocar_livros(self,código_do_livro):
            self.livros.remove(código_do_livro)

        def catalogo(self):    
            return self.livros

        def __call__(self):
            return self.__dict__


#=======================Area de teste=========================#
livro1=biblioteca.livro()
estante=biblioteca.estante()
livro1.cadastrar("Minecraft",código="#i98$l")
print(livro1())
print(livro1.título)

livro2=biblioteca.livro()
estante=biblioteca.estante()
livro2.cadastrar("Jazzghost",código="#i99$l")
print(livro2())
print(livro2.título)

estante.alocar_livros(livro1.código,livro2.código)

print(estante())