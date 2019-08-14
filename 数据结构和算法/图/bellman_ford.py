def bellman_ford(graph, source):
    dist = {}
    pre = {} # 存放父节点
    paths = {} # 求源点到各节点的路径
    inf = float('inf')
    # 初始化
    for v in graph:
        dist[v] = inf
        paths[v] = [v]
        pre[v] = None
    dist[source] = 0
    paths.pop(source)

    for i in range(len(graph)-1):# 循环n-1次
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    pre[v] = u # 完成松弛操作，u为v的前驱结点

    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]: # 判断是否存在环路
                return None, None

    for u in paths:
        temp = u
        while pre[temp] != None and pre[temp] != source:
            paths[u].append(pre[temp])
            temp = pre[temp]
        paths[u].append(source)
        paths[u] = list(reversed(paths[u]))

    return dist, pre, paths


def test():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 2, 'd': 3, 'e': 2},
        'c': {},
        'd': {'b': 3, 'c': 5},
        'e': {'d': -3}
    }
    dist, p, paths = bellman_ford(graph, 'a')
    print(dist)
    print(p)
    print(paths)


if __name__ == '__main__':
    test()



    # def testfail():
    #     graph = {
    #         'a': {'b': -1, 'c': 4},
    #         'b': {'c': 2, 'd': 3, 'e': 2},
    #         'c': {'d': -5},
    #         'd': {'b': 3},
    #         'e': {'d': -3}
    #     }
    #     dist, p = bellman_ford(graph, 'a')
    #     print(dist)
    #     print(p)
    
    
    
    # testfail()
