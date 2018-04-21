### Código para trocar as referências de template para as referências do DJANGO

import os
import codecs
from shutil import copyfile


def dir_change_alg (filename):

    new_text = []

    file = codecs.open(filename, 'r')
    f = file.readlines()
    #.decode('utf-16')

    #line = f.readline()
    #line = line.decode()

    new_line = ''

    for line in f:
        # verificar se há indicar de referência na linha
        new_line = ''
        if line.count("src") != 0 or line.count("href") != 0:
            print(line)
            count_position_word_on_line = 0
            for word in line:
                ## modelo geral de referência src = "algocoisa.css /.js /#"
                if word == "src" or word == "href" or count_position_word_on_line == 1 or count_position_word_on_line == 2:
                    count_position_word_on_line = count_position_word_on_line + 1
                elif count_position_word_on_line == 3:
                    if word.count(css) != 0:
                        word = word.replace('"','')
                        word = "'{% static 'css/" + word + " %}" 
                    if word.count(js) != 0:
                        word = word.replace('"','')
                        word = "'{% static 'js/" + word + " %}" 
                    #if word.count(html) != 0:
                        #word = word.replace('"','')
                        # <a href="{% url 'meuSite:index' %}">Home</a>
                        #word = "'{% url 'meuSite:" + word + " %}" 
            new_line = new_line+word
        new_text.append(new_line)    
    file.close()
    f = open('new_'+filename, 'w')
    f.writelines(new_text)
    f.close()

def main(directory):
    
    filenameList = os.listdir(directory)
    count = 0
    for filename in filenameList:

        if filename.count("html") != 0 and filename.count("new") == 0:
            
            # new_filename.html
            new_filename_html = 'text_'+filename
            copyfile(directory+'/'+filename,directory+'/'+new_filename_html)
            new_filename_txt = new_filename_html.replace('.html','.txt')

            # new_filename.txt
            os.rename(new_filename_html,new_filename_txt)
            print("Copia: "+str(count)+" - Nome: "+new_filename_txt)
            count = count + 1

    count = 0
    for filename in filenameList:

        if filename.count("text") == 1 and filename.count("new") == 0:
            print("Arquivo: "+str(count)+" - Nome: "+filename)
            dir_change_alg(filename)
            print("Arquivo: "+str(count)+" - Nome: "+filename+ " - CONVERTIDO")
            print("\n")
            count = count+1

    count = 0
    for filename in filenameList:

        if filename.count("text") == 1 and filename.count("new") == 1:
            print("Arquivo: "+str(count)+" - Nome: "+filename)
            new_filename_html = filename.replace('.txt','.html')
            os.rename(filename,new_filename_html)
            print("Arquivo: "+str(count)+" - Nome: "+new_filename_html+ " - CONVERTIDO")
            print("\n")
            count = count+1

        
directory = "/home/edivaldo/Documentos/ElaAdmin"
main(directory)