with open('test1.txt') as f:
    print(f.readline())
    print(f.readline())
    print(type(f))
print("End of code")
with open('test1.txt','a') as ff:
    ff.write('This appears at the end of the text')
with open('test1.txt','r') as fff:
    fffr = fff.read()
    print(fffr)

import json
person_dict = {
    "name":"Muhammed",
    "country":"Canada",
    "city":"ottawa",
    "skills":["JavaScript","React","Python"]
}
person_json = json.dumps(person_dict, indent=2)
print(type(person_json))
print(person_json)

person = json.loads(person_json)
print(type(person))
print(person)

with open('test_json.json','w',encoding='utf-8') as p:
    json.dump(person_json,p,ensure_ascii=False,indent=4)
with open('test_json.json','r') as l:
    json_read = l.read()
    print(json_read)
with open('test1.txt','r') as test1:
    line_count = 0
    word_count = 0
    for line in test1:
        line_count += 1
        words = line.split()
        word_count += len(words)
print(f"Number of lines:{line_count}")
print(f"Number of words: {word_count}")

def count_no_of_lines_and_words(filename):
    with open(filename, 'r') as test1:
        line_count = 0
        word_count = 0
        for line in test1:
            line_count += 1
            words = line.split()
            word_count += len(words)
    number_of_lines = (f"Number of lines:{line_count}")
    number_of_words = (f"Number of words: {word_count}")
    return number_of_lines, number_of_words

results = count_no_of_lines_and_words('test2.txt')
print(results)
donald_result = count_no_of_lines_and_words("C:\\Users\\hp\\Desktop\\folder\\donald_speech.txt")
print(donald_result)
melina_result = count_no_of_lines_and_words("C:\\Users\\hp\\Desktop\\folder\\melina_trump_speech.txt")
print(melina_result)
michelle_result = count_no_of_lines_and_words("C:\\Users\\hp\\Desktop\\folder\\michelle_obama_speech.txt")
print(michelle_result)
obama_result = count_no_of_lines_and_words("C:\\Users\\hp\\Desktop\\folder\\obama_speech.txt")
print(obama_result)

import re
def extract_emails(text):
    return re.findall(r'[\w\.-]+@[\w\.-]+',text)

def open_file(file):
    with open(file,'r') as emails:
        file_contents = emails.read()
    return file_contents
contents = open_file("C:\\Users\\hp\\Desktop\\folder\\email_exchanges.txt")
all_emails = extract_emails(contents)
incoming_emails = [email for email in all_emails if email.split('@')[1] not in ['postmaster@collab.sakaiproject.org',
                   'source@collab.sakaiproject.org']]
print(incoming_emails)
