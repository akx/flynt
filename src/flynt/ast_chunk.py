"""Uses py3.8 AST to define a chunk of code as an AST node."""

import ast

from flynt.format import QuoteTypes


class AstChunk:
    def __init__(self, node: ast.AST) -> None:
        self.node = node

    @property
    def start_line(self) -> int:
        return self.node.lineno - 1

    @property
    def start_idx(self) -> int:
        return self.node.col_offset

    @property
    def end_idx(self) -> int:
        return self.node.end_col_offset

    @property
    def end_line(self) -> int:
        return self.node.end_lineno - 1

    @property
    def n_lines(self) -> int:
        return 1 + self.end_line - self.start_line

    @property
    def string_in_string(self) -> bool:
        return False

    @property
    def quote_type(self) -> str:
        return QuoteTypes.double

    def __str__(self) -> str:
        from flynt.utils import ast_to_string

        src = ast_to_string(self.node)
        if src.startswith("(") and src.endswith(")"):
            src = src[1:-1]
        return src

    def __repr__(self) -> str:
        return f"AstChunk: {self}"
