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

#(d, N, v) 
#(d, N, v, m)
#(D, M, N, v)
#(d, N, v, d, N)
#(D, M, N, v, m)
#(d, N, v, m, d, N)
#(D, M, N, v, d, N)
#(d, N, v, D, M, N)
#(d, N, v, m, D, M, N)
#(D, M, N, v, m, d, N)
#(D, M, N, v, D, M, N)
#(D, M, N, v, D, M, N)
#(D, M, N, v, m, D, M, N)

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

prod = itertools.product(d, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data01.append (tmp)
    
prod = itertools.product(d, N, v, m)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data02.append (tmp)

prod = itertools.product(D, M, N, v)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data03.append (tmp)  

prod = itertools.product(d, N, v, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data04.append (tmp)

prod = itertools.product(d, N, v, m, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data05.append (tmp)

prod = itertools.product(D, M, N, v, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data06.append (tmp)

prod = itertools.product(d, N, v, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data07.append (tmp)

prod = itertools.product(d, N, v, m, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data08.append (tmp)

prod = itertools.product(D, M, N, v, m, d, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data09.append (tmp)

prod = itertools.product(D, M, N, v, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data10.append (tmp)
    
prod = itertools.product(D, M, N, v, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data11.append (tmp)

prod = itertools.product(D, M, N, v, m, D, M, N)
for p in prod:
    tmp = ''
    for a in p:
       tmp += a + ' '
    data12.append (tmp)		

#for x in data:
#    print (x) 	
    
selec = random.sample (data01, 6)
selec = selec + random.sample (data02, 6)    
selec = selec + random.sample (data03, 6)
selec = selec + random.sample (data04, 6)
selec = selec + random.sample (data05, 6)
selec = selec + random.sample (data06, 6)
selec = selec + random.sample (data07, 6)
selec = selec + random.sample (data08, 6)
selec = selec + random.sample (data09, 6)
selec = selec + random.sample (data10, 6)
selec = selec + random.sample (data11, 6)
selec = selec + random.sample (data12, 6)
	
with open('data.csv', 'w') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    for Satz in selec:
        datawriter.writerow([Satz])	


