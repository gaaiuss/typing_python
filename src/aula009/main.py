# Generic classes

# The generic class typing or generic classes follows the same pattern of the
# generic functions of the previous lesson. Define a type parameter on the class
# and it automatically becomes a generic class with the new syntax of PEP 695

# In the following example we have a MutableMapping that is fixed with a key and
# value. Our work here is to turn that into a generic class that accepts type
# parameters so that it can be used with the types that achieve the objective.

# The final objective is to achive the possibility to invert the kye and value.
# Remember that the key must be hashable.
