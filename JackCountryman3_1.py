import formulas, sys

def main():
    if len(sys.argv) <= 1:
        print("Need to provide the operator name")
        sys.exit()
    if len(sys.argv) <= 3:
        sys.exit("Need to provide at least two values")
    if len(sys.argv) >= 4:
        op = sys.argv[1]
        args = [float(i) for i in sys.argv[2:]]
        if op == "divide":
            print(f'Answer = {formulas.divide(args):.2f}')
        elif op == "multiply":
            print(f'Answer = {formulas.multiply(args):.2f}')
        elif op == "subtract":
            print(f'Answer = {formulas.subtract(args):.2f}')
        elif op == "add":
            print(f'Answer = {formulas.add(args):.2f}')
        else:
            print("Valid operator names (add, subtract, multiply, divide)")

if __name__ == '__main__':
    main()