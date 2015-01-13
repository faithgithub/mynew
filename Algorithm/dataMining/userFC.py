# coding=utf-8
__author__ = "wxy"
import sys,math
from texttable import Texttable
#读取文件
def readFile(file_name):
    with open(file_name) as f:
       for i in f.readlines():
           yield i
#
#   解压rating信息，格式：用户id\电影id\t用户rating\t时间
#   输入：数据集合
#   输出:已经解压的排名信息
#
def getRatingInformation(ratings):
    rates = []
    for i in ratings:
        try:
            rate = i.split('\t')
            rates.append([int(rate[0]),int(rate[1]),int(rate[2])])
        except Exception,e:
            print str(e)
    return rates
#
#   生成用户评分的数据结构
#
#   输入:所以数据 [[2,1,5],[2,4,2]...]
#   输出:1.用户打分字典 2.电影字典
#   使用字典，key是用户id，value是用户对电影的评价，
#   rate_dic[2]=[(1,5),(4,2)].... 表示用户2对电影1的评分是5，对电影4的评分是2
#
def createUserRankDic(rates):
    user_dict = {}
    movie_dict = {}
    for i in rates:
        user_rank = (i[1],i[2])
        if i[0] in user_dict:
            user_dict[i[0]].append(user_rank)
        else:
            user_dict[i[0]] = [user_rank]
        if i[1] in movie_dict:
            movie_dict[i[1]].append(i[0])
        else:
            movie_dict[i[1]] = [i[0]]
    return  user_dict,movie_dict
#
#
#   相似余弦距离
#   使用 |A&B|/sqrt(|A || B |)计算余弦距离
#
#
def calcSimlaryCosDist(user1,user2):
    sum_x=0.0
    sum_y=0.0
    sum_xy=0.0
    avg_x=0.0
    avg_y=0.0
    for key in user1:
        avg_x+=key[1]
    avg_x=avg_x/len(user1)

    for key in user2:
        avg_y+=key[1]
    avg_y=avg_y/len(user2)

    for key1 in user1:
        for key2 in user2:
            if key1[0]==key2[0] :
                sum_xy+=(key1[1]-avg_x)*(key2[1]-avg_y)
                sum_y+=(key2[1]-avg_y)*(key2[1]-avg_y)
        sum_x+=(key1[1]-avg_x)*(key1[1]-avg_x)

    if sum_xy == 0.0 :
        return 0
    sx_sy=math.sqrt(sum_x*sum_y)
    return sum_xy/sx_sy
#
#   计算与指定用户最相近的邻居
#   输入:指定用户ID，所以用户数据，所以物品数据
#   输出:与指定用户最相邻的邻居列表
#
def calcNearestNeighbor(userid,users_dic,item_dic):
    ngb = []
    for i in users_dic[userid]:
        for n in item_dic[i[0]]:
            if n!=userid and n not in ngb:
                ngb.append(n)
    ngb_dist = []
    for n in ngb:
         dist=calcSimlaryCosDist(users_dic[userid],users_dic[n])  #calcSimlaryCosDist  calcCosDist calcCosDistSpe
         ngb_dist.append([dist,n])
    ngb_dist.sort(reverse=True)
    return ngb_dist
#
#
#   获取电影的列表
#
#
#
def getMoviesList(file_name):
    #print sys.getdefaultencoding()
    movies_contents=readFile(file_name)
    movies_info={}
    for movie in movies_contents:
        movie_info=movie.split("|")
        movies_info[int(movie_info[0])]=movie_info[1:]
    return movies_info


#
#   使用UserFC进行推荐
#   输入：文件名,用户ID,邻居数量
#   输出：推荐的电影ID,输入用户的电影列表,电影对应用户的反序表，邻居列表
#
def recommendByUserFC(file_name,userid,k=5):
    contents = readFile(file_name)
    #文件数据格式化成二维数组 List[[用户id,电影id,电影评分]...]
    rates = getRatingInformation(contents)
      #格式化成字典数据
    #    1.用户字典：dic[用户id]=[(电影id,电影评分)...]
    #    2.电影字典：dic[电影id]=[用户id1,用户id2...]
    test_dic,test_item_to_user=createUserRankDic(rates)
    #寻找邻居
    neighbors=calcNearestNeighbor(userid,test_dic,test_item_to_user)[:k]
    recommend_dict = {}
    for n in neighbors:
        n_uid = n[1]
        movies = test_dic[n_uid]
        for m in movies:
            if m[0] not in recommend_dict:
                recommend_dict[m[0]] = n[0]
            else:
                recommend_dict[m[0]] += n[0]
    recommend_list = []
    for k in recommend_dict:
        recommend_list.append(([recommend_dict[k]],k))
    recommend_list.sort(reverse=True)
    user_movies = [i[0] for i in test_dic[userid]]
    return [i[1] for i in recommend_list],user_movies,test_item_to_user,neighbors

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data_path = '/Users/zxh/Downloads/ml-100k/'
    data_movies = data_path+'u.item'
    data_user = data_path+'u.data'
    user_id = int(raw_input('please enter a user id!'))
    movies = getMoviesList(data_movies)
    recommend_list,user_movie,items_movie,neighbors=recommendByUserFC(data_user,user_id,80)
    neighbors_id = [i[1] for i in neighbors]
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t',  # text
                          't',  # float (decimal)
                          't']) # automatic
    table.set_cols_align(["l", "l", "l"])
    rows=[]
    rows.append([u"movie name",u"release", u"from userid"])
    for movie_id in recommend_list[:20]:
        from_user=[]
        for user_id in items_movie[movie_id]:
            if user_id in neighbors_id:
                from_user.append(user_id)
        rows.append([movies[movie_id][0],movies[movie_id][1],''])
    table.add_rows(rows)
    print table.draw()

