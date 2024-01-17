# Part 1: Author class

Create a new class called Author.  Create a regular class, not a dataclass.

An Author has a name, and a list of books published.

When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.

Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.

Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.

Write a main function to test your class, create some example authors, and publish some example books.

# Part 2: Author class - no duplicate books

Start with the program from part 1.

In this version, an author can't publish two books with the same name.

When the publish method is called, print an error message if the book given has the same name as a book currently in the books list. Do not add the duplicate book. (In other words, make sure the Author object's book list doesn't already contain that name).  

In your breakout rooms: there's more than one way to solve this - can you come up with two different solutions?

# Part 3: Student dataclass

Type in the dataclass code from the slides/video. You would have done this before class.

Add one more field: gpa, a float.

Write a main function to create some example Student objects with some example names, college_id and GPA values. 

Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 

Add some comments in your code to compare the dataclass version to the "traditional" version.

To submit:

Add all of your files to a GitHub repository. Submit the link to the Lab 2 dropbox. 