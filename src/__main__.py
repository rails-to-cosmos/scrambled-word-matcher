from parser.automaton import Automaton

automaton = Automaton()

automaton.add_word('aapxj')
automaton.add_word('apaxj')
automaton.add_word('apaxd')
automaton.add_word('apal')
automaton.add_word('apalc')
automaton.add_word('pda')
automaton.add_word('bpde')
automaton.add_word('bp')
automaton.add_word('bzd')
automaton.add_word('b')

print(automaton.root.prettify())

automaton.scan('aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt')
