from queue import Queue
from copy import deepcopy




class Graph:

  def __init__(self, lis1, lis2):
    self.graph = []
    self.revers_graph = []
    self.lis_aux_cri = []
    self.lis_rev = []
    self.lis_criticos = []
    self.res = []
    self.s = Queue

    self.in_list_nodes = deepcopy(lis1)
    self.in_list_edges = deepcopy(lis2)

    # aqui mais tarde, vai receber a entrada certinha:


    

  def build_graph(self, lis_nodes, lis_edges):
      
    self.graph.append(len(lis_nodes))
    self.revers_graph.append(len(lis_nodes))

    
    for n in lis_nodes:
      
      nod = [False, n , []]
      self.graph.append(nod)
      self.revers_graph.append(deepcopy(nod))

    for v, u in lis_edges:
      
      self.graph[v][2].append(u)
      self.revers_graph[u][2].append(v)

    # print(graph)
    # print(revers_graph)

    return self.graph, self.revers_graph

  def bfs(self, in_graph):
    
    out_graph = []
    out_graph = deepcopy(in_graph)
    lis_aux = []
    
    s = []
    tot_trees = 0

    print(in_graph)
    print(out_graph)

    for i in range(1, out_graph[0]+1):
      if not out_graph[i][0]:
        s.append(out_graph[i][1])
        out_graph[i][0] = True

        tot_trees += 1
        lis_aux.append(out_graph[i][1])


        while s:
          v = s.pop(0)

          for u in out_graph[v][2]:
            if not out_graph[u][0]:
              out_graph[u][0] = True
              s.append(u)



    self.lis_aux_cri.append([tot_trees, deepcopy(lis_aux)])

    return tot_trees
            

  def analisa_criticos(self):

    # som_crit = lis_aux_cri[0][0] + lis_criticos[1][0]

    # # if som_crit == 2:

    res = []
    res = deepcopy(self.in_list_nodes)

    
    print(res)
    
    return self.in_list_nodes




    # return lis_criticos

lis1 = [1, 2, 3, 4, 5, 6, 7]
lis2 = [[1,2], [1,4], [1,5], [2,3], [3,4], [4,1], [5,6], [6,7]]
          
test1 = Graph(lis1, lis2)

g = []
grev = []

g, grev = test1.build_graph(lis1, lis2)

test1.bfs(g)

test1.bfs(grev)

test1.analisa_criticos()

# print(lis_aux_cri)

# build_revers_graph(nodes)
