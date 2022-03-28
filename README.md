# Encryption-hacking
A collection of encryption flaws that allows hackers to break into the system. 

## CBC-MAC with IV=0
Assuming the web app is set cookie as something like `administrator:cbc-mac(administrator,key)`.  
Then you can trick it to create a valid cookie for `administrator` by creating two users one for `administ` and another for `rator\00\00\00`, the `\00` is a padding. To know why this works have a look to the diagram below. ![](https://github.com/alshaboti/encryption-hacking/blob/main/resources/855px-CBC-MAC_structure_(en).svg.png) 
