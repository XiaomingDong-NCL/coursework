This is my readme.file

# make sure you have installed the follow packages first
** Python.version 3.7.6
** Django.version 3.0.3
** Biopython

# a quick link to get started
# main funtions and methods are stored in these files, two apps named bioinformaticsapp and helloapp , three python files 
toccess to my file you may also use the command line as below, or download the zip file I submit through NESS:
git clone http://github.com/XiaomingDong-NCL/coursework.git
cd path/to/coursework
ls 
# my coursework is about a web development based on Django, to run it use the command below
cd path/to/coursework
python manage.py runserver

# you will get a development server address, http://127.0.0.1:8000/, copy it your explorer
This address is the homepage of my web. There are three webs in total, home page offers a link to the main page, /info/ shows my git address, /bio/ shows the main use of the web.

# I designed this web for the purpose of showing bioinformatics beginners how we could use python to work with biology data
Is this readme file, i will address my coursework as below: how to , what i have finined and what not


# How i programmmed my files, and where my codes are stored.
In the coursework project:

1, manage.py is used for running server

2, part11.py declares a new class My_randomseq taking a Seq object as parameter, method My_randomseq.rev_c is used for generating its reverse_complement sequence. Method My_randomseq.protein is used for generating its possible proteins, transtarting with the first base, second base and third base separtely.
It would ask you to type in an integer number and than it generates a random sequence. The length of DNA, the random sequence, the reverse_complement sequence, the protein sequence that could be translated into is will be printed.
eg: Please enter a random integer number greater than zero: 
if you type in 10, the results will be
the length of DNA is: 10
the random sequence is: CCAGGTCCCT
the reverse_complement sequence is: AGGGACCTGG
the protein sequence that could be translated into is: [Seq('PGP', ExtendedIUPACProtein()), Seq('QVP', ExtendedIUPACProtein()), Seq('RS', ExtendedIUPACProtein())]

3, part12.py is added another functions from part11.py, named find_lmotif. It takes two sequence and return the longest shared motif, which means teh longest shared substring of these two sequences.

4, part1witout_input.py has the same class defination but without input. It would be imported to my Django project.
# part11.py and part12.py are designed to showe the users how my web runs , part1without_input.py is used to Django project. I intened to put the code on the web and show the uesage case on the webpage, but have not finished this part.


5, /coursework/bioinformaticsapp/tempaltes/ bio.html
# This file is designed as web template and it stores four variables that could be passed by POST and GET method.Click this file, it shows your how this webpage would be like. The four variables are {{length}} , {{myRandomseq}} ,  {{myRCSeq}} , {{myProtein}}. They are designed to pass values once users submit an integer number and submit the functions they want to require. 
I also declared methods 'get' 'post' with labels which could be recognized by system.

6, /coursework/bioinformaticsapp/views.py
# This is the main file to file to get deal with the request from users and return the results. 

7, /coursework/bioinformaticsapp/models.py, forms.py  are designed for passing values for view.py