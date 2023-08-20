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
                    
                    for pair in to_refresh:
                        io = input(f" do you want refresh pair: {pair}? y/n or a for refreshing all pairs")
                        match io:
                            case "y":
                                command_funcs.refresh_pair(pair)
                            case "n":
                                continue
                            case "a":
                                command_funcs.refresh_pairs(to_refresh)
                                break
                    
                case "-clear":
                    command_funcs.clear_file_pairs_file()
                case "-dir":
                    src = sys.argv[first_file_idx]
                    dst = sys.argv[first_file_idx + 1]
                    command_funcs.add_folders(src, dst)
                case _:
                    raise Exception("no mode added, please add a mode, -add, -refresh, -clear. -dir")

if __name__ == "__main__":
    main()
