# koppreeds
HTML source for KoppReeds web site

If anything changes in the include directory, the program `dshea-include.py` needs to be run on all of the HTML files in the main directory.  The Python program is in the main directory.

## `dshea-include.py`

this program looks for specific HTML comments and replaces the text inbetween the start and stop comment with the contents of the specified file.  Here is an example:

```html
<!-- dshea-include BEGIN include/header.html ***************** -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="main.css" type="text/css">
<!-- dshea-include END include/header.html ***************** -->
```

The program looks for the two comments:

```
dshea-include BEGIN filename
dshea-include END filename
```

and will replace the text in between these comments with the contents of the file **filename**

## command line syntax

```
./dshea-include.py <file1 [file2 ...]>
```
