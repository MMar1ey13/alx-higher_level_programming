if __name__ == "__main__":
        import sys
            n = len(sys.argv) - 1
                if n != 3:
                            print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="")
                                    sys.exit(1)
                                        op = sys.argv[2]
                                            if op != '+' and op != '-' and op != '/' and op != '*':
                                                        print("Unknown operator. Available operators: +, -, * and /",end="")
                                                                sys.exit(1)

                                                                    from calculator_1 import add, sub, div, mul
                                                                        a = int(sys.argv[1])
                                                                            b = int(sys.argv[3])
                                                                                if op == '+':
                                                                                            print("{} + {} = {}".format(a, b, add(a, b)))
                                                                                                elif op == '-':
                                                                                                             print("{} - {} = {}".format(a, b, sub(a, b)))
                                                                                                                 elif op == '/':
                                                                                                                              print("{} / {} = {}".format(a, b, div(a, b)))
                                                                                                                                  else:
                                                                                                                                               print("{} * {} = {}".format(a, b, mul(a, b)))
