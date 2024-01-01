# DroppersForFun
Keeping a place for quick shellcode loaders and other droppers for quick AV evasion. 

In test_cpp I embed shellcode using a resource file outlined in this <a href="https://www.ired.team/offensive-security/code-injection-process-injection/loading-and-executing-shellcode-from-portable-executable-resources">article<a>. Besides that it's a standard VirtualAlloc with RWX to get shellcode into memory. Will probably store variants here that are more stealthy and maybe with more functionality. 
  
Also need to make some for reflective dll loading and shellcode loading dotnet assemblies as well. 

## Update 
dropper.py will take in a bin file & output a windows exe that will load and execute the shellcode in its current directory. Only works with the golang loader I stole from <a href="https://github.com/Ne0nd0g/go-shellcode/blob/master/cmd/CreateThreadNative/main.go">here<a> but will eventually expand to different techniques. Mostly for using in ctf's and htb type of challenges where I don't wanna write droppers from scratch everytime to evade standard AV. 