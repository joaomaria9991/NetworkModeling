def remove_third_word(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                words = line.strip().split()
                if len(words) >= 3:
                    del words[2]
                output_file.write(' '.join(words) + '\n')

input_file_path = 'test1_digraph.txt'
output_file_path = 'test1_digraph_treated.txt'

remove_third_word(input_file_path, output_file_path)