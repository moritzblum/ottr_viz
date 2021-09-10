import argparse
from antlr4 import *
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

from ottr_parser.stOTTRLexer import stOTTRLexer
from ottr_parser.stOTTRListener import stOTTRListener
from ottr_parser.stOTTRParser import stOTTRParser


def get_text(context):
    return context.symbol.text


class OTTRPrinter(stOTTRListener):
    def __init__(self, template_tree):
        self.iri = None
        self.template_name = None

        self.used_templates = []
        self.template_tree = template_tree

    # Exit a parse tree produced by stOTTRParser#templateName.
    def exitTemplateName(self, ctx: stOTTRParser.TemplateNameContext):
        self.template_name = self.iri
        self.used_templates.append(self.template_name)
        self.iri = None

    # Exit a parse tree produced by stOTTRParser#template.
    def exitTemplate(self, ctx: stOTTRParser.TemplateContext):
        self.template_tree.extend([[self.used_templates[0], used_template] for used_template in self.used_templates[1:]])
        self.used_templates = []

    # Enter a parse tree produced by stOTTRParser#iri.
    def enterIri(self, ctx: stOTTRParser.IriContext):
        if ctx.prefixedName():
            self.iri = ctx.prefixedName().start.text
        else:
            self.iri = get_text(ctx.IRIREF())

    # Exit a parse tree produced by stOTTRParser#stOTTRDoc.
    def exitStOTTRDoc(self, ctx: stOTTRParser.StOTTRDocContext):
        print('exit parser')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot OTTR template library dependencies.')
    parser.add_argument('-format', '--format', default='png',
                        help='output file format, e.g. png, pdf (all types supported by graphviz)')
    parser.add_argument('input_file', help='OTTR template library file.')

    args = parser.parse_args()
    template_library_file = args.input_file

    # parse OTTR template library and collect graph edges
    input_stream = FileStream(template_library_file, encoding="utf-8")
    lexer = stOTTRLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = stOTTRParser(stream)
    tree = parser.stOTTRDoc()
    template_tree = []
    printer = OTTRPrinter(template_tree)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    # build networkx graph
    G = nx.DiGraph()
    G.add_edges_from(template_tree)
    print('is_directed_acyclic_graph:', nx.is_directed_acyclic_graph(G))

    # plot with graphviz
    A = to_agraph(G)

    # dot layout
    A.layout('dot')
    A.draw(template_library_file[:-7] + '_viz.' + args.format)

    print('done.')
