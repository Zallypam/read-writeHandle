
def modify_file_content(input_filename, output_filename):

    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()
        
        # Modify the content (example: convert to uppercase)
        modified_content = [line.upper() for line in content]
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)
        
        print(f"Modified content successfully written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read the file '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    # Ask the user for the input and output filenames
    input_filename = input("Enter the name of the file to read: ").strip()
    output_filename = input("Enter the name of the file to write: ").strip()
    
    # Call the function to handle the file operations
    modify_file_content(input_filename, output_filename)
