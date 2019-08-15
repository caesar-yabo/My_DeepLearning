def prime(node_array, start_node, graph_matrix):
    index_start_node = node_array.index(start_node)
    node_list = []
    node_list.append(start_node)

    pre = [] # 记录父节点
    lowcost = []

    length_nodes = len(node_array)

    # 初始化
    for i in range(length_nodes):
        lowcost.append(graph_matrix[index_start_node][i])
        pre.append(index_start_node)
    lowcost[index_start_node] = -1

    sum_ = 0
    for _ in range(1, length_nodes):
        minid = index_start_node
        min_ = float('inf')
        for j in range(length_nodes):
            if lowcost[j] != -1 and lowcost[j] < min_:
                min_ = lowcost[j]
                minid = j

        node_list.append(node_array[minid])
        lowcost[minid] = -1
        sum_ += min_

        # 更新lowcost
        for j in range(length_nodes):
            if lowcost[j] != -1 and lowcost[j] > graph_matrix[minid][j]:
                lowcost[j] = graph_matrix[minid][j]
                pre[j] = minid

    pre = list(node_array[x] for x in pre)
    return sum_, node_list, pre


if __name__ == '__main__':
    MAX = float('inf')
    node_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    graph_matrix = [[MAX, 10, MAX, MAX, MAX, 11, MAX, MAX, MAX],
                    [10, MAX, 18, MAX, MAX, MAX, 16, MAX, 12],
                    [MAX, 18, MAX, 22, MAX, MAX, MAX, MAX, 8],
                    [MAX, MAX, 22, MAX, 20, MAX, MAX, 16, 21],
                    [MAX, MAX, MAX, 20, MAX, 26, 7, 19, MAX],
                    [11, MAX, MAX, MAX, 26, MAX, 17, MAX, MAX],
                    [MAX, 16, MAX, MAX, 7, 17, MAX, 19, MAX],
                    [MAX, MAX, MAX, 16, 19, MAX, 19, MAX, MAX],
                    [MAX, 12, 8, 21, MAX, MAX, MAX, MAX, MAX]]

    sum_, node_list, mid = prime(node_array, 'B', graph_matrix)
    print(sum_)
    print(node_list)
    print(mid)
