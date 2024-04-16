from queue import Queue
from copy import deepcopy

class Graph:

  def __init__(self, lis1, lis2):
    self.graph = []
    self.revers_graph = []
    self.lis_aux_cri = []
    self.lis_rev = []
    self.lis_criticos = []
    self.in_list_nodes = []
    self.in_list_edges = []
    self.res = []
    self.s = Queue

    for i in range(1, len(lis1)+1):
      self.in_list_nodes.append(i)

    self.in_list_edges = deepcopy(lis2)
    
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

    return self.graph, self.revers_graph

  def bfs(self, in_graph):
    
    out_graph = []
    out_graph = deepcopy(in_graph)
    lis_aux = []
    
    s = []
    tot_trees = 0

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

    res = []
    
    if self.lis_aux_cri[0][0] == 1 and self.lis_aux_cri[1][0] == 1:

      res = ["GREEN", deepcopy(self.in_list_nodes)]

    elif self.lis_aux_cri[0][0] == 1 or self.lis_aux_cri[1][0] == 1:
      res = ["YELLOW", deepcopy(self.in_list_nodes)]

    else:

      res = ["RED", deepcopy(self.in_list_nodes)]
    
    return res

  def run(self):
    
    g, grev = Graph.build_graph(self, self.in_list_nodes, self.in_list_edges)

    Graph.bfs(self, g)
    Graph.bfs(self, grev)

    resp = Graph.analisa_criticos(self)

    return resp
