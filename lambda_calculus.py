# %%

# Only single argument functions, arguments are also function since nothing else 
# exists in the universe other than functions
f = lambda x: x

# %%
# Definition of TRUE and FALSE. TRUE and FALSE 
# are behaviors and does not say anything about the 
# universe. The behavior of TRUE function is to return 
# first value passed to it. The behavior of the FALSE 
# function is to return the second value passed to it.

# TRUE = lambda x: lambda y: x
def TRUE(x):
    return lambda y: x

# FALSE = lambda x: lambda y: y
def FALSE(x):
    return lambda y: y

# %%
print(TRUE(TRUE)(FALSE))
print(FALSE(TRUE)(FALSE))
# %%

# Logic gates

NOT = lambda x: x(FALSE)(TRUE)
print(NOT(TRUE))
print(NOT(FALSE))
# %%

AND = lambda x: lambda y: y(x)(y)
# AND = lambda x: lambda y: x(y)(x)
print(AND(TRUE)(TRUE))
print(AND(TRUE)(FALSE))
print(AND(FALSE)(TRUE))
print(AND(FALSE)(FALSE))

# %%
OR = lambda x: lambda y: x(x)(y)
print(OR(TRUE)(TRUE))
print(OR(TRUE)(FALSE))
print(OR(FALSE)(TRUE))
print(OR(FALSE)(FALSE))

# %%
# Numbers
ZERO = lambda f: lambda x: x
# Note that this is exactly the same as 
# the behavior of FALSE. Pick the second thing.

ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))

# %%
incr = lambda x: x+1
print(ONE(incr)(0))
print(TWO(incr)(0))
print(THREE(incr)(0))

# %%
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
print(SUCC(THREE)(incr)(0))

# %%
ADD = lambda x: lambda y: x(SUCC)(y)
print(ADD(THREE)(TWO)(incr)(0))
# %%
MUL = lambda x: lambda y: x(SUCC)((SUCC)(y))
print(MUL(THREE)(TWO)(incr)(0))

# %%
