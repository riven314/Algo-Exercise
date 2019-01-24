#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:07:03 2019

@author: hongyeah2151
"""
def riverSizes(matrix):
    # initialized required parameters
	sizes = []
	visited = [[False for value in row] for row in matrix] # may not uniform
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j] == True:
				continue
			TraverseNode(i, j, matrix, visited, sizes)
	return sizes

def TraverseNode(i, j, matrix, visited, sizes):
	traverse_nodes = [[i,j]]
	current_sizes = 0
	while len(traverse_nodes):
		current_node = traverse_nodes.pop()
		current_i = current_node[0]
		current_j = current_node[1]
		# if visited, skip else fill as visited
		if visited[current_i][current_j] == True:
			continue
		visited[current_i][current_j] = True
		# if not 1, skip else increment current_sizes 
		# and include its adj unvisited nodes
		if matrix[current_i][current_j] == 0:
			continue
		current_sizes += 1
		unvisited_nodes = GetUnvisitedNodes(current_i, current_j, matrix, visited)
		if unvisited_nodes != []:
			traverse_nodes = traverse_nodes + unvisited_nodes
	# update sizes if it's not 0
	if current_sizes > 0:
		sizes.append(current_sizes)

		
def GetUnvisitedNodes(current_i, current_j, matrix, visited):
	unvisited_nodes = []
	if (current_i > 0) and not visited[current_i-1][current_j]:
		unvisited_nodes.append([current_i-1, current_j])
	if (current_i < len(matrix) - 1) and not visited[current_i+1][current_j]:
		unvisited_nodes.append([current_i+1, current_j])
	if (current_j > 0) and not visited[current_i][current_j-1]:
		unvisited_nodes.append([current_i, current_j-1])
	if (current_j < len(matrix[current_i]) - 1) and not visited[current_i][current_j+1]:
		unvisited_nodes.append([current_i, current_j+1])
	return unvisited_nodes

mat = [[1,0,1,0], [1,0,0,1], [1,0,0,0]]
