#!/bin/python3
def findCluster(zlist):
    """This function creates the cluster from connected-zlist, removes duplicate records.
    input : [[1, 2], [1, 2, 3], [2, 3], [4]]
    output: [[4], [1, 2, 3]]
    """
    zombieTouched = []
    for i in range(1, len(zlist)+1):
        zCluster = []
        for alist in zlist:
            if i in alist:
                zCluster += alist
        zombieTouched.append(list(set(zCluster)))

    newlist = [list(tupl) for tupl in {tuple(item) for item in zombieTouched}]
    print("zombie clusters are:  ",newlist)
    print(len(newlist))


def zombieConnected(matrix):
    """This function will return a list connected zombies.
    input: [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    output: [[1, 2], [1, 2, 3], [2, 3], [4]]
    """
    zlist = []
    for row in matrix:
        j =0
        rowList = []
        for ele in row:
            j += 1
            val = ele *j
            if val !=0:
                rowList.append(val)
        zlist.append(rowList)
    print(zlist)
    findCluster(zlist)

if __name__ == '__main__':
    zombieConnected([[1,0,1],[0,1,0],[1,0,1]])
    zombieConnected([[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]])
    zombieConnected([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
