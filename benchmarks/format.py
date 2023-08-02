import re

from tabulate import tabulate

output_file = "output"
output_table_style = "github"
max_num_rows = 10


"""Typical ASV table file (before processing):
    
All benchmarks:

       before           after         ratio
     [fcd6c976]       [bc939276]
     <main>           <test-pr> 
            2.1k             2.1k     1.00  benchmarks.MemSuite.mem_list
          failed          304±2ms      n/a  benchmarks.TimeSuite.time_iterkeys
     2.43±0.05μs        205±0.7ms 84400.48  benchmarks.TimeSuite.time_keys
     9.67±0.03μs          505±1ms 52177.14  benchmarks.TimeSuite.time_range
          failed          1.01±0s      n/a  benchmarks.TimeSuite.time_xrange
"""

"""Formatted ASV table file (github style):
| Before      | After       | Ratio    | Method                             |
|-------------|-------------|----------|------------------------------------|
| [fcd6c976]  | [bc939276]  |          |                                    |
| failed      | 304±2ms     | n/a      | benchmarks.TimeSuite.time_iterkeys |
| 2.43±0.05μs | 205±0.7ms   | 84400.48 | benchmarks.TimeSuite.time_keys     |
| 9.67±0.03μs | 505±1ms     | 52177.14 | benchmarks.TimeSuite.time_range    |
| failed      | 1.01±0s     | n/a      | benchmarks.TimeSuite.time_xrange   |
"""


def format_asv_table_from_file(filename):
    """Parses and formats a table generated by asv compare.

    Parameters
    ----------
    filename : str
        Name of the file containing the table.

    Returns
    -------
    tuple of str
        Headers and rows of the formatted table.
    """
    headers = []
    table_data = []

    with open(filename, "r") as file:
        rows = parse_table_rows(file.readlines())
        headers = format_headers(rows[0])
        branch_data = [rows[1]]
        bench_data = rows[3:]
        num_results = min(max_num_rows, len(bench_data))
        table_data = extract_benchmarks(bench_data[:num_results])

    return headers, branch_data + table_data


def parse_table_rows(rows):
    """Splits the columns, for each row, by whitespace separator.

    Parameters
    ----------
    rows : list of str
        Lines read from a file.

    Returns
    -------
    list of lists
        List of columns for each row. The first three lines of the original
        file are ignored as they do not contain useful information.
    """
    return [re.split(r"\s+", row.strip()) for row in rows[3:]]


def format_headers(headers):
    """Reads and capitalizes the table headers.

    Parameters
    ----------
    headers : list of str
        List of headers read from the file.

    Returns
    -------
    list of str
        Table headers, updated and capitalized.
    """
    headers.append("method")
    return [header.capitalize() for header in headers]


def extract_benchmarks(lines):
    """Extracts the rows containing benchmarks.

    Parameters
    ----------
    lines : list of lists
        Lines containing benchmark information.

    Returns
    -------
    list of lists
        Lines containing failed benchmark information.
    """
    return list(filter(lambda line: len(line) == 4, lines))


if __name__ == "__main__":
    headers, rows = format_asv_table_from_file(output_file)

    with open(output_file, "w") as file:
        file.write(tabulate(rows, headers=headers, tablefmt=output_table_style))
