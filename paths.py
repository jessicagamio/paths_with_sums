# Paths with sum
"""You are given a binary tree in which each node contains an integer value (pos or neg)
. Design algorithm to count number of paths that sum to a given value. The path does not need to start or 
end at the root or a leaf. But must go downwards Parent to child"""




def path(node, val=19, path =[], set_paths):


    # At node
    # check current node

    # if current node == 19
        # add node to set_paths


    # if current < 19
        #check left child
        #if the sum of current node and left child < 19
            #add current to path
            # if sum of path == 19
                # if path not in set_paths
                # add to set_paths


            #path(leftchild, path, set_paths)


        #check right child
        # if the sum of current node and right child < 19
            # add current to path
            # if sum of path == 19
                # add to set_paths

            #path(leftchild, path, set_paths)
    
        # else 
        # return 0