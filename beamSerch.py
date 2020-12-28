import random
Words=     []
minimom=   []
dic=       []  
distWords= []
myK=       []
distBank=  []
myPath=    []
k=         3
myTopK=    [k]

#you define
inputBolean=False
start='house'
target='cuttle'




def firstK(start,target,myPath,k):
   '''
   Description:
   Pick the first 3 words 
   In distance 1 from start-word    
   
   '''
   Words=       options(start,myPath)
   distWords=   distOption(Words,target)
   myTopK=      pickThree(distWords,Words,k)
   myPath=      myPath+myTopK
   return       myTopK
    
def buildBank(myTopK):
    '''
    Description:
    will build a bank of words from the top picks
    '''
    BankS=set()                                                                #no duplicates
    for i in myTopK:
      BankS.update(options(i,myPath))
      
    Bank=list(BankS)                  
    return Bank
        
def main(start,target,myPath,k,inputBolean):
    
    m=                 10
    found=             False
    myTopK=            firstK(start,target,myPath,k)                           #first three words
    if target in myTopK:
      myPath.append    (myTopK)
      found=           True 
    
   
    while (m>0)and(found==False):
      Bank=                     buildBank(myTopK)
      if(inputBolean):
        print('words i consider are:',Bank)  
      if len(Bank)==0:break
      distBank=                 distOption(Bank,target)
      myTopK=                   pickThree(distBank,Bank,k)
      myPath.append             (m) 
      myPath=                   myPath+myTopK
      m=                        m-1  
      del                       Bank[:]
                                                                               #optional#print('the path so far is:',myPath)
      if target in myTopK:
        found=                  True
      
    if(found):
      print('my path is:', myPath)
    
    else:
      print('there is no path but this is what i have:',myPath)  
        
        
    


     
#%%
def options(source, myPath):
    '''
    Description:
    will build a bank of options by distance(0 or 1) from source word    
    '''
    del Words[:]
    leng=len(source)
    for i in range (0,len(dic)):  
       if(abs(leng- len(dic[i]))<2): 
         x=distance(source,dic[i])
         if ((x==1 or x==0) and (dic[i] not in myPath)):
           Words.append(dic[i] )
           
           
                                                                               #optinal#print ('words are:',Words)
  
    return Words 
 
    
#%%
def distOption(words, target):
   '''
   Description:
   Will tell the distance from the target-word for every word in words
   '''
   del distWords[:]
   for i in range (0,len(words)):
      x=distance(words[i],target)  
      distWords.append(x)
                                                                               #optional#print ('distance word:',distWords)
   return distWords




#%% distance
   

def distance(source, target): 
    '''
    Description:
    will initialize a 2d array with (-1)
    '''
    FlenS=len(source)+1
    FlenT=len (target)+1
            
    table=[[-1]*FlenT]*FlenS
    return distance1(table,source,target)

def distance1(table, source, target):
     """
     Description: req function
     Will tell the distance between two given words, 
     By the amount of changes needed to be done to transforam the first to the sec
     """
     if (len(source)== 0):  
        return len(target)
     if (len(target) == 0): 
        return len(source)
    
     if (table[len(source)][len(target)]) == -1:
       if (source[0] == target[0]): 
          table[len(source)][len(target)] = distance1(table,source[1:],target[1:])
       else:
          substitution = distance1(table,source[1:], target[1:])
          deletion     = distance1(table,source[1:], target)
          insertion    = distance1(table,source, target[1:])
          table[len(source)][len(target)] = 1 + min(min(substitution, deletion), insertion)
                 
     return table[len(source)][len(target)]
 

#%% 
def  pickThree(distWords,Words,k):
     '''
     Description: 
     Will collect all minimom elements 
     If there are a few equal minimom will randomize between them  
     '''
     del minimom[:]
     del myK[:]
    
     
     while (len(myK)<3):
       #this part will inizialize a min  
       minVal=      min(distWords)                                             # min distance
       minIndex=    distWords.index(minVal)                                    #index of minVAl
       minWord=     Words[minIndex]                                            #the word that match the minVal
       distWords.remove(minVal)                                                #delete it
       Words.remove(minWord)                                                   #delete it 
       minimom.append(minWord)                                                 #add it to minimom array
   
       #as long as there are more equal minimom collect them
       if len(distWords)>0 and (min(distWords))==minVal:
         while ((len(distWords)>0 and min(distWords))==minVal):
           minVal1=     min(distWords)
           minIndex1=   distWords.index(minVal1)
           minWord1=    Words[minIndex1]
           distWords.remove(minVal1)
           Words.remove(minWord1)
           minimom.append(minWord1)
           
       #this part will put the elements in my k picks      
   
       #if all  min  can enter in myK
       if len(minimom)<(k-(len(myK))):
         for i in range(len(minimom)):    
           r=random.randint(0,len(minimom)-1)
           myK.append(minimom[r])
           dic.remove(minimom[r])
           minimom.remove(minimom[r])
       else:  
         #meaning minimom is bigger then the space in myK
         for i in range(k-len(myK)):    
           r=random.randint(0,(len(minimom)-1))
           myK.append(minimom[r])
           dic.remove(minimom[r])
           minimom.remove(minimom[r])
         

    
     return myK
   
#%% dic and main


d='C:\\ai\\dclean.txt'#path
with open(d) as f:
  dic = f.readlines()
  for i in range (0,len(dic)):
    dic[i]=dic[i].strip()
    dic[i]= dic[i].lower()    
    
    
ans=main(start,target,myPath,k,inputBolean)

