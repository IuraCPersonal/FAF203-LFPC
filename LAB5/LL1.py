# TODO: Normalize the input grammar
#        1. Left Factoring
#        2. Left Recursion

import copy


class LL1:
    def __init__(self, grammar, terminals, non_terminals, start, empty) -> None:
        self.grammar = grammar
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.start = start
        self.empty = empty

    def check_if_ll1(self):
        invalid = []
        for symbol, transition in self.grammar.items():
            for production in transition:
                if production[0] == symbol:
                    invalid.append([symbol, production])
        return invalid

    def FIRST(self, symbol, p_dict, terminals, non_terminals, empty):
        symbol = symbol[0]
        if symbol in terminals:
            return [symbol]

        first_set = []
        for s in p_dict[symbol]:
            if s == empty:
                if len(symbol) > 1:
                    first_set += self.FIRST(symbol[1:], p_dict,
                                            terminals, non_terminals, empty)
                else:
                    first_set += [empty]
            else:
                sub_first_set = self.FIRST(
                    s, p_dict, terminals, non_terminals, empty)
                first_set += sub_first_set
        return first_set

    def FOLLOW(self, symbol, p_dict, terminals, non_terminals, empty, gen_follow):
        if len(symbol) != 1:
            return {}

        for key in p_dict.keys():
            for value in p_dict[key]:
                if symbol in value:
                    index = value.index(symbol)
                    if index == (len(value) - 1):
                        if key != symbol:
                            if key in gen_follow:
                                temp = gen_follow[key]
                            else:
                                gen_follow = self.FOLLOW(
                                    key, p_dict, terminals, non_terminals, empty, gen_follow)
                                temp = gen_follow[key]
                            gen_follow[symbol] += temp
                    else:
                        first_of_next = self.FIRST(
                            value[index + 1:], p_dict, terminals, non_terminals, empty)
                        if empty in first_of_next:
                            if key != symbol:
                                if key in gen_follow:
                                    temp = gen_follow[key]
                                else:
                                    gen_follow = self.FOLLOW(
                                        key, p_dict, terminals, non_terminals, empty, gen_follow)
                                    temp = gen_follow[key]
                                gen_follow[symbol] += temp
                                gen_follow[symbol] += first_of_next + \
                                    [empty]
                        else:
                            gen_follow[symbol] += first_of_next
                    gen_follow[symbol] = list(set(gen_follow[symbol]))
        return gen_follow

    def generate_table(self, p_dict, first_dict, next_dict, empty):
        table = {}
        for key in p_dict.keys():
            for value in p_dict[key]:
                if value != empty:
                    for element in first_dict[value[0]]:
                        table[key, element] = value
                else:
                    for element in next_dict[key]:
                        table[key, element] = value
        return table

    def parse_grammar(self, ll1_table, start, empty, input_program):
        end_symbol = "$"
        user_input = input_program + end_symbol
        stack = [end_symbol, start]

        index = 0
        parsed = []

        while len(stack) > 0:
            top = stack[-1]
            temp_stub = [copy.copy(stack), copy.copy(user_input[index:]), None]
            current_input = user_input[index]

            if top == current_input:
                stack.pop()
                index = index + 1
            else:
                key = top, current_input
                if key not in ll1_table:
                    return None

                value = ll1_table[key]
                temp_stub[2] = str(key[0]) + " -> " + str(value)
                if value != empty:
                    value = value[::-1]
                    value = list(value)
                    stack.pop()
                    for element in value:
                        stack.append(element)
                else:
                    stack.pop()
            parsed.append(temp_stub)

        return parsed

    def show_parse_steps(self, parsed, language):
        if parsed is None:
            print("Parse language '" + language + "', not accepted.")
        else:
            print("Parse language '" + language + "', accepted:")
            columns = ["Stack", "Input", "Production"]
            rows = []
            columns_width = [len(x) for x in columns]
            for ind in range(0, len(parsed)):
                rows.append([str(parsed[ind][0]), str(
                    parsed[ind][1]), str(parsed[ind][2])])
                columns_width = [max(columns_width[tmp_ind], len(
                    rows[-1][tmp_ind])) for tmp_ind in range(0, len(columns_width))]
            titles = []
            for ind in range(0, len(columns)):
                padding = " "*(columns_width[ind]-len(columns[ind]))
                titles.append(columns[ind] + padding)
            print(' '.join(titles))
            for row in rows:
                row_str = []
                for ind in range(0, len(columns)):
                    padding = " "*(columns_width[ind]-len(row[ind]))
                    row_str.append(row[ind] + padding)
                print(' '.join(row_str))

    def main(self, language):
        invalid_result = self.check_if_ll1()
        if len(invalid_result) > 0:
            print("Grammar Error: The current grammar is not LL(1): " +
                  str(invalid_result))
            return

        first_dict = {}
        for left_symbol in self.grammar.keys():
            first_dict[left_symbol] = list(
                set(self.FIRST(left_symbol, self.grammar, self.terminals, self.non_terminals, self.empty)))
        for left_symbol in self.terminals:
            first_dict[left_symbol] = list(
                set(self.FIRST(left_symbol, self.grammar, self.terminals, self.non_terminals, self.empty)))

        # print("First Dict: " + str(first_dict))

        next_dict = {}
        next_dict[self.start] = ['$']

        for left_symbol in self.grammar.keys():
            next_dict[left_symbol] = []
        for left_symbol in self.grammar.keys():
            next_dict = self.FOLLOW(
                left_symbol, self.grammar, self.terminals, self.non_terminals, self.empty, next_dict)

        next_dict[self.start] = ['$']

        # print("Next Dict: " + str(next_dict))

        ll_1_table = self.generate_table(
            self.grammar, first_dict, next_dict, self.empty)

        print("LL(1) Table")
        for key in ll_1_table:
            print(key, ll_1_table[key])

        parse_hist = self.parse_grammar(
            ll_1_table, self.start, self.empty, language)
        self.show_parse_steps(parse_hist, language)
