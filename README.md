# OpenAI GridLAB-D Advisor

**WARNING**: this tool is highly experimental. The responses can be incomplete, misleading, and simply wrong.

## Installation

To install the tool from the command line:

~~~
curl -sL https://raw.githubusercontent.com/dchassin/gridlabd-advisor/main/install.sh | bash
~~~

## API Key

To obtain an API key from OpenAI:

~~~
gridlabd advisor --signup
~~~

After you signup, you can copy the key for your clipboard and paste it on the command line when you install the API key:

~~~
gridlabd advisor --apikey=YOUR_APIKEY
~~~

## Usage

To get advice:

~~~
gridlabd advisor 'How do I define a class in GridLAB-D?'
In GridLAB-D, classes are defined using the class keyword followed by the class 
name. The class definition is then enclosed by a pair of curly braces and may 
contain other objects, such as properties, functions, and variables. For example, 
the following code defines a class called "MyClass":

class MyClass {
    // class definition goes here
};
~~~

## Useful Options

### `--responses|-N=<int>`

Request multiple responses. By default only one answer is returned. However, the OpenAI model can return multiple answers. This is helpful when the answers may be of uncertainty quality or accuracy.

### `--echo|-E[=<bool>]`

Echo the query in the response. The default is `False`.

### `--temperature|-T=<float>`  

Set the riskiness of responses.  Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 for ones with a well-defined answer. The default value is `0.1`.

### `--force[=<bool>]`

Force responses to queries even when the advisor thinks they are not related to GridLAB-D. The default is `False`.

### `--length|-L=<int>`

Set the number of token allowed in the response. Default is 1024.

### `--model|-M=<str>`

Set the bot model name. The default is "text-davinci-003".

### `--quiet|-q[=<bool>]`

Disable error message output.

### `--warning|-w[=<bool>]`

Disable warning message output.

### `--silent[=<bool>]`

Disable warning and error message output.

### `--debug[=<bool>]`

Enable traceback on exceptions.

## Getting help

To get detailed help:

~~~
gridlabd advisor help
~~~
