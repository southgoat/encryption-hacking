# Encryption-hacking
A collection of encryption flaws that allows hackers to break into the system. 

## CBC-MAC with IV=0
Assuming the web app is set cookie as something like `administrator:cbc-mac(administrator,key)` and use `IV=0`.  
Then you can trick it to create a valid cookie for `administrator` by creating two users one for `administ` and another for `rator\00\00\00`, the `\00` is a padding. To know why this works have a look to the diagram below. ![](https://github.com/alshaboti/encryption-hacking/blob/main/resources/855px-CBC-MAC_structure_(en).svg.png) 


## CBC-MAC with IV controlled by user
One way is to set `IV=0` and use the prevous trick. 
Other way is to create user as `bdministrator` then change the first byte of `IV` (i.e. `IV[0]`) to keep the first byte of XOR operation as it is while having the fist byte in the message as `a` instead of `b`. See below why this works. ![](https://github.com/alshaboti/encryption-hacking/blob/main/resources/CBC-MAC-iv-controlled.png)
