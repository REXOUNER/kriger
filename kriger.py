# by rexouner  

# https://github.com/rexouner


from os import name, chdir
from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write


code = """# Protected with Scarecrow

# https://github.com/kriger/kriger


try:        
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess

    class scare:

        def fuck(names):
            for proc in process_iter():
                try:
                    for name in names:
                        if name.lower() in proc.name().lower():
                            proc.kill()
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass

        def crow():
            forbidden = ['http', 'traffic', 'wireshark', 'fiddler', 'packet']
            return scare.fuck(names=forbidden)
        
    scare.crow()
except:
    pass


# by rexouner
\n\n\n"""


if name == 'nt':
  path = '/'.join(__file__.split('\\')[:-1])
  chdir(path)




banner = """
                                                   ///                                  
                /                                +s+/                                   
                +o/                            /s/                                      
                 /oo/        /       +o        y                                        
                    oo/      s+       y       s/                                        
                      +o/     s/      s/     oo                                         
                        +o/   oo      s+    oo      .....   +o+                         
                          +o   y      s+    h      .. +shdNMMM+                         
           ...  .....      /+o//s     +o    h     . hNMMMMMMMy                          
         +sssyhhyy+ ...       h /y     h   +o    . mMMMMMMMMm                           
         oMMMMMMMMMMd+..      s+ +o    y   h     /mMMMMMMMMN              /             
          oNMMMMMMMMMMm/..     os+y    h  h     sMMMMMMMMMN .           +myo            
            hMMMMMMMMMMMd .      +yh/  y s+    dMMMMMMMMMh .           sMo              
            .+MMMMMMMMMMMMh .      so   oho++osyyyys++o/ .             hy               
             . smMMMMMMMMMMmo++o++oo         +o+++/          +      /osy                
              ..  /++syhhs+   oo                   +oo/    +s/      oh                  
                   ...    +++o/                       /++o+/         +d/                
yh/                     /s/                                           sy                
/oy              /+//////                                          /oss/                
  yo                                                             omys                   
  /mso/                                                           M/                    
   ++omo                                                          Nh/                   
     /yy                           /o      d           /++yssy/  /oNmo                  
       m+o/o                       oN+ . /oMd         +NNMMMMMNmdddNd+                  
       ymysds      ss//            sMNNhdNMMMo.. o   omMMMMMMMMMMMmo                    
        moDMdd    ohNMMMdy/       .oNMMMMMMMMMMsomMddNMMMMMMMMMMMmo                      
          /NN/+dMMMMMMMMMMmhsyooyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo                        
           dMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm/                         
             +shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                          
                omNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy                           
                   NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/                           
                   mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                            
                   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm                            
                   /MMMMMmdhmMmMMMMMMMMMMMMMMMMMNMdMh/oyhNMN                            
                    MMNh+  . y oNMMMMMMMMMMMMms//+ /      od                            
                   +ds/         sNNMMMMMMMMMy                                           
                                 //sNMMMMMNo                                            
                                    /dMMMMs                                             
                                      sMMN                                              
                                       hMs                                              
                                        m"""[1:]

ascii = '''
   ▄█   ▄█▄    ▄████████  ▄█     ▄██████▄     ▄████████    ▄████████ 
  ███ ▄███▀   ███    ███ ███    ███    ███   ███    ███   ███    ███ 
  ███▐██▀     ███    ███ ███▌   ███    █▀    ███    █▀    ███    ███ 
 ▄█████▀     ▄███▄▄▄▄██▀ ███▌  ▄███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀█████▄    ▀▀███▀▀▀▀▀   ███▌ ▀▀███ ████▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███▐██▄   ▀███████████ ███    ███    ███   ███    █▄  ▀███████████ 
  ███ ▀███▄   ███    ███ ███    ███    ███   ███    ███   ███    ███ 
  ███   ▀█▀   ███    ███ █▀     ████████▀    ██████████   ███    ███ 
  ▀           ███    ███                                  ███    ██  ''' [1:]


def init():
  System.Title("Scarecrow")
  System.Size(180, 50)
  Anime.Fade(text=Center.Center(banner), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)


def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(ascii)))
  print("\n"*5)

  file = Write.Input("Drag a Python file -> ", Colors.red_to_yellow, interval=0.005)
  print()

  if not isfile(file):
      print(Colorate.Error("Error! This file does not exist!"))
      return

  with open(file, mode='r', encoding='utf-8') as f:
      content = f.read()

  content = code + content

  with open("krigered.py", mode='w', encoding='utf-8') as f:
      f.write(content)

  Write.Input("Done!", Colors.red_to_yellow, interval=0.005)
  return exit()


if __name__ == '__main__':
  init()
  while True:
    main()
