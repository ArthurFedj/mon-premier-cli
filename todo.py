import sys

def main():
    if len(sys.argv) < 2:
        print("Usage : python todo.py [ajouter|liste]")
        return
    commande = sys.argv[1]
    if commande == "ajouter":
        with open("taches.txt", "a") as f:
            f.write(sys.argv[2] + "\n")
    elif commande == "liste":
        with open("taches.txt", "r") as f:
            print(f.read())

if __name__ == "__main__":
    main()
