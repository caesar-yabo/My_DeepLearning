import copy
class Graph_matrix():
    def __init__(self):
        self.storage_matrix = []
        self.node_list = []


    def make_graph(self, matrix, _nodes):
        self.node_list = _nodes
        for m in matrix:
            self.storage_matrix.append(m)


    def dict_min_by_value(self, this_dict):
        min_ = float('inf'  )
        key = ''
        for item in this_dict.items():
            if item[-1] < min_:
                min_ = item[-1]
                key = item[0]

        return key


    def get_node_index(self, node):
        return self.node_list.index(node)


    def dijkstra(self, start_node):
        over_node = {start_node: 0}
        found_node = dict()
        i = self.get_node_index(start_node)
        # 初始化
        for j in range(len(self.storage_matrix[i])):
            if j != i:
                found_node[self.node_list[j]] = self.storage_matrix[i][j]

        while found_node:
            min_key = self.dict_min_by_value(found_node)
            over_node[min_key] = found_node[min_key]
            found_node.pop(min_key)
            # 更新found_node值
            i = self.get_node_index(min_key)
            for node_item in found_node.items():
                j = self.get_node_index(node_item[0])
                if node_item[-1] > over_node[min_key] + self.storage_matrix[i][j]:
                    found_node[node_item[0]] = over_node[min_key] + self.storage_matrix[i][j]

        print(over_node)


    def dijkstra_path(self, start_node):
        length = len(self.storage_matrix)
        i = self.get_node_index(start_node)
        paths = dict()
        path_parent = [i]*length

        over_node = {start_node: 0}
        found_node = dict()

        # 初始化
        for j in range(len(self.storage_matrix[i])):
            if j != i:
                found_node[self.node_list[j]] = self.storage_matrix[i][j]

        while found_node:
            min_key = self.dict_min_by_value(found_node)
            over_node[min_key] = found_node[min_key]
            found_node.pop(min_key)
            # 更新found_node值
            i = self.get_node_index(min_key)

            path = []
            path.append(str(i))
            k = i
            while (path_parent[k] != self.get_node_index(start_node)):  # 找该节点的父节点添加到path，直到父节点是start
                path.append(str(path_parent[k]))
                k = path_parent[k]
            path.append(str(self.get_node_index(start_node)))
            path.reverse()  # path反序产生路径

            # paths[i] = path # 路径存储为index
            # print(str(i) + ':', '->'.join(path))

            paths[self.node_list[i]] = [self.node_list[int(x)] for x in path] # 路径存储为节点名
            # print(self.node_list[i]+':', '->'.join([self.node_list[int(x)] for x in path]))

            for node_item in found_node.items():
                j = self.get_node_index(node_item[0])
                if node_item[-1] > over_node[min_key] + self.storage_matrix[i][j]:
                    found_node[node_item[0]] = over_node[min_key] + self.storage_matrix[i][j]
                    path_parent[j] = i
        # print(over_node)
        return over_node, paths



    def floyd(self):
        len_node_list = len(self.node_list)
        # res = copy.deepcopy(self.storage_matrix)
        # res = [x for x in self.storage_matrix]
        res = [[0]*len_node_list]*len_node_list
        for i in range(len_node_list):
            for j in range(len_node_list):
                res[i][j] = self.storage_matrix[i][j]


        for k in range(len_node_list):
            for i in range(len_node_list):
                for j in range(len_node_list):
                    if res[i][j] > res[i][k]+res[k][j]:
                        res[i][j] = res[i][k]+res[k][j]
        return res

if __name__ == '__main__':
    
    m = float('inf')  # 代替表示无穷大
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    distance = [[0, 12, m, m, m, 16, 14],  # a
                [12, 0, 20, m, m, 7, m],  # b
                [m, 20, 0, 3, 5, 6, m],  # c
                [m, m, 3, 0, 4, m, m],  # d
                [m, m, 5, 4, 0, 2, 8],  # e
                [16, 7, 6, m, 2, 0, 9], # f
                [14, m, m, m, 8, 9, 0]]  # g
    test = Graph_matrix()
    test.make_graph(distance,nodes)
    # test.dijkstra('c')
    print('d:')
    length, paths = test.dijkstra_path('d')
    print(length)
    print(paths)
    
    
    
    
    # m = float('inf')  # 代替表示无穷大
    # nodes = ['a', 'b', 'c', 'd', 'e', 'f']
    # distance = [[0, 7, 9, m, 14, m],  # a
    #             [7, 0, 10, 15, m, m],  # b
    #             [9, 10, 0, 11, 2, m],  # c
    #             [m, 15, 11, 0, m, 6],  # d
    #             [14, m, 2, m, 0, 9],  # e
    #             [m, m, m, 6, 9, 0]]  # f
    # test = Graph_matrix()
    # test.make_graph(distance,nodes)
    # # test.dijkstra('c')
    # print('a:')
    # test.dijkstra('a')
    
    # print('b:')
    # test.dijkstra('b')
    # print('c:')
    # test.dijkstra('c')
    # print('d:')
    # test.dijkstra('d')
    # print('e:')
    # test.dijkstra('e')
    # print('f:')
    # test.dijkstra('f')
    
    # print(test.storage_matrix)
    # print(test.floyd())
    # print(test.storage_matrix)
