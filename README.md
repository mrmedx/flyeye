# FlyEye

<p align="center">
  <img width="250" height="250" src="https://github.com/mrmedx/flyeye/blob/main/icon/icon.jpg" alt='FlyEye'>
</p>

<p align="center">
  ⚠️ **We disclaim responsibility for any illegal activities. Users are advised to adhere to applicable laws and use the tool responsibly.**
  
FlyEye® is an open source web forensics framework for web investigation and detecting data leaks using simple queries like:"who said "download this" on <WEBSITE> after 2023-12-27 in <COUNTRY>" or "who leaked access_token on <WEBSITE> after 2023-01-01", users can retrieve and analyze all the matched results from example.com in the USA after the specified date, and gather valuable information, or monitor web traffic from one website to another, finding a group commenting about a specific topic in a certain place and time, FlyEye used also for web security to protect your website by identifying and addressing potential sensitive information leakage, for more information how to use FlyEye for Web Forensics check out the documentation below. 


</p>

<p align="center">
  <a href="https://www.facebook.com/jasmeztr"><img src="https://www.facebook.com/favicon.ico" width="18" height="18"></a>
</p>

## Requirements

The requests python library:

- [requests](https://pypi.org/project/requests/)

Install the requirements:

```bash
pip install -r requirements.txt

```

## Usage

Initiate an investigation on web traffic from example.com to any distination.com subdomain and save the results in a 'results.json' to load it later for more analysis:

```bash
python flyeye.py saveto results.json who fly from example.com to *.distination.com

```
## Load Data From File
 
Load the previous saved json file and perform another analysis to detect the source that includes the text 'click here.':
 
```bash
python flyeye.py load results.json who said excat "click here"

```

## Country, Date and Time

Specify a date in the year-month-day, and the country in - [ISO 3166-1 alpha-2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format:

```bash
python flyeye.py who fly from example.com to distination.com in us after 2023-11-01
python flyeye.py who fly from example.com to distination.com in uk before 2023-11-01 and after 2022-11-01 

```

## AND, OR, NOT

Logical and, or, not

```bash
python flyeye.py who said exact "hello world" and said "hi" on example.com

python flyeye.py who said exact "hello world" and not said "hi" on example.com

python flyeye.py who said exact "hello world" or said "hi" on example.com

python flyeye.py who said "click here" in uk on example.com or on example1.com and not on example3.com

```

## Exact

This query match the occurrence of "click" and here" anywhere in the source, but  when using the keyword "exact" it will look for the exact word "click here to download the file":

```bash
python flyeye.py who said exact "hello world" on example.com

python flyeye.py who said "click here" or said exact "click here to download the file" in us on example.com and not on example2.com 

```

## any site

```bash
python flyeye.py who fly from example.com to any site

```

## Web Security

Discover data leaks caused by website bugs. The tool currently supports three types of leaks:

## Access Token

```bash
python flyeye.py who leaked access_token on api.example.com after 2023-01-01
python flyeye.py who leaked access_token on *.example.com after 2023-01-01

```

## Email

```bash
python flyeye.py who leaked email on api.example.com after 2023-01-01
python flyeye.py who leaked email on *.example.com after 2023-01-01

```

## Phone

```bash
python flyeye.py who leaked phone on *.example.com after 2023-01-01

```

## Data Leaked By Humans

To find data leaked by human just use the said keyword for example:

```bash
python flyeye.py who said "email list" and said "@gmail.com" on any site after 2023-01-01

```

## Help
Show the help menu:

```bash
python flyeye.py help

flyeye 1.0 - web forensics framework.
who:
  info about an event.
  Example: python flyeye.py who fly from example.com to des.com
said:
  find words mentioned in a source
  Example: python flyeye.py who said "download now" on example.com
fly:
  info about web traffic.
  Example: python flyeye.py who fly from example.com to des.com in us
from:
  the source website.
  Example: python flyeye.py who fly from example.com to des.com
to:
  the destination website.
  Example: python flyeye.py who fly from example.com to des.com
on:
  the target website.
  Example: python flyeye.py who said "hello world" on example.com
in:
  the target country.
  Example: python flyeye.py who said "hello world" in us
before:
  search before the given date <Y-M-D>
  Example: python flyeye.py who said "hello world" before 2023-01-01
after:
  search after the given date <Y-M-D>
  Example: python flyeye.py who said "hello world" after 2023-01-01
leaked:
  find leaked data <email, access_token, phone>
  Example: python flyeye.py who leaked email on example.com
email:
  the leaked data type
  Example: python flyeye.py who leaked email on example.com
phone:
  the leaked data type
  Example: python flyeye.py who leaked phone on example.com
access_token:
  the leaked data type
  Example: python flyeye.py who leaked access_token on example.com
any:
  used before the site keyword to search for any site
  Example: python flyeye.py who fly from any site to example.com
site:
  used after the any keyword to search for any site
  Example: python flyeye.py who fly from example.com to any site
exact:
  search for exact word
  Example: python flyeye.py who said exact "hello world" on example.com
and:
  logical and
  Example: python flyeye.py who said exact "hello world" and said "hi" on example.com
or:
  logical or
  Example: python flyeye.py who said exact "hello world" or said "hi" on example.com
not:
  logical not
  Example: python flyeye.py who said exact "hello world" and not said "hi" on example.com
saveto:
  save the results to a local file
  Example: python flyeye.py saveto results.json who said exact "hello world" on example.com
load:
  load a flyeye saved results and perform a task
  Example: python flyeye.py load results.json who said exact "download this file"
['help', '-h', '--h']:
  show this help menu.
  Example: python flyeye.py help"

```
To get help about a specific command:

```bash
python flyeye.py help access_token

flyeye 1.0 - web forensics framework.
access_token:
  the leaked data type
  Example: python flyeye.py who leaked access_token on example.com

```


This README will be regularly updated with additional documentation for users or developers. For any inquiries or assistance, please reach out via the provided email.

