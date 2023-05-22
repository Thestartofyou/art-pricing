def calculate_art_price(artist_reputation, medium, size):
    base_price = 1000  # Set a base price for the art
    
    # Calculate reputation factor
    if artist_reputation == "high":
        reputation_factor = 1.5
    elif artist_reputation == "medium":
        reputation_factor = 1.2
    else:
        reputation_factor = 1.0
    
    # Calculate medium factor
    if medium == "oil":
        medium_factor = 1.3
    elif medium == "acrylic":
        medium_factor = 1.1
    else:
        medium_factor = 1.0
    
    # Calculate size factor
    if size == "small":
        size_factor = 0.8
    elif size == "medium":
        size_factor = 1.0
    else:
        size_factor = 1.2
    
    # Calculate the final price
    price = base_price * reputation_factor * medium_factor * size_factor
    
    return price


# Example usage
artist_reputation = input("Enter artist reputation (high/medium/low): ")
medium = input("Enter art medium (oil/acrylic/other): ")
size = input("Enter art size (small/medium/large): ")

art_price = calculate_art_price(artist_reputation, medium, size)
print("The price of the art is $", art_price)
