def urutNumber(input):
    input.sort(reverse=False)
    return input

def repeatCharacter(input):
    hasil = ""
    for i in input:
        hasil += i * 2
    return hasil

def Terbilang(input):
    
      angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
                "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
      Hasil = " "
      n = int(input)
      if n>=0 and n <= 11:
        Hasil = angka[n]
      elif n <20:
        Hasil = Terbilang(n-10) + " Belas"
      elif n <100:
            Hasil = Terbilang (n/10) + " Puluh " + Terbilang (n%10)
      elif n <200:
          Hasil = " Seratus " + Terbilang (n-100)
      elif n <1000:
          Hasil = Terbilang (n/100) + " Ratus " + Terbilang (n%100)
      elif n <2000:
          Hasil = " Seribu " + Terbilang (n-1000)
      elif n <1000000:
          Hasil = Terbilang (n/1000) + " Ribu " + Terbilang (n%1000)
      elif n <10000000:
          Hasil = Terbilang (n/1000000) + " Juta " + Terbilang (n%1000000)
      else: Hasil = "Maksimal 9.000.000"
      return Hasil

if __name__ == "__main__":
    while True:
        print("=====================")
        print("Choose your function")
        print("1. Ordering Number")
        print("2. Repeating")
        print("3. Int to String")
        print("4. Exit")
        print("=====================")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            input_list = input("Input your numbers separated by commas: ").split(",")
            input_list = [int(num) for num in input_list]
            result = urutNumber(input_list)
            print("Here is your sorted number:")
            print(result)

        elif choice == "2":
            input_string = input("Input your string: ")
            result = repeatCharacter(input_string)
            print("Here is your repeated string:")
            print(result)
            

        elif choice == "3":
            input_number = int(input("Input your number: "))
            result = Terbilang(input_number)
            print("Here is your number in text:")
            print(result)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")