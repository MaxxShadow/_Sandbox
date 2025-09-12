#
#
#

def funcA01(A):
     AA = "AA - funcA01"
     print(f"func01: AA => {AA}")
     print(f"func01: A => {A}")
     A = "A - funcA01"
     return(A)

def funcA02():
     global A                      # použití globální proměnné, def mimo funkci
     AB = "AB - funcA02"
     print(f"func02: AB => {AB}")
     print(f"func02: A => {A}")
     A = "A - funcA02"             # změna globální proměnné
     return(A)

A = "A - main"
print(f"main: A => {A}")
print("")

print(funcA01(A))
print(f"main: A => {A}")
print("")

print(funcA02())
print(f"main: A => {A}")
