import sys

import lib.tools as tools
import lib.index as index

INDEX_METHODS = {
    1: 'forward',
    2: 'inverted'
}

ACTIONS = {
    1: 'index file',
    2: 'search',
    3: 'exit'
}

INDEX = {}

def get_index_method():
    message = 'please, choose indexing method:'
    options = INDEX_METHODS.values()
    result = tools.picker(message, options)
    return result

def get_next_action():
    message = 'please, choose next action:'
    options = ACTIONS.values()
    result = tools.picker(message, options)
    return result

def handle_action(action, index_method):
    if action == 1:
        handle_index_action(index_method=index_method)
    if action == 2:
        handle_search(index_method)
    if action == 3:
        tools.print_with_separator('exiting...')
        sys.exit(1)

def handle_index_action(index_method):
    message = 'please, enter a file for indexing'
    doc, text = tools.get_file(message)
    if index_method == 1:
        index.forward_index(text, doc, INDEX)
    else:
        index.inverted_index(text, doc, INDEX)

def handle_search(index_method):
    message = 'please, enter search query'
    tools.print_with_separator(message)
    query = input()
    result = {}
    if index_method == 1:
        result = index.forward_search(query, INDEX)
    else:
        result = index.inverted_search(query, INDEX)
    print(result)

def program_flow():
    index_method = get_index_method()
    while True:
        handle_action(get_next_action(), index_method=index_method)

def main():
    program_flow()

if __name__ == "__main__":
    main()