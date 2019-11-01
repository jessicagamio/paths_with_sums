

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