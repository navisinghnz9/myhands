def show_menu():
    print("+--------------------------------------------------+")
    print("| SELECT LINE                                      |")
    print("+--------------------------------------------------+")
    print("| 1.  Head Line                                    |")
    print("| 2.  Fate Line                                    |")
    print("| 3.  Destiny Line                                 |")
    print("| 4.  Heart Line                                   |")
    print("| 5.  Life Line                                    |")
    print("| 6.  Sun Line (Apollo Line)                       |")
    print("| 7.  Marriage Lines                               |")
    print("| 8.  Health Line                                  |")
    print("| 9.  Travel Line                                  |")
    print("| 10. Children Line                                |")
    print("| 11. Intuition Line                               |")
    print("| 12. Hepatica Line (Liver Health Line)            |")
    print("| 13. Exit                                         |")
    print("+--------------------------------------------------+")
    print("")

def head_line_info():
    print("\nThe Head Line:")
    print("The Head Line in palmistry represents the person's intellect, thoughts, and decision-making abilities. It usually runs below the Heart Line.")
    print("A clear and deep Head Line indicates a sharp intellect, while a curved one suggests a creative thinker.")

def fate_line_info():
    print("\nThe Fate Line:")
    print("The Fate Line indicates the individual's destiny or the influence of outside forces. It usually runs from the middle of the palm upwards.")
    print("A deep and clear Fate Line suggests a strong sense of purpose, while a faint or broken Fate Line might indicate a less clear life path.")

def destiny_line_info():
    print("\nThe Destiny Line:")
    print("The Destiny Line is often similar to the Fate Line, but it reflects the individual's overall life journey and major life events.")
    print("A well-defined Destiny Line suggests a clear life purpose, while a weak or absent one may suggest a more flexible life course.")

def heart_line_info():
    print("\nThe Heart Line:")
    print("The Heart Line represents emotions, love, and matters of the heart. It typically curves around the top of the palm.")
    print("A deep, long Heart Line suggests someone who is deeply emotional and expressive, while a short Heart Line may indicate a more reserved or practical person.")

def life_line_info():
    print("\nThe Life Line:")
    print("The Life Line surrounds the base of the thumb and curves around the ball of the thumb, indicating the person’s vitality and general life path.")
    print("A deep, long Life Line signifies strength and vitality, while a shorter or broken Life Line can suggest a more challenging path or vulnerability.")

def sun_line_info():
    print("\nThe Sun Line (Apollo Line):")
    print("The Sun Line, or Apollo Line, represents creativity, fame, and success. It is a line that runs vertically from the palm's bottom to the ring finger.")
    print("A clear Sun Line indicates artistic talent or the potential for recognition in one's life, while a faint line suggests a less prominent role in the arts or public life.")

def marriage_lines_info():
    print("\nThe Marriage Lines:")
    print("Marriage Lines are small lines found on the edge of the palm, just below the little finger. These lines are often associated with relationships, particularly significant ones such as marriage.")
    print("Multiple lines can indicate multiple relationships, while a deep line suggests a strong and enduring bond.")

def health_line_info():
    print("\nThe Health Line:")
    print("The Health Line runs parallel to the Life Line and is often associated with the physical well-being of the individual.")
    print("A clear and straight Health Line suggests good health, while a broken or weak Health Line may indicate periods of poor health or challenges.")

def travel_line_info():
    print("\nThe Travel Line:")
    print("The Travel Line is typically found below the little finger and is believed to indicate the frequency of travel or movement in a person’s life.")
    print("A deep, clear Travel Line can suggest a life full of travel or exploration, while a faint or absent line may indicate a more sedentary lifestyle.")

def children_line_info():
    print("\nThe Children Line:")
    print("The Children Line is found just below the little finger, near the edge of the palm, and indicates the number and influence of children in a person's life.")
    print("Multiple lines may suggest several children, while a single, deep line indicates a strong connection with one or more children.")

def intuition_line_info():
    print("\nThe Intuition Line:")
    print("The Intuition Line is believed to represent psychic abilities or intuition. It runs parallel to the Heart Line and may be faint or absent in some individuals.")
    print("A deep Intuition Line suggests strong psychic abilities or intuition, while a faint or absent line indicates a less pronounced ability to sense things intuitively.")

def hepatica_line_info():
    print("\nThe Hepatica Line (Liver Health Line):")
    print("The Hepatica Line, a relatively less-known concept, is thought to represent the individual's liver health and overall vitality.")
    print("A clear and unbroken Hepatica Line suggests strong liver health and a well-balanced internal system, while a broken or faint line may indicate vulnerabilities in health, particularly related to the liver or digestion.")

def main():
    while True:
        show_menu()
        
        # Ask user for their choice
        choice = input("\nEnter your choice (1-13): ")
        
        if choice == '1':
            head_line_info()
        elif choice == '2':
            fate_line_info()
        elif choice == '3':
            destiny_line_info()
        elif choice == '4':
            heart_line_info()
        elif choice == '5':
            life_line_info()
        elif choice == '6':
            sun_line_info()
        elif choice == '7':
            marriage_lines_info()
        elif choice == '8':
            health_line_info()
        elif choice == '9':
            travel_line_info()
        elif choice == '10':
            children_line_info()
        elif choice == '11':
            intuition_line_info()
        elif choice == '12':
            hepatica_line_info()
        elif choice == '13':
            print("\nThank you for using the Palmistry Line Viewer. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option from the menu (1-13).")

if __name__ == "__main__":
    main()

