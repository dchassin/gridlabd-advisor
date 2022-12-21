"""HiPAS GridLAB-D advisor

Syntax:

  gridlabd advisor [OPTIONS ...] [QUERY ...]

Options:

  --help|-h|help            display this documentation
  --signup                  signup for an API key (opens browser)
  --apikey=<str>            set the API key
  --responses|-N=<int>      request multiple responses (default 1)
  --echo|-E[=<bool>]        echo the query in the response (default False)
  --temperature|-T=<float>  set the riskiness of responses (default 0.1)
  --force[=<bool>]          force responses to queries not related to 
                            GridLAB-D
  --length|-L=<int>         set the number of token allowed in the response 
                            (default 1024)
  --model|-M=<str>          set the bot name (default is "text-davinci-003")
  --quiet|-q[=<bool>]       disable error message output
  --warning|-w[=<bool>]     disable warning message output
  --silent[=<bool>]         disable warning and error message output
  --debug[=<bool>]          enable traceback on exceptions

Description:

  The advisor generates responses using OpenAI completion API.  Responses
  can be expected to vary unless a 0 temperature is used. 

Environment:

  OPENAI_APIKEY       set the OpenAI API key
  OPENAI_APIKEY_FILE  set the OpenAI API key file
"""
import os, sys
import json
import openai
import textwrap

class OpenaiHelperException(Exception):
  pass

def get_apikey():
  openai.api_key = os.getenv('OPENAI_APIKEY')
  if not openai.api_key:
    api_keyfile = os.getenv('OPENAI_APIKEY_FILE')
    if not api_keyfile:
      api_keyfile = f"{os.getenv('HOME')}/.openai/api_key"
    try:
      with open(api_keyfile,"r") as fh:
        openai.api_key = fh.read().strip()
    except FileNotFoundError:
      error(f"You do not have an OpenAI API key yet. Use https://beta.openai.com/account/api-keys to get a new key, and use '--apikey=YOUR_APIKEY' to set it.",E_TOKEN)

def set_apikey(key):
  if not openai.api_key:
    api_keyfile = os.getenv('OPENAI_APIKEY_FILE')
    if not api_keyfile:
      api_keyfile = f"{os.getenv('HOME')}/.openai/api_key"
    with open(api_keyfile,"w") as fh:
      fh.write(key)

BASENAME=os.path.splitext(os.path.basename(sys.argv[0]))[0]
TEXTWRAP = 80
TEMPERATURE = 0.5
ECHO = False
CHOICES = 1
FORCE = False
TOKENS = 1024
BOTNAME = "text-davinci-003"
WARNINGS = False
ERRORS = False
DEBUG = False

E_OK = 0
E_FAILED = 1
E_TOKEN = 2
E_SYNTAX = 3

def error(msg,code=None):
  if not ERRORS:
    print(f"ERROR [{BASENAME}]: {msg}",file=sys.stderr)
  if type(code) is int:
    exit(code)
  elif type(code) is Exception:
    raise code(msg)
  else:
    raise OpenaiHelperException(msg)

def warning(msg):
  if not WARNINGS:
    print(f"WARNING [{BASENAME}]: {msg}",file=sys.stderr)

def asbool(value):
  if value == True or value == 'True' or (type(value) is int and value != 0):
    return True
  elif value == False or value == 'False' or value == 0:
    return False
  else:
    raise ValueError(f"value '{value}' is not a boolean")

def query(query_text):
  if "GridLAB-D" not in query_text and "gridlabd" not in query_text and not FORCE:
    error("query not related to GridLAB-D",E_FAILED)
  get_apikey()
  try:
    response = openai.Completion.create(
      model=BOTNAME,
      prompt=query_text,
      max_tokens = TOKENS,
      temperature = TEMPERATURE,
      echo = ECHO,
      n = CHOICES,
    )
    N = len(response['choices'])
    reply = []
    if N > 1:
      reply.append(f"{N} response{'' if N==1 else 's'} received")
      for n, result in enumerate(response["choices"]):
        reply.append("")
        reply.append(f"Response {n+1}:")
        reply.append(f"-----------")
        reply.append(result['text'].strip().replace('\n\n','\n'))
        if result["finish_reason"] == "length":
          warning(f"response {n} truncated; use '--length=<int>' option with a value greater than {TOKENS}")
    else:
        reply.append(response["choices"][0]['text'].strip())
        if response["choices"][0]["finish_reason"] == "length":
          warning(f"response truncated. Use '--length=<int>' option with a value greater than {TOKENS}")
  except:
    e_type,e_value,e_trace = sys.exc_info()
    error(e_value,E_FAILED)
    if DEBUG:
      raise
    return []
  return "\n".join(reply)

if __name__ == "__main__":
  
  query_data = []
  for arg in sys.argv[1:]:
    spec = arg.split("=")
    tag,value = (spec[0],True) if len(spec) == 1 else (spec[0],'='.join(spec[1:]))
    if tag in ['-h','--help','help']:
      print(__doc__,file=sys.stdout)
      exit(0)
    elif tag in ['--signup']:
      os.system("open https://beta.openai.com/account/api-keys")
      exit(E_OK)
    elif tag in ['--apikey']:
      set_apikey(value)
      exit(E_OK)
    elif tag in ['-N','--responses']:
      CHOICES = int(value)
    elif tag in ['-E','--echo']:
      ECHO = asbool(value)
    elif tag in ['-T','--temperature']:
      TEMPERATURE = float(value)
    elif tag in ['--force']:
      FORCE = asbool(value)
    elif tag in ['-M','--model']:
      BOTNAME = value
    elif tag in ['-L','--length']:
      TOKENS = int(value)
    elif tag in ['-q','--quiet']:
      ERRORS = asbool(value)
    elif tag in ['-w','--warning']:
      WARNINGS = asbool(value)
    elif tag in ['--debug']:
      DEBUG = asbool(value)
    elif tag in ['--silent']:
      WARNINGS = asbool(value)
      ERRORS = asbool(value)
    else:
      query_data.append(arg)

  if not query_data:
    print("Syntax: {BASENAME} [OPTIONS ...] [QUERY ...]",file=sys.stderr)
    exit(E_SYNTAX)
  query_text = " ".join(query_data)

  print(query(query_text),file=sys.stdout)
