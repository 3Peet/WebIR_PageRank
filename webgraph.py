import os
import codecs
import time

def link_parser(raw_html):
    urls = []
    pattern_start = '<a href="'
    pattern_end = '"'
    index = 0
    length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            link = raw_html[start:end]
            if len(link) > 0:
                if link not in urls:
                    urls.append(link)
            index = end
        else:
            break
    return urls

def norm_path_to_url(path, filename):
    return str(path)[35:]+'\\'+str(filename)

def write_urlmap_txt():
    for i in urlmap_array:
        cwd = os.getcwd()
        path_url = cwd + '/urlmap.txt'
        f = codecs.open(path_url, 'a', 'utf-8')
        f.write(norm_path_to_url(root, filename) + '\n')
    f.close()

def urlmap():
    global urlmap_array
    global urlmap_array_full_path
    for root, dirs, files in os.walk("C:\\Users\\mypee\\Desktop\\Web IR\\HTML"):
        for filename in files:
            urlmap_array.append(norm_path_to_url(root, filename))
            urlmap_array_full_path.append(str(root)+'\\'+str(filename))

def url_norm(current_url):
    if(current_url[-1:]=="/"):
        if(current_url[:5] == "https"): #HTTPS
            current_url = current_url[8:] +"index.html"
        else:                           #HTTP
            current_url = current_url[7:] +"index.html"
    elif(current_url[-5:]==".html"):
        if(current_url[:5] == "https"): #HTTPS
            current_url = current_url[8:]
        else:                           #HTTP
            current_url = current_url[7:]
    else:
        if(current_url[:5] == "https"):
            current_url = current_url[8:] +"/index.html"
        else:
            current_url = current_url[7:] +"/index.html"
    return current_url.replace('/','\\')
urlmap_array = []
urlmap_array_full_path = []


urlmap()
index_base = 0
index_link = 0
cwd = os.getcwd()
path_web_graph = cwd + '/webgraph.txt'
web_graph_file = codecs.open(path_web_graph, 'a', 'utf-8')

for path in urlmap_array_full_path:
    buffer = ''
    index_link+=1
    f = codecs.open(path, 'r', 'utf-8')
    link_web = link_parser(f.read())
    f.close()
    for url in link_web:
        fillter_pic = (".png" not in url) and (".jpg" not in url) and (".gif" not in url) and (".webp" not in url) and (".jpeg" not in url)
        fillter_url = ("ku.ac.th"in url) and (".pdf" not in url) and (".php" not in url) and (".doc" not in url) and ("?" not in url) and (":" not in url[7:]) and (".docx" not in url) and len(url) < 130
        if(fillter_pic and fillter_url):
            for base_url in urlmap_array:
                index_base +=1
                if(base_url == url_norm(url)):                  
                    buffer = buffer + str(index_base) + ','
            index_base = 0
    if(len(buffer)<1):
        buffer = '-'
        print(str(index_link)+" link to "+ buffer)
        web_graph_file.write(buffer+'\n')
        
    else:
        print(str(index_link)+" link to "+ buffer[:-1])
        web_graph_file.write(buffer[:-1]+'\n')

web_graph_file.close()


# webgraph()