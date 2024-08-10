class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def helper( node: 'Node'):
            
            if not node:
                return None
            
            scanner = node.next

            # Scanner finds left-most neighbor, on same level, in right hand side
            while scanner:

                if scanner.left:
                    scanner = scanner.left
                    break

                if scanner.right:
                    scanner = scanner.right
                    break

                scanner = scanner.next


            # connect right child if right child exists
            if node.right:
                node.right.next = scanner 

            # connect left child if left child exists
            if node.left:
                node.left.next = node.right if node.right else scanner


            helper( node.right )  
            helper( node.left )  
                
            return node
        
        return helper( root ) 