Project Aim: 

Implement all the operations of relational algebra

An overview of Relational Algebra:


The basic set of operations for the relational model is the relational algebra. These operations enable a user to specify basic retrieval requests as relational algebra expressions. The result of a retrieval is a new relation, which may have been formed from one or more relations. The algebra operations thus produce new relations, which can be further manipulated using operations of the same algebra. A sequence of relational algebra operations forms a relational algebra expression, whose result will also be a relation that represents the result of a database query (or retrieval request).
The relational algebra is very important for several reasons.

1. First, it provides a formal foundation for relational model operations. 

2. Second, and perhaps more important, it is used as a basis for implementing and optimizing queries in the query processing and optimization modules that are integral parts of relational database management systems (RDBMSs).

3. Third, some of its concepts are incorporated into the SQL standard query language for RDBMSs.

 
There are many operations in relational algebra, like

•	Select

•	Project

•	Rename

•	Union

•	Intersection

•	Difference

•	Natural Join

•	Theta Join

•	Division Operator

All these operators are implemented here, using Python


Design and implementation-

Idea behind the functions-

1.	Select :
Here the idea is that we take the input condition and the name of the relation from the user and substitute in the attributes present in the input condition with corresponding value present in every tupple of the relation stated, and evaluate the logical expression. If this line evaluates to true, only then the line is printed.
The syntax is given in the help documentation of the program.

2.	Project :
Here the idea is to take the relation and the set of attribute names to be projected as arguments in the syntax specified in the help documentation, and then it compares the name of the attribute in the file with those specified and if they match only then it is shown.

3.	Rename :   
This is nothing but renaming a file and then using it
.
4.	Union, Difference and Intersection :
This simulates the required operations of the set theory based on the concept of union compatibility and only then executes it else generates an error.

5.	Theta Join, Cartesian Product and Natural Join :
This simulates the various join operations, and joins the attributes. This can include any number of relations as the input, and is efficient in storing the result in a new relation, but delay occurs in displaying the result.


PROBLEMS FACED/ ASSUMPTIONS :


•	It is seen that though this method gives extremely fast results for fairly small inputs,as the number of tupples  increases, generally beyond 3000 or so, the displaying stops , because of increasing burden over the RAM.The problem is with the displaying.

•	Another problem is with the strict syntax.

•	A third problem is with the naming of attributes in the relation,which should be as given in the assumptions.

•	A fourth  problem is with regard to the use of aggregate functions, which is not possible here.



FUTURE WORK-


•	I am trying to implement Aggregate functions, but these are absent in R.A.

•	Insert and Delete operations can also be added here.

•	Regular Expression Evaluation can be added as an extended functionality.


Help/ Manual:

=======> This is the help Documentation for the Relational Algebra <========
	Here we have help for all the instructions

1.Selection :
	This is used to simulate the select or the sigma operator of relational algebra to select few tupples.
   Syntax : "" select/sig | relation_name | on | conditions ""
	This can also be used recursively,where , you need to write the name of expression instead of the <relation_name> field
--------------------------------------------------------------------------------------------------------------------------------------------------

2.Project :
	This is used to simulate the project or the pi operator of relational algebra to project few columns.
   Syntax : "" project/pi | list_of_attributes | from | relation_name ""
	This can also be used recursively,where , you need to write the name of expression instead of the <relation_name> field 
--------------------------------------------------------------------------------------------------------------------------------------------------

3.Rename :
	This is used to rename a relation along with all its attributes, like the rho operator in relational algebra.
    Syntax : "" rename/rho | old_relation_name | to | new_relation_name | new_attributes ""
	This can also be used recursively,where , you need to write the name of expression instead of the old_relation_name field   

    This can also be simulated for renaming the relation only using the "newname <-- oldname" operator
--------------------------------------------------------------------------------------------------------------------------------------------------

4.Display :
	This is used to display a relation whose name is given as the argument.
    Syntax : "" display | relation_name ""
	This can also be used recursively,where , you need to write the name of expression instead of the relation_name field 
	Without any display is as good as display
This ends the loop also
--------------------------------------------------------------------------------------------------------------------------------------------------

5.Diff :
	This is used to find set difference.
    Syntax : " diff/- | relation_list_seperated_by_commas ""

--------------------------------------------------------------------------------------------------------------------------------------------------

6.Union :
	This is used to find set union.
    Syntax : " union/U | relation_list_seperated_by_commas ""
	

--------------------------------------------------------------------------------------------------------------------------------------------------

7.Intersect :
	This is used to find set intersection.
    Syntax : " intersect/n | relation_list_seperated_by_commas ""


--------------------------------------------------------------------------------------------------------------------------------------------------

8.Natural Join :
	This is used to display natural join of 2 or more relation.
    Syntax : " join/* | relation_list_seperated_by_commas ""
	

--------------------------------------------------------------------------------------------------------------------------------------------------

9.Theta Join :
	This is used to display theta join of 2 conditions.
    Syntax : " theta | relation_list_seperated_by_commas | on | join_condition ""

--------------------------------------------------------------------------------------------------------------------------------------------------

10.Division :
	This is used to display division between 2 compatible relations.
    Syntax : " div/% | dividend | divisor ""



Assumptions:


1. The attributes names in the relations begin with the filename seperated by period.

2. The file has following format.

	line 1: attribute list(delim == | )

	line 2: datatype list(delim == | )

	line 3: -------------------------------

Then all tupples appear

3. Delimiter is "|"

4.No aggregate functions are present.

