"""
Hypertext Markup Language (HTML) is the standard markup language for creating web pages and web applications. 
HTML is the language in which most websites are written. 
HTML is used to create pages and make them functional.
Write a program, that will read HTML variable and output attribute value of id attribute (tag) into the console. 
Input will be provided in a single line as outlined below. 
If HTML variable doesn't contain <html> attribute, print out into the console message: "Invalid input!".
Sample Output:
     input: <!DOCTYPE html><html><head><title>Java</title></head><body><p id="myid"></p></body></html>
     output: myid
"""

html  = input("Please enter the HTML code : ")
if html.find("html")==-1:
    print("Invalid input!")
else:
    print("output : ", html[html.index('"')+1:html.index('"',html.index('"')+1)])
