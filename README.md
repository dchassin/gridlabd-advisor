# OpenAI GridLAB-D Advisor

**WARNING**: this tool is highly experimental. The responses can be incomplete, misleading, and simply wrong.

## Installation

To install the tool from the command line:

~~~
sh$ curl -sL https://raw.githubusercontent.com/dchassin/gridlabd-advisor/install.sh | bash
~~~

## API Key

To obtain an API key from OpenAI:

~~~
sh$ gridlabd advisor --signup
~~~

After you signup, you can copy the key for your clipboard and paste it on the command line when you install the API key:

~~~
sh$ gridlabd advisor --apikey=YOUR_APIKEY
~~~

## Usage

To get advice:

~~~
sh$ gridlabd advisor 'How do I define a class in GridLAB-D?'
~~~

## Useful Options

### `--responses|-N=<int>`

Request multiple responses. By default only one answer is returned. However, the OpenAI model can return multiple answers. This is helpful when the answers may be of uncertainty quality or accuracy.

### `--echo|-E`

Echo the query in the response. The default is `False`.

### `--temperature|-T=<float>`  

Set the riskiness of responses.  Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 for ones with a well-defined answer. The default value is `0.1`.

### `--force`

Force responses to queries even when the advisor thinks they are not related to GridLAB-D. The default is `False`.


## Getting help

To get detailed help:

~~~
sh$ gridlabd advisor help
~~~
