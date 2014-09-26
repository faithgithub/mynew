__author__ = 'zxh'
m = 3
n = 3
citys = 4
input_num = '010000020'

def get_tops(m,n):
    tops = []
    for i in range(m):
        for j in range(n):
            top = (i,j)
            tops.append(top)

    return tops
def get_start_special(input_num,tops):
    j = 0
    start,special = None,None
    for i in input_num:
        if int(i)==1:
            start = tops[j]
        if int(i)==2:
            special = tops[j]
        j+=1
    return (start,special)
def judge_distance(a,b):
    flag = False
    distance = (b[0]-a[0])**2+(b[1]-a[1])**2
    if 0<distance<=2:
        flag=True
    return flag


def create_graph(tops):
    graph = {}
    for i in tops:
        tmp_list = []
        for j in tops:
            flag = judge_distance(i,j)
            if flag:
                tmp_list.append(j)
        graph[i] = tmp_list
    return graph

def find_all_paths(graph, start,citys, path=None):
    path = [] if not path else path
    path = path + [start]
    if len(path)==citys:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node,citys, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
def get_special_paths(paths,special):
    special_paths = []
    for i in paths:
        if special in i:
                special_paths.append(i)
    return special_paths

tops = get_tops(m,n)
start,special = get_start_special(input_num,tops)
graph = create_graph(tops)
paths = find_all_paths(graph,start,citys)
special_paths = get_special_paths(paths,special)
print special_paths,len(special_paths)
