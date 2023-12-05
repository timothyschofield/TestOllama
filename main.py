"""
Test Ollama

03 Dec 2023

We have Llama2-7B running loaclly in Umbuntu
How to use the API?

https://github.com/jmorganca/ollama

https://www.llama-api.com/

In browser
localhost:11434
Ollama is running

REST API served automaticaly on localhost

Ollama has a REST API for running and managing models. For example, to generate text from a model:
NOTE: This is Ollama's API, NOT Llama's

Ollama API documentation
https://github.com/jmorganca/ollama/blob/main/docs/api.md

curl http://localhost:11434/api/generate -d '{
	"model": "llama2",
	"prompt": "Why is the sky blue?",
	"stream": false
}'

====== In Terminal ======
ollama list
NAME            ID              SIZE    MODIFIED     
llama2:latest   fe938a131f40    3.8 GB  20 hours ago

$ ollama run llama2 "Hello"
Hello! How can I help you today?

=============================================================
$ ollama help

Usage:
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   version for ollama

=============================================================
curl --help

Usage: curl [options...] <url>
 -d, --data <data>          HTTP POST data
 -f, --fail                 Fail silently (no output at all) on HTTP errors
 -h, --help <category>      Get help for commands
 -i, --include              Include protocol response headers in the output
 -o, --output <file>        Write to file instead of stdout
 -O, --remote-name          Write output to a file named as the remote file
 -s, --silent               Silent mode
 -T, --upload-file <file>   Transfer local FILE to destination
 -u, --user <user:password> Server user and password
 -A, --user-agent <name>    Send User-Agent <name> to server
 -v, --verbose              Make the operation more talkative
 -V, --version              Show version number and quit

=============================================================
  git config --global user.email "timothyschofield@hotmail.com"
  git config --global user.name "Tim Schofield"
============================================================= 
  
# -d means data
curl http://localhost:11434/api/generate -d '{"model": "llama2","prompt": "Why is the sky blue?","stream": false}'

"""
# pip install requests
import requests
from timutils import *
import json

payload = '{"model": "llama2","prompt": "What color is the sky?", "stream": false}'

return_from_oollama = requests.post("http://localhost:11434/api/generate", data=payload)

print("###########################")
print(return_from_oollama) # Was 400 bad request, now 200
print("###########################")
# its in bytes b'{"model":"llama2"... the b means bytes
print(return_from_oollama.content) 
print("###########################")
parsed = json.loads(return_from_oollama.content)
print(parsed)
print(type(parsed)) # A dictionary
print("###########################")
print(parsed['response'])
print("###########################")





