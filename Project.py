movies = {
    1: {"name": "Avengers: Endgame", "price": 250, "seats": 50},
    2: {"name": "KGF Chapter 2", "price": 200, "seats": 40},
    3: {"name": "Inception", "price": 180, "seats": 30},
    4: {"name": "Animal", "price": 220, "seats": 45}
}

def show_movies():
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['name']} - ₹{movie['price']} (Seats left: {movie['seats']})")

def book_ticket():
    show_movies()
    
    choice = int(input("\nEnter movie number to book: "))
    
    if choice not in movies:
        print("Invalid movie selection! Try again.\n")
        return
    
    movie = movies[choice]
    
    print(f"\nYou selected: {movie['name']}")
    print(f"Ticket Price: ₹{movie['price']}")
    
    seats = int(input("How many tickets do you want to book? "))
    
    if seats <= 0:
        print("Seat number must be at least 1!\n")
        return
    
    if seats > movie['seats']:
        print(" Not enough seats available!\n")
        return
    
    total_cost = seats * movie['price']
    movie['seats'] -= seats

    print("\n Ticket Booked Successfully! ")
    print("--------------- TICKET DETAILS ---------------")
    print(f"Movie: {movie['name']}")
    print(f"Tickets: {seats}")
    print(f"Total Price: ₹{total_cost}")
    print("Seat Status Updated.")
    print("----------------------------------------------\n")

def main():
    while True:
        print("===== MOVIE TICKET BOOKING APP =====")
        print("1. Show Movies")
        print("2. Book Ticket")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            show_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thank you for using the Movie Ticket Booking App!")
            break
        else:
            print("Invalid choice! Try again.😭\n")

main()













