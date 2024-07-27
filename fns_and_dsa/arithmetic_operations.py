def perform_operation (num1 , num2, operations):
    match operations:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                print("Please enter a number other than 0")
            else :
                return num1 / num2
