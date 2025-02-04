def create_markdown_table(headers, rows, path):
    """
    Create a markdown table and write it to a file.

    :param headers: List of column headers
    :param rows: List of rows, where each row is a list of column values
    :param path: Path to the file where the table should be written
    :return: None
    """
    # Create the header row
    header_row = '| ' + ' | '.join(headers) + ' |'
    
    # Create the separator row
    separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    
    # Create the data rows
    data_rows = ['| ' + ' | '.join(map(str, row)) + ' |' for row in rows]
    
    # Combine all parts into the final table
    table = '\n'.join([header_row, separator_row] + data_rows)
    
    # Write the table to the specified file
    with open(path, 'w') as file:
        file.write(table)
    
    return table