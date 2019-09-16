# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:07:04 2019

@author: tarun
"""
import matplotlib.pyplot as plt

def sketch_graph(player_name,l):
    for i in range(1,len(l)+1):
        if l[i-1]==-1:
            plt.bar(i,-1)
        else:
            plt.plot(i,l[i-1],'bs')
    plt.plot()        
    plt.ylabel('Runs')
    plt.xlabel('Matches')
    plt.title('Batting Stats of '+player_name)
    plt.grid(True)
    plt.show()

def mi():
    players={
             'rohit sharma':     [14,48,32,13,11],
             'quinton de kock':  [27,23,60,4,19,24],
             'suryakumar yadav': [2,38,11,59,7,21],
             'yuvraj singh':     [53,23,18,4],
             'kieron pollard':   [21,5,7,17,46,83],
             'hardik pandya':    [0,32,31,25,14,19],
             'krunal pandya':    [32,1,10,42,6,1],
             'ben cutting':      [3],
             'mcclenaghan':      [10,1,0],
             'rasikh salam':     [5],
             'jasprit bumrah':   [-1,0,-1,-1,-1,-1],
             'mayank markande':  [6,0],
             'lasith malinga':   [-1,-1,-1],
             'rahul chahar':     [-1,10,1],
             'jason behrendroff':[-1,-1,-1],
             'ishan kishan':     [17,7],
             'alzarri joseph':   [0,15],
             'siddhesh lad':     [15]   
            }
    
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of mi')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])
    
def rcb():
    players={
             'virat kohli':        [6,46,3,23,84,41],
             'parthiv patel':      [29,31,11,67,25,9],
             'moeen ali':          [9,13,2,18,0,32],
             'ab de villiers':     [9,70,1,13,63,17],
             'shimron hetmyer':    [0,5,9,1],
             'shivam dube':        [2,9,5],
             'colin de grandhomme':[4,2,37],
             'navdeep saini':      [2,-1,-1,-1,-1],
             'yuzvendra chahal':   [4,-1,1,-1,-1,1],
             'umesh yadav':        [1,-1,14,-1],
             'mohammed siraj':     [0,-1,3,-1,-1,1],
             'priyash barman':     [19],
             'marcus stoinis':     [31,28,15],
             'akshdeep nath':      [-1,-1,19],
             'pawan negi':         [-1,0],
             'tim southee':        [-1,9] 
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of rcb')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])
    
def dc():
    players={
             'prithvi shaw':        [7,24,99,0,11,28,14],
             'shikhar dhawan':      [43,51,16,30,12,0,97],
             'shreyas iyer':        [16,18,47,28,43,67,6],
             'colin ingram':        [47,2,10,38,5,22,14],
             'rishab pant':         [78,25,17,39,5,18,46],
             'keemo paul':          [3,0,-1],
             'axar patel':          [4,9,23,4,-1],
             'rahul tewatia':       [9,11,5,1,-1],
             'kagiso rabada':       [-1,-1,-1,0,3,-1,-1],
             'trent boult':         [-1],
             'ishant sharma':       [-1,-1,0,-1,-1],
             'amit mishra':         [-1,-1],
             'hanuam vihari':       [2,2],
             'chris morris':        [-1,0,17,0,-1],
             'sandeep lamichhane':  [-1,0,-1,-1] ,
             'avesh khan':          [4],
             'harshal patel':       [0,0]
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of dc')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])

def csk():
    players={
             'shane watson':        [0,44,13,5,26,17,0],
             'ambati rayudu':       [28,5,1,0,21,21,57],
             'suresh raina':        [19,30,36,16,17,14,4],
             'kedar jadhav':        [13,27,8,58,-1,8,1],
             'ravindra jadeja':     [6,-1,8,1,-1,-1,9],
             'ms dhoni':            [-1,32,75,12,37,-1,58],
             'dwayne bravo':        [-1,4,27,8],
             'deepak chahar':       [-1,-1,-1,7,-1,-1,-1],
             'shardul thakur':      [-1,-1,-1,12,-1],
             'harbhajan singh':     [-1,-1,-1,-1],
             'imran tahir':         [-1,-1,-1,-1,-1,-1,-1],
             'mitchell santner':    [-1,10],
             'mohit sharma':        [0],
             'faf du plessis':      [54,43,7],
             'scott kuggeleijn':    [-1,-1]
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of csk')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])
 
def rr():
    players={
             'ajinkya rahane':    [27,70,0,22,5,14],
             'jos buttler':       [69,5,6,59,37,23],
             'sanju samson':      [30,102,8,6],
             'steve smith':       [20,-1,28,38,73,15],
             'ben stokes':        [6,16,46,1,7,28],
             'rahul tripathi':    [1,-1,39,34,6,10],
             'krishnappa gowtham':[3,-1,9,-1,-1],
             'jofra archer':      [2,-1,24,-1,-1,13],
             'jaydev unadkat':    [1,-1,0,-1],
             'shreyas gopal':     [1,-1,0,-1,-1,19],
             'dhawal kulkarni':   [5,-1,-1,-1,-1,-1],
             'stuart binny':      [-1] ,
             'varun aaron':       [-1] ,
             'prashant chopra':   [-1] ,
             'sudhesan midhun':   [-1],
             'riyan parag':       [16]  
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of rr')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])   

def kxip():
    players={
             'kl rahul':           [4,1,71,15,55,71,100],
             'chris gayle':        [79,20,40,5,16,63],
             'mayank agarwal':     [22,58,43,6,0,55,],
             'safaraz khan':       [46,13,-1,39,67,-1,-1],
             'nicolas pooran':     [12],
             'mandeep singh':      [5,33,-1,29,1,2,7],
             'sam curran':         [-1,20,0,5,8],
             'ravichandran ashwin':[-1,-1,-1,3,-1,-1,-1],
             'mohammed shami':     [-1,-1,-1,0,-1,-1,-1],
             'mujeeb ur rahman':   [-1,0,-1],
             'ankit rajpoot':      [-1,-1,-1],
             'david miller':       [59,15,43,6,1,7],
             'varun chakravarthi': [-1],
             'hardus viljoen':     [-1,-1,1,-1],
             'andrew tye':         [-1,-1,-1],
             'murugan ashwin':     [-1,1,-1] ,
             'karun nair':         [5] 
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of kxip')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')    
    sketch_graph(player_name,players[player_name])
 
def srh():
    players={
             'david warner':       [85,69,100,10,15,70],
             'jonny bairstow':     [39,45,114,48,16,1],
             'vijay shankar':      [40,35,9,16,5,26],
             'yusuf pathan':       [1,16,6,9,0,-1],
             'manish pandey':      [8,1,-1,10,16,19],
             'deepak hooda':       [-1,-1,10,20,14],
             'shakib al hasan':    [-1],
             'rashid khan':        [-1,15,-1,-1,0,-1],
             'sandeep sharma':     [-1,-1,-1,-1,5,-1],
             'bhuvneshwar kumar':  [-1,-1,-1,-1,2,-1],
             'siddarth kaul':      [-1,-1,-1,-1,-1],
             'shahbaz nadeem':     [-1,0],
             'kane williamson':    [14],
             'mohammad nabi':      [-1,17,11,12] 
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of srh')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])  

def kkr():
    players={
             'chris lynn':          [7,10,20,43,50,0],
             'nitish rana':         [68,63,1,37,-1,0,11],
             'robin uthappa':       [35,67,13,33,26,11,28],
             'dinesh kartik':       [2,1,51,19,-1,19,2],
             'andre russell':       [49,48,66,48,-1,50,45],
             'shubhman gill':       [18,-1,3,6,9,65],
             'sunil narine':        [-1,24,4,10,47,6],
             'lockie ferguson':     [-1,-1,-1,-1,-1],
             'piyush chawla':       [-1,-1,12,-1,-1,8,14],
             'kuldeep yadav':       [-1,-1,10,-1,-1,0,2],
             'prasidh krishna':     [-1,-1,-1,-1,-1,0,-1],
             'nikhil naik':         [7], 
             'harry gurney':        [-1,1] ,
             'joe denly':           [0] ,
             'carlos brathwaite':   [6]
            }
    print('players are :--\n',"\n".join(list(dict.keys(players))))
    l=[]
    for i in players:
        s=0
        for j in players[i]:
            if j>0:
                s+=j
        l.append(s)
    plt.bar(list(dict.keys(players)),l)
    plt.xticks(list(dict.keys(players)),list(dict.keys(players)),rotation='vertical')
    plt.title('stats of kkr')
    plt.ylabel('total runs')
    plt.xlabel('player name')
    plt.grid(True)
    plt.show()
    player_name=input('Enter player name as it is as shown to find batting stats ')
    sketch_graph(player_name,players[player_name])

def ipl(team_name):
    if team_name=='mi':
        mi()
    elif team_name=='rcb':
        rcb()
    elif team_name=='dc':
        dc()
    elif team_name=='csk':
        csk()
    elif team_name=='rr':
        rr()
    elif team_name=='kxip':
        kxip()
    elif team_name=='srh':
        srh()
    else:
        kkr()
    
    

print('Team List---\nmi\nrcb\ndc\ncsk\nrr\nkxip\nsrh\nkkr')
team_name=input('Enter team of ipl ')
print()
ipl(team_name)
