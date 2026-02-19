def calculate_match_score(listing, buyer):
    score = 0

    if listing.price <= buyer.max_price:
        score += 40

    if listing.location == buyer.preferred_location:
        score += 30

    if listing.bedrooms >= buyer.min_bedrooms:
        score += 20

    # Bonus for square footage
    if listing.square_feet > 1500:
        score += 10

    return score
