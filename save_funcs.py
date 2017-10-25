def save(file_, last_name, first_name, uid):
    """Save in the form:
        lastname,firstname,uid
        On a new line of the file."""

    formatted = "%s,%s,%d\n" % (last_name, first_name, uid)

    f = open(file_, "r")

    # list the lines
    lines = [line for line in f.readlines()]
    f.close()

    # empty file
    if not lines:
        lines = formatted
        f = open(file_, "w")
        f.writelines(lines)
        f.close()
        return

    for idx, line in enumerate(lines):
        # ignore lines with fewer than 3 csv
        if len(line) < 3:
            continue

        if idx == len(lines) - 1:  # reached the end
            lines.append(formatted)
            _write(file_, lines)
            return

        # our line comes first alphabetically, or EOF
        for i in range(len(line)):
            # The name doesn't go here
            if formatted[i] > line[i]:
                break
            # check the next letter if not reached the end of the entry
            elif formatted[i] == line[i] and i != len(line) - 1:
                continue
            # The name belongs here in the list
            else:
                # save the lines we haven't read yet
                lines_left = lines[idx:]
                # insert new line
                lines[idx] = formatted

                # rewrite the rest of the lines
                lines[idx+1:] = lines_left
                _write(file_, lines)
                return


def _write(file_, lines):
    """Write the list to the file as-is."""
    f = open(file_, "w")
    f.writelines(lines)
    f.close()


if __name__ == '__main__':
    ex = "example.csv"
    first = "Matthew"
    last = "AiLoreto"
    save(ex, last, first, 0)
