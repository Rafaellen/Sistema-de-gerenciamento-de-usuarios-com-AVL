from typing import Optional, List
from src.user import User

class AVLNode:
    def __init__(self, user: User):
        self.user = user
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None
        self.size = 0
    
    def insert(self, user: User) -> None:
        self.root = self._insert(self.root, user)
        self.size += 1
    
    def _insert(self, node: Optional[AVLNode], user: User) -> AVLNode:
        if node is None:
            return AVLNode(user)
        
        if user.name < node.user.name:
            node.left = self._insert(node.left, user)
        else:
            node.right = self._insert(node.right, user)
        
        node.height = 1 + max(self._get_height(node.left), 
                            self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        # rotação
        if balance > 1 and user.name < node.left.user.name:
            return self._right_rotate(node)
        
        if balance < -1 and user.name > node.right.user.name:
            return self._left_rotate(node)
        
        if balance > 1 and user.name > node.left.user.name:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < -1 and user.name < node.right.user.name:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def delete(self, name: str) -> None:
        self.root = self._delete(self.root, name)
        if self.root:
            self.size -= 1
    
    def _delete(self, node: Optional[AVLNode], name: str) -> Optional[AVLNode]:
        if node is None:
            return node
        
        if name < node.user.name:
            node.left = self._delete(node.left, name)
        elif name > node.user.name:
            node.right = self._delete(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp = self._get_min_node(node.right)
            node.user = temp.user
            node.right = self._delete(node.right, temp.user.name)
        
        if node is None:
            return node
        
        node.height = 1 + max(self._get_height(node.left),
                             self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        # rebalanceamento
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def search(self, name: str) -> Optional[User]:
        node = self._search(self.root, name)
        return node.user if node else None
    
    def _search(self, node: Optional[AVLNode], name: str) -> Optional[AVLNode]:
        if node is None:
            return None
        
        if name == node.user.name:
            return node
        elif name < node.user.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)
    
    def in_order_traversal(self) -> List[User]:
        users = []
        self._in_order_traversal(self.root, users)
        return users
    
    def _in_order_traversal(self, node: Optional[AVLNode], users: List[User]) -> None:
        if node:
            self._in_order_traversal(node.left, users)
            users.append(node.user)
            self._in_order_traversal(node.right, users)
    
    def _get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def _get_balance(self, node: Optional[AVLNode]) -> int:
        return self._get_height(node.left) - self._get_height(node.right) if node else 0
    
    def _left_rotate(self, z: AVLNode) -> AVLNode:
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), 
                          self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                          self._get_height(y.right))
        
        return y
    
    def _right_rotate(self, z: AVLNode) -> AVLNode:
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), 
                          self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                          self._get_height(y.right))
        
        return y
    
    def _get_min_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def __len__(self) -> int:
        return self.size