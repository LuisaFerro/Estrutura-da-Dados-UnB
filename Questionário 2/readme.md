De acordo com o [livro da disciplina](https://runestone.academy/ns/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html), 

*In Python, all classes have a set of standard methods that are provided but may not work properly. One of these, __str__, **is the method to convert an object into a string.** The default implementation for this method is to return the instance address string as we have already seen. What we need to do is provide a “better” implementation for this method. We will say that this implementation overrides the previous one, or that it redefines the method’s behavior.*

ou seja, pra poder printar o objeto de uma classe a ente tem que instanciar como esse objeto pode ser chamado na própria classe. A forma de fazer isso é:

*To do this, we simply define a method with the name __str__ and give it a new implementation as shown in Listing 4. This definition does not need any other information except the special parameter self. In turn, the method will build a string representation by converting each piece of internal state data to a string and then placing a / character in between the strings using string concatenation. The resulting string will be returned any time a Fraction object is asked to convert itself to a string. Notice the various ways that this function is used.*
