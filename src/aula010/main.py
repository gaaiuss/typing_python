# Protocol and Structural Subtyping: static typing in Python

# Until now we have been working with nominal typing, in other words, a class
# is subtype of another only when you declare it explicitly.
# Example: if 'B' inherit from 'A', then 'B' is an 'A'. This is nominal subtyping.

# In daily life, Python is famous by the 'duck typing', in other words, in runtime
# Python is not checking inheritance but instead a if especific method or attribute
# exists in the project.

# The good news is that in the static typing we also have an equivalent of duck
# typing and that is Structural Typing.

# To work with structural typing we use Protocol. It permits us to define a contract
# of methods/atributes that any class can fulfill even without declaring inheritance
