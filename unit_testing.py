import unit_testing_sample_code
 

#include test_name as the parameter of the function
def test_string(test_name, expected, actual): 
    if actual == expected:
        print(f"Test {test_name} passed! \'{expected}\' matches \'{actual}\'.")
    else:
        print(f"Test {test_name} failed. Expected: \'{expected}\'. Got: \'{actual}\'.")
    
def test_strlist(test_name, expected, actual):
    for t in range(int(test_name) + 1):
        print(f"Test {test_name}:")
        for i in range(len(expected)):
            if expected[i] == actual[i]:
                print(f"Part {i} in test {test_name} passed! \'{expected[i]}\' matches \'{actual[i]}\'")
            else:
                print(f"Part {i} in test {test_name} failed. Expected: \'{expected[i]}\'. Got: \'{actual[i]}\'.")
   
def test_int(test_name, expected, actual):
    if actual == expected:
        print(f"Test {test_name} passed! \'{expected}\' matches \'{actual}\'.")
    else:
        print(f"Test {test_name} failed. Expected: \'{expected}\'. Got: \'{actual}\'.")   

def test_intlist(test_name, expected, actual):
    for t in range(int(test_name) + 1):
        print(f"Test {test_name}:")
        for i in range(len(expected)):
            if expected[i] == actual[i]:
                print(f"Part {i} in test {test_name} passed! \'{expected[i]}\' matches \'{actual[i]}\'")
            else:
                print(f"Part {i} in test {test_name} failed. Expected: \'{expected[i]}\'. Got: \'{actual[i]}\'.")

# Run tests
if __name__ == '__main__':
    print("\nString Capitalizer Tests:")
    # test_string is the function for testing the string capitalizer and takes 
    # three arguments: test number (“0”), expected output value (“TwO”), and
    # the call to the string_capitalizer function with the argument “two”.
    test_string("0", "TwO", unit_testing_sample_code.string_capitalizer("two"))
    test_string("1", "C", unit_testing_sample_code.string_capitalizer("c"))
    test_string("2", "FouR", unit_testing_sample_code.string_capitalizer(4))
    test_string("3", "", unit_testing_sample_code.string_capitalizer(""))
    
    print("\nList Capitalizer Tests:")
    test_strlist("0", ["TwO","C","FouR",""], unit_testing_sample_code.capitalize_list(["two","c",4,""]))
    
    print("\nInteger Manipulator Tests:")
    test_int("0", 66, unit_testing_sample_code.integer_manipulator(10))
    test_int("1", 2, unit_testing_sample_code.integer_manipulator(2))
    test_int("2", 6, unit_testing_sample_code.integer_manipulator(3))
    test_int("3", 0, unit_testing_sample_code.integer_manipulator(0))
    test_int("4", 1, unit_testing_sample_code.integer_manipulator("three"))
    
    print("\nManipulate List Tests:")
    test_intlist("0", [66,2,6,0,1], unit_testing_sample_code.manipulate_list([10,2,3,0,"three"]))
    