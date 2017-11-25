def function(var):
    if len(var) < 3:
        print(var)
    elif var[-3:]=="ing":
        print(var+"ly")
    else:
        print(var+"ing")



function("vipin")
function("abc")
function("no")
function("lying")
function("a")
