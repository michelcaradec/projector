# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import csv


def get_schema(schema_filename):
    """
    Read schema file.
    """
    with open(schema_filename, "r") as csv_file:
        for line in csv_file:
            c_name, c_projection = line.split(";")
            yield c_name, c_projection.rstrip("\n")


def project(data_filename, schema_filename, delimiter=";", quotechar="\"", lineterminator="\n"):
    """
    Project selected columns.
    """
    schema = [(c_name, c_projection) \
             for (c_name, c_projection) \
             in get_schema(schema_filename)]

    with open(data_filename, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter, quotechar=quotechar)
        writer = csv.writer(sys.stdout, \
                            delimiter=delimiter, \
                            quotechar=quotechar, \
                            quoting=csv.QUOTE_ALL, \
                            lineterminator=lineterminator)

        for row in reader:
            row_project = [col \
                          for (col, (_, c_projection)) \
                          in zip(row, schema) if c_projection == "T"]
            writer.writerow(row_project)


def main(args):
    """
    Main function.
    """
    data_filename = ""
    schema_filename = ""
    delimiter = ";"
    quotechar = "\""
    lineterminator = "\n"

    for arg in args:
        if arg.startswith("-data:"):
            data_filename = arg[6:]
        elif arg.startswith("-schema:"):
            schema_filename = arg[8:]
        elif arg.startswith("-delimiter:"):
            delimiter = arg[11:]
        elif arg.startswith("-quotechar:"):
            quotechar = arg[11:]
        elif arg.startswith("-lineterminator:"):
            lineterminator = arg[16:]

    if data_filename == "":
        raise Exception("Missing data filename")
    if schema_filename == "":
        raise Exception("Missing schema filename")

    project(data_filename, schema_filename, delimiter, quotechar, lineterminator)


if __name__ == "__main__":
    main(sys.argv[1:])
