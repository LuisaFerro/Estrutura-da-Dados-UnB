Grafo, referência [livro da disciplina](https://panda.ime.usp.br/pythonds/static/pythonds_pt/07-Grafos/toctree.html)

Sendo Grafo -> G = (V,E). 

    Em que V = vértices e E = Arestas
    Cada aresta é uma tupla
    
Gráfos têm informações dependêntes: [Representação por listas de adjacência](https://panda.ime.usp.br/pythonds/static/pythonds_pt/07-Grafos/AnAdjacencyList.html)


![grafo](https://panda.ime.usp.br/pythonds/static/pythonds_pt/_images/digraph.png)

Herança: Herda métodos e atributos de uma classe mãe;
Portanto:

Class DFSGraph(Graph): -> a classe DFSGraph HERDOU de Graph todos os atributos
    def __init__(self):
        super().__init__() -> comando que herda os atributos da classe mãe
        sel.time = 0 -> Aqui adicionamos um novo atributo só para essa classe criada
    

OBS: O super serve para - em uma relação de herança entre uma classe Base e outra Derivada - permitir que a classe Derivada se refira explicitamente à classe Base.

O super não serve somente para o construtor, é claro: qualquer método da classe Base pode ser chamado dessa forma pela classe Derivada:

______________________________________________________________________________________

Sendo pytohn fracamente tipada, n precisa-se definir o tipo das variáveis, como em C++, no começo. Sendo assim.
    

