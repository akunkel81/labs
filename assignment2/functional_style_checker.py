import ast
import os
import re

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w') as output_file:
        output_file.write(content)

def get_file_structure(tree: ast.Module, file_path: str) -> str:
    total_lines = sum(1 for _ in open(file_path))
    import_statements = [node.names[0].name for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    class_definitions = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    function_definitions = [node.name for node in ast.walk(tree)
                            if isinstance(node, ast.FunctionDef) and not isinstance(getattr(node, 'parent', None), ast.ClassDef)]

    structure = [
        f"Total lines of code: {total_lines}",
        f"Imports: {', '.join(import_statements) if import_statements else 'None'}",
        f"Classes: {', '.join(class_definitions) if class_definitions else 'None'}",
        f"Functions: {', '.join(function_definitions) if function_definitions else 'None'}"
    ]
    return "\n".join(structure)

def get_docstrings(tree: ast.Module) -> str:
    docstring_summaries = []
    for element in ast.walk(tree):
        if isinstance(element, (ast.FunctionDef, ast.ClassDef)):
            docstring_content = ast.get_docstring(element)
            if docstring_content:
                docstring_summaries.append(f"{element.name}: {docstring_content}")
            else:
                docstring_summaries.append(f"{element.name}: DocString not found.")
    return "\n".join(docstring_summaries)

def check_type_annotations(tree: ast.Module) -> str:
    unannotated_functions = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and
           not node.returns and
           not any(arg.annotation for arg in node.args.args)
    ]
    if unannotated_functions:
        return f"Functions without type annotations: {', '.join(unannotated_functions)}"
    return "All functions and methods use type annotations."

def check_naming_conventions(tree: ast.Module) -> str:
    camel_case_regex = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
    snake_case_regex = re.compile(r'^[a-z_][a-z0-9_]*$')

    invalid_class_names = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and not camel_case_regex.match(node.name)
    ]

    invalid_function_names = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and not snake_case_regex.match(node.name)
    ]

    messages = []
    if invalid_class_names:
        messages.append(f"Classes with incorrect naming conventions: {', '.join(invalid_class_names)}")
    else:
        messages.append("All class names adhere to the CamelCase naming convention.")

    if invalid_function_names:
        messages.append(f"Functions with incorrect naming conventions: {', '.join(invalid_function_names)}")
    else:
        messages.append("All function and method names adhere to the snake_case naming convention.")

    return "\n".join(messages)

def generate_report(file_path: str) -> str:
    source_code = read_file(file_path)
    parsed_tree = ast.parse(source_code)

    def set_parents(node, parent=None):
        for child in ast.iter_child_nodes(node):
            child.parent = parent
            set_parents(child, node)

    set_parents(parsed_tree)

    report_sections = [
        "File Structure",
        get_file_structure(parsed_tree, file_path),
        "\nDoc Strings",
        get_docstrings(parsed_tree),
        "\nType Annotation Check",
        check_type_annotations(parsed_tree),
        "\nNaming Convention Check",
        check_naming_conventions(parsed_tree)
    ]
    return "\n".join(report_sections)

def sanitize_file_path(raw_path: str) -> str:
    return raw_path.strip('"').strip("'")

def main() -> None:
    raw_file_path = input("Enter the path to the Python file: ").strip()
    file_path = sanitize_file_path(raw_file_path)

    if not file_path.endswith(".py") or not os.path.isfile(file_path):
        print("Invalid Python file path. Please try again.")
        return

    report_content = generate_report(file_path)

    report_file_name = f"style_report_{os.path.basename(file_path).replace('.py', '')}.txt"
    report_file_path = os.path.join(os.path.dirname(file_path), report_file_name)
    write_file(report_file_path, report_content)

    print(f"Report generated and saved to {report_file_path}")

if __name__ == "__main__":
    main()
