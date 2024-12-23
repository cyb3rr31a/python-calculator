# Calculator Application (Tkinter)

This is a simple and visually appealing calculator application built using Python's Tkinter library. It provides basic arithmetic functionality (addition, subtraction, multiplication, and division) with a modern design.

---

## Features

- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear Button**: Easily reset the calculator display.
- **Error Handling**: Displays "Error" for invalid input (e.g., division by zero).
- **Responsive Design**: Buttons and display adjust with padding for a clean and modern appearance.
- **Dark Theme**: The calculator uses a dark color scheme with vibrant button colors for better visual appeal.

---

## Screenshot

![Calculator Screenshot](#)
> (Add an image of the calculator here)

---

## How to Run

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the project folder.
3. Run the following command:
   ```bash
   python calculator.py
   ```
4. The calculator window will open, and you can start using it.

---

## Code Structure

### `calculator.py`
- **Import Statements**: Imports the Tkinter library for GUI development.
- **Root Window**: Creates the main application window with a dark theme.
- **Display**: Adds a text input field where calculations are displayed.
- **Buttons**: Creates number buttons, operator buttons, and functional buttons (Clear and Equals).
- **Functions**:
  - `button_click(value)`: Appends the clicked button's value to the display.
  - `clear_display()`: Clears the display.
  - `calculate()`: Evaluates the math expression entered in the display and handles errors.
- **Styling**: Adds consistent styling to buttons and display for a modern look.

---

## Design Details

### Colors
- **Background**: `#2e3f4f` (dark blue-gray)
- **Button Colors**:
  - Default: `#4e5d6c` (dark gray)
  - Operators: `#ff9f43` (orange)
  - Equals: `#5cb85c` (green)
  - Clear: `#d9534f` (red)
- **Hover Effect**: Buttons light up slightly when hovered over.

### Fonts
- **Display**: Arial, size 24 (large and readable).
- **Buttons**: Arial, size 18 (consistent and clean).

---

## Future Enhancements

Here are some ideas for improving the calculator:
- **Advanced Operations**: Add square root, percentage, or exponentiation.
- **Backspace Button**: Allow users to delete the last character entered.
- **Themes**: Add light mode or custom theme options.
- **History**: Display previous calculations in a scrollable area.

---

## License

This project is open-source and available under the MIT License.

---

## Author

- **My Name**
- GitHub: [cyb3rr31a](https://github.com/cyb3rr31a)

Feel free to fork and contribute to this project!
