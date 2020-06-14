x=["a","b", "c","d", "e","f","g","h","i","j","k","l","m","n","ñ", "o","p","q","r","s","t","u","v","w","x","y","z"]
def encriptar(s,n):
    y=len(s)
    '''
    la función encripta palabras
    
    parametros:
    la palabra (s)
    el valor de encriptación (n)

    retorna la encriptación de la palabra dependiendo del valor (n)
    '''
    return enc_aux(s,n,x,y-1)
def enc_aux(s,n,x,y):
    if y==0:
        return x[x.index(s)+n]
    else:
        return enc_aux2(s,n,x,y-1)
def enc_aux2(s,n,x,y):
    if y>-1:
        return (s.replace(s[0],x[(x.index(s[0])+n)]))#encriptar(s,n,contador+1,
  
def contador(n):
    if n==0:
        return encriptar(s,n)
    else:
        return encriptar(s,n)-1         
s="hola"
print (encriptar(s,2))        
        
        
def desencriptar(a,n):
    y=len(a)
    '''
    La función desencripta

    Parametros:
    la palabra encriptada(a)
    el valor de desencriptación(n)

    retorna la palabra desencriptada en relacion al valor (n) de desencriptación
    '''
    return desenc_aux(a,n,x,y-1)
def desenc_aux(a,n,x,y):
    if y==0:
        return x[x.index(a)-n]
    else:
        return desenc_aux2(a,n,x,y-1)
def desenc_aux(a,n,x,y):
    if y>-1:
        return 
a="h"
#print (desencriptar(a,2))      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        #(s.replace(s[-1],x[(x.index(s[-1])+n)]))#enc_aux3((f'{list(s.strip())}')) #, (s.replace(s[0],x[(x.index(s[0])+2)])) , (s.replace(s[-1],x[(x.index(s[-1])+2)]))
#def enc_aux3(s):
 #   return (s.replace(s[0],x[(x.index(s[1])+n)]))
        
        
    
        #return (s.replace(s[y],x[n]),n+2+n+2+x.index(s[y]),x,y-1)





    
