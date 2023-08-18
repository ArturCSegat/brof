import sys
import command_funcs

def main():
    argc = len(sys.argv)

    options = []
    first_file_idx = 1

    # loads options into option list
    for i in range(1, argc):
        if sys.argv[i][0] == "-":
            options.append(sys.argv[i])
            first_file_idx += 1
    
    if len(options):
        for opt in options:
            match opt:
                case "-add":
                    src = sys.argv[first_file_idx]
                    dst = sys.argv[first_file_idx + 1]
                    command_funcs.add_pair_to_store(src, dst)
                case "-refresh":
                    to_refresh = command_funcs.find_changed()
                    print("Pairs to be updated: ")
                    print(to_refresh)
                    yn = input("Do you want to refresh? y/n: ")

                    if yn.lower == "n":
                        return

                    command_funcs.refresh_pairs(to_refresh)
                case "-clear":
                    command_funcs.clear_file_pairs_file()

if __name__ == "__main__":
    main()
