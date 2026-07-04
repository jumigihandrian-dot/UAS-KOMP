class DoWhileCompiler:

    def __init__(self, source_code):
        self.source_code = source_code
        self.label_counter = 1

    def new_label(self):
        lbl = f"L{self.label_counter}"
        self.label_counter += 1
        return lbl

    # =====================
    # Lexical Analysis
    # =====================
    def lexical_analysis(self):
        symbols = ['(', ')', '{', '}', ';']
        code = self.source_code

        for s in symbols:
            code = code.replace(s, f' {s} ')

        return code.split()

    # =====================
    # Syntax & Semantic Analysis
    # =====================
    def syntax_semantic_analysis(self, tokens):

        if "do" not in tokens or "while" not in tokens:
            raise SyntaxError("Struktur do-while tidak valid.")

        # kondisi IF
        first_open = tokens.index("(")
        first_close = tokens.index(")")
        if_condition = " ".join(tokens[first_open+1:first_close])

        # isi IF
        first_curly = tokens.index("{")
        first_end = tokens.index("}")
        if_body = " ".join(tokens[first_curly+1:first_end])

        # ELSE
        else_idx = tokens.index("else")

        else_open = tokens.index("{", else_idx)
        else_close = tokens.index("}", else_open)

        else_body = " ".join(tokens[else_open+1:else_close])

        # kondisi WHILE
        while_idx = tokens.index("while")
        while_open = tokens.index("(", while_idx)
        while_close = tokens.index(")", while_open)

        while_condition = " ".join(tokens[while_open+1:while_close])

        return if_condition, if_body, else_body, while_condition

    # =====================
    # Generate TAC
    # =====================
    def generate_tac(self):

        tokens = self.lexical_analysis()

        if_condition, if_body, else_body, while_condition = \
            self.syntax_semantic_analysis(tokens)

        start = self.new_label()
        else_lbl = self.new_label()
        end_if = self.new_label()

        tac = []

        tac.append(f"{start}:")
        tac.append(f"ifFalse {if_condition} goto {else_lbl}")
        tac.append(if_body)
        tac.append(f"goto {end_if}")
        tac.append(f"{else_lbl}:")
        tac.append(else_body)
        tac.append(f"{end_if}:")
        tac.append(f"if {while_condition} goto {start}")

        return "\n".join(tac)


# =====================
# Contoh Penggunaan
# =====================

source = """
do {
    if ( x > 5 ) {
        y = 1 ;
    } else {
        y = 0 ;
    }
} while ( x < 10 );
"""

compiler = DoWhileCompiler(source)

print("=== TOKENS ===")
print(compiler.lexical_analysis())

print("\n=== THREE ADDRESS CODE ===")
print(compiler.generate_tac())