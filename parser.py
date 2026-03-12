def attempt_int(token):
    return int(token) if token.lstrip('-').isdigit() else token

def tokenize(text):
    raw_tokens = text.replace('[', ' [ ').replace(']', ' ] ').split()
    clean_tokens = filter(lambda t: not t.startswith('#'), raw_tokens)
    mapped_tokens = map(attempt_int, clean_tokens)
    return tuple(mapped_tokens)

def parse_expression(tokens):
    if not tokens:
        return None, ()
    
    first_token, remaining = tokens[0], tokens[1:]
    
    if first_token == '[':
        return parse_list(remaining, ())
    elif first_token == ']':
        return ']', remaining
    else:
        return first_token, remaining

def parse_list(tokens, acc):
    if not tokens:
        return acc, ()
    
    if tokens[0] == ']':
        return acc, tokens[1:]
        
    parsed_val, remaining_tokens = parse_expression(tokens)
    return parse_list(remaining_tokens, acc + (parsed_val,))

def parse_dsl(text):
    tokens = tokenize(text)
    ast, _ = parse_expression(tokens)
    return ast

if __name__ == "__main__":
    data_string = "[ user 101 [ role admin #internal_comment ] ]"
    pure_result = parse_dsl(data_string)
    print(pure_result)
