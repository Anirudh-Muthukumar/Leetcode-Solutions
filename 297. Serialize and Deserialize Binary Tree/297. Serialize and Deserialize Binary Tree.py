# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        def encode(node):
            nonlocal data
            if node:
                data += str(node.val),
                encode(node.left)
                encode(node.right)
            else:
                data += "#",
        
        data = []
        encode(root)
        return ' '.join(data)
        

    def deserialize(self, data):
        
        def decode(vals):
            val = next(vals)
            if val=='#':
                return None
            node = TreeNode(int(val))
            node.left = decode(vals)
            node.right = decode(vals)
            return node
        
        vals = iter(data.split())
        return decode(vals)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))