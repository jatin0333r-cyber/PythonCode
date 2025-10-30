global_var="I am global variable"
def outer_function():
    global global_var
    def inner_function():
        global_var="I am modified in inner"
        inner_function()

outer_function()
print(global_var) #Output: I am modified in inner