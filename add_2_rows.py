import csv

def add_row_below_existing_rows(csv_file, column_index, new_row_data):
    updated_rows = []

    # Read the existing CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            updated_rows.append(row)  # Add existing row

            # Add a new row below each existing row
            if index % 1 == 0:  # Insert a new row for even index rows (0, 2, 4, ...)
                new_row_1= [None] * len(row)
                new_row_1[column_index] = new_row_data
                updated_rows.append(new_row_1)

                new_row_2= [None] * len(row)
                new_row_2[column_index] = new_row_data
                updated_rows.append(new_row_2)


    # Write the updated rows to a new CSV file
    with open('updated_file_3_event.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# Usage example
csv_file = 'All_Annotation_Real3EV.csv'  # Path to the CSV file
column_index = 2  # Index of the selected column (0-based)
new_row_data = ''  # New row data

add_row_below_existing_rows(csv_file, column_index, new_row_data)
