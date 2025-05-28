class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Calculate number of columns and rows
        num_cols = key
        num_rows = len(text) // num_cols
        num_extra_chars = len(text) % num_cols

        # Create a grid to store the decrypted text
        grid = []
        for i in range(num_rows + (1 if num_extra_chars > 0 else 0)):
            grid.append([''] * num_cols)

        # Fill the grid column by column
        col = 0
        row = 0
        for char in text:
            grid[row][col] = char
            row += 1
            # Move to next column when we reach the end of current column
            if (col < num_extra_chars and row == num_rows + 1) or (col >= num_extra_chars and row == num_rows):
                col += 1
                row = 0

        # Read the grid row by row to get decrypted text
        decrypted_text = ''
        for row in range(len(grid)):
            for col in range(num_cols):
                if grid[row][col] != '':
                    decrypted_text += grid[row][col]

        return decrypted_text
