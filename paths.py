# Paths with sum
"""You are given a binary tree in which each node contains an integer value (pos or neg)
. Design algorithm to count number of paths that sum to a given value. The path does not need to start or 
end at the root or a leaf. But must go downwards Parent to child"""




def path(node, val=19, path =[], set_paths, count):
    """returns number of all paths that sum upto given value"""


    # At node
    # check current node


    # if current node has no children
        # return count

        
    # if current node == val
        # add node to set_paths
        # count = count + 1



    # if sum(path) + current node == val
        # if path not in set_paths
            # add path to set paths
            # count = count + 1

    # if sum(path) + current node > val
        # failed path
        # empty path
        # path(cur, path, setpaths, count)

    # if sum(path) + current node < va,
        # go to next child

        #check left child
        #if the sum of current node and left child < val
            #add current to path
            # if sum of path == 19
                # if path not in set_paths
                    # add to set_paths
                    # count = count + 1
                    # empty path


            #path(leftchild, path, set_paths, count)


        #check right child
        # if the sum of current node and right child < val
            # add current to path
            # if sum of path == 19
                # if path not in set_paths
                    # add to set_paths
                    # count = count + 1
                    # empty path

            #path(leftchild, path, set_paths, count)
    