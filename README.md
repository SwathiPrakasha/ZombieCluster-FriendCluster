# ZombieCluster-FriendCluster
You have a matrix, full of 1 and zeros.
Each {row,col} value represents the friendship status of two people/zombies.
If they know each other the value is 1, else zero.
A zombie(Friend) cluster is a group of zombies(friends) who are directly linked or 
indirectly through other zombies(friends).
Find how many clusters for the given input(matrix)
Ex1 :
[[1,0,0,0,0],
[0,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,0],
[0,0,0,0,1]]
output: 5 clusters

Ex2:
[[1,1,0,0],
[1,1,1,0],
[0,1,1,0],
[0,0,0,1]]
output: 2 clusters
"""
