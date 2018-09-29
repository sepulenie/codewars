def camel_case(string):
    g = ''
    space_p = False
    for i,n in enumerate(string):
        if n == ' ':
            space_p = True
        else:
            if space_p == True or i == 0:
                g+=string[i].upper()
                space_p = False
            else:
                g+=string[i].lower()
    return(g)
















camel_case('test case')
#Test.assert_equals(camel_case("test case"), "TestCase")