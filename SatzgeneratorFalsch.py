/* MIT License
 * Copyright (c) 2018 Christopher Fust
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

import itertools
import csv
import random

# Wortwiederholungsfehler, bei denen die Wortklasse wiederholt wird (major violations)
#D, M, N, v, v, N
#d, N, v, v, N
#D, M, N, v, v, M, N
#d, N, v, m, v, M, N
#d, N, v, m, m, M, N
#D, M, N, v, N, N
#D, M, N, v, m, N, N
#D, M, N, v, m, m, N
#D, M, N, v, N, M, N
#d, N, v, N, M, N
#Zuordnungsfehler von Artikel, Adektiv und Verb (agreement violations)
#D, M, N, v, d, M, N
#d, M, N, v
#d, M, N, v, d, N
#d, N, v, d, M, N
#D, M, N, v, D, N
#D, N, v, D, M, N
#D, N, v, m
#d, N, v, m, D, N
#Falsche Abfolge von Nominal- und Verbalphrase (phrase level violation)
#d, N, d, N, v
#d, N, d, N, v, m
#D, M, N, d, N, v
#D, M, N, d, N, v, m
#d, N, D, M, N, v
#d, N, D, M, N, v, m
#D, M, N, D, M, N, v
#D, M, N, D, M, N, v, m

x = 1 # Anzahl der zufällig ausgewählten Sätze
N = ['tok', 'plox', 'gum', 'trul']
v = ['prez', 'pel', 'glif', 'rix']
M = ['füne', 'böke']
m = ['rüfi', 'nöri']
d = ['aaf']
D = ['aak']
c = ['caf']
data01 = []
data02 = []
data03 = []
data04 = []
data05 = []
data06 = []
data07 = []
data08 = []
data09 = []
data10 = []
data11 = []
data12 = []
data13 = []
data14 = []
data15 = []
data16 = []
data17 = []
data18 = []
data19 = []
data20 = []
data21 = []
data22 = []
data23 = []
data24 = []
data25 = []
data26 = []

print ("Wortwiederholungsfehler")

prod = itertools.product(D, M, N, v, v, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data01.append (tmp)
    print (tmp)
    
prod = itertools.product(d, N, v, v, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data02.append (tmp)
    print (tmp)

prod = itertools.product(D, M, N, v, v, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data03.append (tmp)
    print (tmp)

prod = itertools.product(d, N, v, m, v, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data04.append (tmp)
    print (tmp)

prod = itertools.product(d, N, v, m, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data05.append (tmp)
    print (tmp)

prod = itertools.product(D, M, N, v, N, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data06.append (tmp)
    print (tmp)

prod = itertools.product(D, M, N, v, m, N, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data07.append (tmp)
    print (tmp)
    
prod = itertools.product(D, M, N, v, m, m, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data08.append (tmp)
    print (tmp)

prod = itertools.product(D, M, N, v, N, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data09.append (tmp)
    print (tmp)
    
prod = itertools.product(d, N, v, N, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data10.append (tmp)
    print (tmp)
    
print ("Zuordnungsfehler")
    
prod = itertools.product(D, M, N, v, d, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data11.append (tmp)
    print (tmp)

prod = itertools.product(d, M, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data12.append (tmp)
    print (tmp)
    
prod = itertools.product(d, M, N, v, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data13.append (tmp)
    print (tmp)
    
prod = itertools.product(d, N, v, d, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data14.append (tmp)
    print (tmp)
    
prod = itertools.product(D, M, N, v, D, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data15.append (tmp)
    print (tmp)
    
prod = itertools.product(D, N, v, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data16.append (tmp)
    print (tmp)

prod = itertools.product(D, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data17.append (tmp)
    print (tmp)
    
prod = itertools.product(d, N, v, m, D, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data18.append (tmp)
    print (tmp)   

print ("Falsche Abfolge von Nominal- und Verbalphrase")
    
prod = itertools.product(d, N, d, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data19.append (tmp)
    print (tmp) 
    
prod = itertools.product(d, N, d, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data20.append (tmp)
    print (tmp)   
    
prod = itertools.product(D, M, N, d, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data21.append (tmp)
    print (tmp)    
    
prod = itertools.product(D, M, N, d, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data22.append (tmp)
    print (tmp)   
    
prod = itertools.product(d, N, D, M, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data23.append (tmp)
    print (tmp)
    
prod = itertools.product(d, N, D, M, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data24.append (tmp)
    print (tmp)   

prod = itertools.product(D, M, N, D, M, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data25.append (tmp)
    print (tmp)

prod = itertools.product(D, M, N, D, M, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data26.append (tmp)
    print (tmp)
    
#for x in data:
#    print (x) 	
    
selec = random.sample (data01, x)
selec = selec + random.sample (data02, x)    
selec = selec + random.sample (data03, x)
selec = selec + random.sample (data04, x)
selec = selec + random.sample (data05, x)
selec = selec + random.sample (data06, x)
selec = selec + random.sample (data07, x)
selec = selec + random.sample (data08, x)
selec = selec + random.sample (data09, x)
selec = selec + random.sample (data10, x)
selec = selec + random.sample (data11, x)
selec = selec + random.sample (data12, x)
selec = selec + random.sample (data13, x)
selec = selec + random.sample (data14, x)
selec = selec + random.sample (data15, x)
selec = selec + random.sample (data16, x)
selec = selec + random.sample (data17, 2)
selec = selec + random.sample (data18, 2)
selec = selec + random.sample (data19, 2)
selec = selec + random.sample (data20, 2)
selec = selec + random.sample (data21, 2)
selec = selec + random.sample (data22, 2)
selec = selec + random.sample (data23, 2)
selec = selec + random.sample (data24, 2)
selec = selec + random.sample (data25, 2)
selec = selec + random.sample (data26, 2)

	
with open('data.csv', 'w') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for Satz in selec:
        datawriter.writerow([Satz])	


