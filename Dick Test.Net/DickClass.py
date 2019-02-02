class Dick:

    def __init__(self, size, IP, country):
        self.size = size
        self.IP = IP
        self.country = country

def main():

    d = Dick(size = 7, IP = "12.23.55.12", country = "India" )

    d.size += 1

    print(d.size)
    print(d.country)

if __name__ == "__main__":
    main()
