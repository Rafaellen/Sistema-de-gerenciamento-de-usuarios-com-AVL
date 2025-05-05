import uuid
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.avl_tree import AVLTree
from src.user import User
from src.utils import Color, export_users, import_users

class UserManager:
    def __init__(self):
        self.tree = AVLTree()
        self.load_initial_data()
    
    def load_initial_data(self):
        users = import_users()
        for user in users:
            self.tree.insert(user)
    
    def generate_id(self) -> str:
        return str(uuid.uuid4())[:8]
    
    def add_user(self):
        print(f"\n{Color.HEADER}=== Adicionar Novo Usuário ==={Color.END}")
        
        name = input(f"{Color.BLUE}Nome: {Color.END}").strip()
        if not name:
            print(f"{Color.FAIL}O nome não pode estar vazio!{Color.END}")
            return
        
        email = input(f"{Color.BLUE}E-mail: {Color.END}").strip()
        if not User.validate_email(email):
            print(f"{Color.FAIL}E-mail inválido!{Color.END}")
            return
        
        if self.tree.search(name):
            print(f"{Color.WARNING}Já existe um usuário com este nome!{Color.END}")
            return
        
        user_id = self.generate_id()
        new_user = User(name=name, user_id=user_id, email=email)
        self.tree.insert(new_user)
        
        print(f"\n{Color.GREEN}Usuário adicionado com sucesso!{Color.END}")
        print(f"ID: {user_id}")
    
    def remove_user(self):
        print(f"\n{Color.HEADER}=== Remover Usuário ==={Color.END}")
        
        if len(self.tree) == 0:
            print(f"{Color.WARNING}Não há usuários cadastrados!{Color.END}")
            return
        
        name = input(f"{Color.BLUE}Nome do usuário a remover: {Color.END}").strip()
        if self.tree.search(name):
            self.tree.delete(name)
            print(f"\n{Color.GREEN}Usuário '{name}' removido com sucesso!{Color.END}")
        else:
            print(f"\n{Color.FAIL}Usuário '{name}' não encontrado!{Color.END}")
    
    def search_user(self):
        print(f"\n{Color.HEADER}=== Buscar Usuário ==={Color.END}")
        
        if len(self.tree) == 0:
            print(f"{Color.WARNING}Não há usuários cadastrados!{Color.END}")
            return
        
        name = input(f"{Color.BLUE}Nome do usuário a buscar: {Color.END}").strip()
        user = self.tree.search(name)
        
        if user:
            print(f"\n{Color.GREEN}Usuário encontrado:{Color.END}")
            print(f"Nome: {user.name}")
            print(f"ID: {user.user_id}")
            print(f"E-mail: {user.email}")
        else:
            print(f"\n{Color.FAIL}Usuário '{name}' não encontrado!{Color.END}")
    
    def list_users(self):
        print(f"\n{Color.HEADER}=== Lista de Usuários ({len(self.tree)} no total) ==={Color.END}")
        
        if len(self.tree) == 0:
            print(f"{Color.WARNING}Não há usuários cadastrados!{Color.END}")
            return
        
        for i, user in enumerate(self.tree.in_order_traversal(), 1):
            print(f"\n{Color.CYAN}Usuário #{i}{Color.END}")
            print(f"Nome: {user.name}")
            print(f"ID: {user.user_id}")
            print(f"E-mail: {user.email}")
    
    def export_data(self):
        if export_users(self.tree.in_order_traversal()):
            print(f"\n{Color.GREEN}Dados exportados com sucesso!{Color.END}")
        else:
            print(f"\n{Color.FAIL}Falha ao exportar dados!{Color.END}")
    
    def show_menu(self):
        print(f"\n{Color.HEADER}{Color.BOLD}=== Sistema de Gerenciamento de Usuários ==={Color.END}")
        print(f"{Color.BLUE}1. Adicionar Usuário{Color.END}")
        print(f"{Color.BLUE}2. Remover Usuário{Color.END}")
        print(f"{Color.BLUE}3. Buscar Usuário{Color.END}")
        print(f"{Color.BLUE}4. Listar Usuários{Color.END}")
        print(f"{Color.BLUE}5. Exportar Dados{Color.END}")
        print(f"{Color.BLUE}0. Sair{Color.END}")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input(f"\n{Color.GREEN}Escolha uma opção: {Color.END}").strip()
            
            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.remove_user()
            elif choice == "3":
                self.search_user()
            elif choice == "4":
                self.list_users()
            elif choice == "5":
                self.export_data()
            elif choice == "0":
                print(f"\n{Color.HEADER}Saindo do sistema...{Color.END}")
                break
            else:
                print(f"\n{Color.FAIL}Opção inválida! Tente novamente.{Color.END}")
            
            input(f"\n{Color.CYAN}Pressione Enter para continuar...{Color.END}")

if __name__ == "__main__":
    manager = UserManager()
    manager.run()