
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res