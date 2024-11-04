import ast
import re
import os
import shutil
from typing import List

class PythonStyleChecker:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path).replace(".txt", "")
        self.report = []

    def generate_report(self) -> None:
        with open(self.file_path, 'r') as file:
            file_content = file.read()

        tree = ast.parse(file_content)
        
        self.set_parents(tree)
        
        self.check_file_structure(tree)
        self.check_docstrings(tree)
        self.check_type_annotations(tree)
        self.check_naming_conventions(tree)
        
        self.write_report()

    def set_parents(self, node, parent=None):
        for child in ast.iter_child_nodes(node):
            child.parent = parent
            self.set_parents(child, node)

    def check_file_structure(self, tree: ast.Module) -> None:
        num_lines = sum(1 for _ in open(self.file_path))
        imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and not isinstance(getattr(node, 'parent', None), ast.ClassDef)]
        
        self.report.append(f"File structure:\nTotal lines of code: {num_lines}")
        self.report.append(f"Imports: {', '.join(imports) if imports else 'None'}")
        self.report.append(f"Classes: {', '.join(classes) if classes else 'None'}")
        self.report.append(f"Functions: {', '.join(functions) if functions else 'None'}\n")

    def check_docstrings(self, tree: ast.Module) -> None:
        self.report.append("Doc Strings:")
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if docstring:
                    self.report.append(f"{node.name}: {docstring}")
                else:
                    self.report.append(f"{node.name}: DocString not found.")
        self.report.append("\n")

    def check_type_annotations(self, tree: ast.Module) -> None:
        functions_without_annotations = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and not node.returns and not any(arg.annotation for arg in node.args.args)
        ]
        
        if functions_without_annotations:
            self.report.append("Type Annotation Check:\nFunctions without type annotations:")
            self.report.extend(functions_without_annotations)
        else:
            self.report.append("Type Annotation Check:\nAll functions and methods use type annotations.")
        self.report.append("\n")

    def check_naming_conventions(self, tree: ast.Module) -> None:
        camel_case_pattern = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
        snake_case_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')

        classes_with_wrong_naming = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef) and not camel_case_pattern.match(node.name)
        ]

        functions_with_wrong_naming = [
            node.name for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and not snake_case_pattern.match(node.name)
        ]

        if classes_with_wrong_naming:
            self.report.append("Classes with incorrect naming conventions:")
            self.report.extend(classes_with_wrong_naming)
        else:
            self.report.append("All class names adhere to the CamelCase naming convention.")

        if functions_with_wrong_naming:
            self.report.append("Functions with incorrect naming conventions:")
            self.report.extend(functions_with_wrong_naming)
        else:
            self.report.append("All function and method names adhere to the snake_case naming convention.")
        self.report.append("\n")

    def write_report(self) -> None:
        report_dir = os.path.dirname(self.file_path)
        report_path = os.path.join(report_dir, f"style_report_{self.file_name}.txt")
        with open(report_path, 'w') as report_file:
            report_file.write("\n".join(self.report))
        print(f"Report written to {report_path}")


class PythonFileConverter:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path).replace(".py", "")
        self.txt_file_path = os.path.join(os.path.dirname(file_path), f"{self.file_name}.txt")
        self.style_checker = PythonStyleChecker(self.txt_file_path)

    def convert_to_txt(self) -> None:
        with open(self.file_path, "r") as py_file:
            content = py_file.read()
        with open(self.txt_file_path, "w") as txt_file:
            txt_file.write(content)
        print(f"Converted {self.file_path} to {self.txt_file_path}")

    def run_style_checker(self) -> None:
        self.style_checker.generate_report()

    def convert_back_to_py(self) -> None:
        restored_file_path = os.path.join(os.path.dirname(self.file_path), f"{self.file_name}_restored.py")
        shutil.copy(self.txt_file_path, restored_file_path)
        print(f"Converted {self.txt_file_path} back to {restored_file_path}")

    def execute(self) -> None:
        self.convert_to_txt()
        self.run_style_checker()
        self.convert_back_to_py()

# Sample usage
if __name__ == "__main__":
    '''This is my sample file I used, replace with wanted file for checker and use double backlashes'''
    file_path = "C:\\Users\\kunke\\Downloads\\bad_naming.py"  # Replace with your actual Python file path and include DOUBLE BACKSLASH FOR PATH
    converter = PythonFileConverter(file_path)
    converter.execute()
