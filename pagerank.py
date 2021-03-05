import numpy as np
import codecs
import os
import time
# Init State


cwd = os.getcwd()
path_web_graph = cwd + '/webgraph.txt'
webgraph_file = open(path_web_graph, "r")
web_link_array = webgraph_file.read().splitlines()
webgraph_file.close()

score = []
numlink = []
list_score = []
alpha = 0.85

n = len(web_link_array)
for i in range(n+1):
    score.append(1/n)


def socre_web(link_score,current_score):
    return (alpha*link_score*current_score)+((1-alpha)*(1/n))
    

print("------------- STR LOOP -------------")
total_round = 10000
for i in range(total_round):
    host_no = 0
    for host in web_link_array:
        if(host=="-"):
            pass
        else:
            # print("Now process HOST: " + str(host_no))
            des = host.split(',')
            for des_no in des:
                
                try:
                    score[int(des_no)] = socre_web(score[int(host_no)],score[int(des_no)])
                except Exception as e:
                    print(e)
                    print('Error HOST: ' + str(host_no) + ' DEST: ' +str(des_no))
                    time.sleep(1)

        host_no+=1
print("------------- END LOOP -------------")


cwd = os.getcwd()
path_page_scores = cwd + '/page_socres.txt'
page_scores_file = codecs.open(path_page_scores, 'a', 'utf-8')

total_score = 0
for i in score:
    total_score += i
    page_scores_file.write(str(i)+'\n')
page_scores_file.close()

print(total_score)

