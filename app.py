from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """
    Generate a random password based on user preferences.
    
    Args:
        length (int): Desired password length
        use_uppercase (bool): Whether to include uppercase letters
        use_lowercase (bool): Whether to include lowercase letters
        use_numbers (bool): Whether to include numbers
        use_symbols (bool): Whether to include special symbols
    
    Returns:
        str: Generated password
    """
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    number_chars = string.digits
    symbol_chars = string.punctuation
    
    # Create the character pool based on user preferences
    char_pool = ''
    if use_uppercase:
        char_pool += uppercase_chars
    if use_lowercase:
        char_pool += lowercase_chars
    if use_numbers:
        char_pool += number_chars
    if use_symbols:
        char_pool += symbol_chars
    
    # Ensure at least one character set is selected
    if not char_pool:
        return "Please select at least one character type"
    
    # Generate the password
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handle password generation requests."""
    try:
        # Get user preferences from the request
        data = request.get_json()
        length = int(data.get('length', 12))
        use_uppercase = data.get('uppercase', False)
        use_lowercase = data.get('lowercase', False)
        use_numbers = data.get('numbers', False)
        use_symbols = data.get('symbols', False)
        
        # Validate length
        if length < 4 or length > 128:
            return jsonify({'error': 'Password length must be between 4 and 128 characters'}), 400
        
        # Generate password
        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )
        
        return jsonify({'password': password})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 