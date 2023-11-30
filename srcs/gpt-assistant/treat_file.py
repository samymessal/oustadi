import sys

def process_file(file_path):
    chapters = {}
    current_chapter = 0
    current_subchapter = 0
    partial_word = ""

    with open(file_path, 'r') as file:
        for line in file:
            # Remove newline characters and append any partial word from previous line
            line = partial_word + line.rstrip('\n')
            partial_word = ""

            # Check for new chapter or subchapter
            if line.startswith('## '):
                current_chapter += 1
                current_subchapter = 0
                chapters[str(current_chapter)] = {'content': '', 'subchapters': {}}
            elif line.startswith('### ') and current_chapter > 0:
                current_subchapter += 1
                chapters[str(current_chapter)]['subchapters'][f"{current_chapter}.{current_subchapter}"] = ''

            # Handle line ending with a hyphen
            if line.endswith('-'):
                partial_word = line[:-1]
                continue

            # Add content to current chapter or subchapter
            if current_subchapter > 0:  # Add to subchapter
                chapters[str(current_chapter)]['subchapters'][f"{current_chapter}.{current_subchapter}"] += line.strip().replace("```", "") + ' '
            elif current_chapter > 0:  # Add to chapter
                chapters[str(current_chapter)]['content'] += line.strip().replace("```", "") + ' '

    return chapters

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a file path.")
    else:
        chapters = process_file(sys.argv[1])
        print(chapters['5'])
