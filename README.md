# Projector

Utility to scan a delimited file, and keep desired columns.

```bash
python projector.py -data:./sample/data.csv -schema:./sample/schema.csv
```

## Arguments

| Argument       | Description                                    |
|----------------|------------------------------------------------|
| data           | Source file.                                   |
| schema         | [Schema file](#schema-file).                   |
| delimiter      | Source file column delimiter (default = ;).    |
| quotechar      | Source file quote char (default = ").          |
| lineterminator | Source file end of line marker (default = \n). |

## Schema file

This file has no header, and uses a semicolon as field separator.

| Column      | Description                   |
| ------------|-------------------------------|
| Column name | Name of the column.           |
| Projection  | **T** to keep, **F** to skip. |

Column names must be declared in correct order.
