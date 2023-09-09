import codecs

def main() -> None:
    user_input: str = input('Your Message: ')
    
    encoded: str = codecs.encode(user_input, 'rot13')
    print(f'Encrypted Message: {encoded}')
    
    decoded: str = codecs.decode(encoded, 'rot13')
    print(f'Decrypted Message: {decoded}')

if __name__ == '__main__':
    main()