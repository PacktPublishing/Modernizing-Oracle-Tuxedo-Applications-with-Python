# Modernizing Oracle Tuxedo Applications with Python 

<a href="https://www.packtpub.com/in/programming/modernizing-oracle-tuxedo-applications-with-python?utm_source=github&utm_medium=repository&utm_campaign=9781786461629"><img src="https://www.packtpub.com/media/catalog/product/cache/c2dd93b9130e9fabaf187d1326a880fc/9/7/9781801070584-original_77.png" alt="Modernizing Oracle Tuxedo Applications with Python" height="256px" align="right"></a>

This is the code repository for [Modernizing Oracle Tuxedo Applications with Python](https://www.packtpub.com/in/programming/modernizing-oracle-tuxedo-applications-with-python?utm_source=github&utm_medium=repository&utm_campaign=9781786461629), published by Packt.

**A practical guide to using Oracle Tuxedo in the 21st century**

## What is this book about?

This book covers the following exciting features:
* Understand Oracle Tuxedo as a microservice platform
* Develop Oracle Tuxedo applications using Python 3
* Perform administration tasks programmatically with Python 3
* Extract Tuxedo statistics for monitoring application performance
* Integrate Tuxedo into the modern software ecosystem
* Understand how distributed transactions work in Tuxedo

If you feel this book is for you, get your [](https://www.amazon.com/dp/180107058X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import tuxedo as t
_, _, res = t.tpcall(
".TMIB",
{
"TA_CLASS": "T_DOMAIN",
"TA_OPERATION": "GET",
},
)
```

**Following is what you need for this book:**
This book is for developers who are new to Tuxedo and are looking to develop a new modern front-end or integrate Tuxedo in their applications. The book will also help experienced Tuxedo, C or COBOL developers to improve their productivity and QA engineers to automate Tuxedo application tests. Beginner-level knowledge of Python and Linux shell is required before getting started with this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-12 |                                          | Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781801070584_ColorImages.pdf).

### Related products
* Modern Python Cookbook - Second Edition [[Packt]](https://www.packtpub.com/product/modern-python-cookbook-second-edition/9781800207455?utm_source=github&utm_medium=repository&utm_campaign=9781800207455) [[Amazon]](https://www.amazon.com/dp/180020745X)

* Oracle CX Cloud Suite [[Packt]](https://www.packtpub.com/product/oracle-cx-cloud-suite/9781788834933?utm_source=github&utm_medium=repository&utm_campaign=9781788834933) [[Amazon]](https://www.amazon.com/dp/1788834933)

*  [[Packt]]() [[Amazon]](https://www.amazon.com/dp/)

*  [[Packt]]() [[Amazon]](https://www.amazon.com/dp/)

## Get to Know the Author
**Aivars Kalvans**
is a developer, software architect, and consultant. He has been using Oracle Tuxedo (formerly BEA Tuxedo) since version 8 in 2003 to develop the Tieto Card Suite payment card system using the C++, Python, and Java programming languages. During his almost 19-year career at Tieto, Aivars has been involved in many projects related to payment card issuing, acquiring, and utility payments through mobile phones, ATMs, and POS terminals.



### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801070584">https://packt.link/free-ebook/9781801070584 </a> </p>