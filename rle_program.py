from console_gfx import ConsoleGfx

# converts integers to hexadecimals
def to_hex_string(data):
    hex_string = ""
    for num in data:
        hex_string += hex(num)[2:]  # prints from the right of the prefix "0x"
    # Test Case #1: print(to_hex_string([3, 15, 6, 4]))  # should return 3f64
    return hex_string

# returns the number of runs
def count_runs(flat_data):
    runs = 1
    zeta = 0
    current = flat_data[0]  # sets current to flat_data index 0
    for num in flat_data:
        if current == num:
            zeta += 1
            if zeta >= 15:  # sets boundary to reset runs
                runs += 1
                zeta = 0
                continue
        elif current != num:
            current = num
            runs += 1
            zeta = 0
    # Test Case #2: print(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]))

    return runs

# returns repetitions, repeated num
def encode_rle(flat_data):
    rep = []  # empty list data is being input
    zeta = 0
    current = flat_data[0]  # sets current to 1st value in flat_data

    for num in flat_data:  # for loop that iterates through the list outputting the number of times a number appears and the number
        if current == num:
            zeta += 1
            if zeta >= 15:
                beta = [zeta, current]
                rep.extend(beta)
                zeta = 0
        else:
            beta = [zeta, current]
            rep.extend(beta)
            current = num
            zeta = 1

    beta = [zeta, current]  # stores iterations , num
    rep.extend(beta)

    # Test Case #3: print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4])  ) # should return [3, 15, 6, 4]

    return rep

# adds repetitions
def get_decoded_length(rle_data):
    alpha = sum(rle_data[0::2])  # adds # of times a value repeats for each number
    # Test Case #4: print(get_decoded_length([3, 15, 6, 4])) # should return 9
    return alpha


def decode_rle(rle_data):
    rep = []
    current = rle_data[1]  # Starts with second element in the list
    alpha = rle_data[1::2]  # iterates by 2 starting at index 1
    bob = 0
    for i in range(0, len(rle_data), 2):
        zeta = rle_data[i]
        num = alpha[bob]
        bob += 1
        if num != current:
            current = num
        rep.extend([num] * zeta)  # multiplies list num by zeta resulting in num in list being repeated zeta times then adds it to list rep []
    return rep
    # Test Case #5 print(decode_rle([3, 15, 6, 4]))  # should return [15, 15, 15, 4, 4, 4, 4, 4, 4]


def string_to_data(data_string):
    wallie = []
    for num in data_string:
        if num.isdigit():  # if the item in the string is a number it returns it as an integer
            wallie.append(int(num))
        else:  # if the item in the string is a hexadecimal it returns it as an integer equivalent
            zeta = int(ord(num.upper()) - ord('A') + 10)
            wallie.append(zeta)
    return wallie

    # Test Case #6: print(string_to_data("3f64"))  # should return [3, 15, 6, 4]


def to_rle_string(rle_data):
    hex_string = ""

    current = rle_data[0]  # starts current at the 1st element in rle_data
    zeta = 0
    for num in rle_data:  # iterates through the list and returns the number with the one to the right followed by a delimiter

        if current == num:
            hex_string += f"{current}"  # adds the current num to hex_string
            continue
        elif current != num:
            zeta += 1  # updates zeta

            if zeta == 1:  # adds prev_num to hex_string followed by a delimiter
                prev_num = num
                hex_string += f"{prev_num}:"
                prev_num = 0
            elif zeta == 2: 
                current = num
                hex_string += f"{current}:"

            elif zeta == 3:  # adds two digit numbers such as 15 to hex_string
                current = num
                hex_string += f"{current}"

                zeta = 0  # resets zeta
    return hex_string[:-1]

# print(to_rle_string([1,9,1,4,15,1,15,1,6,1]))  # should return "19:14:151:151:61"


def string_to_rle(rle_string):
    wallie = []
    rle_string = rle_string.split(':')  # splits the string by the ":" delimiter

    for num in rle_string:
        alpha = 0
        if len(num) == 3:  # if len is 3 the function separates the num
            for i in num:
                if i == num[0] and alpha == 0:
                    alpha += 1
                    continue
                if i >= str(0) and i <= str(9) and alpha == 1:

                    wallie.append(int(i) + 10)  # skips the 1st and adds 10 to the second
                    alpha += 1
                elif i >= str(0) and i <= str(9):
                    wallie.append(int(i))
                else:
                    zeta = int(ord(i.upper()) - ord('A') + 10)
                    wallie.append(zeta)  # hexadecimal conversion added to list
                    alpha += 1
        if len(num) == 2:  # if len is 2 the function returns the individual integers
            for i in num:
                wallie.append(int(i))

    return wallie


# print(string_to_rle("19:14:151:151:61"))  # should return [1, 9, 1, 4, 15, 1, 15, 1, 6, 1]


# Display welcome message
print("Welcome to the RLE image encoder!\n\nDisplaying Spectrum Image:")

# Display spectrum message
ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

image_data = None

def main():
    while True:
        # print all the menu options

        print("\n \nRLE Menu \n -------- \n 0. Exit \n 1. Load File \n 2. Load Test Image \n 3. Read RLE String \n 4. Read RLE Hex String \n 5. Read Data Hex String \n 6. Display Image \n 7. Display RLE String \n 8. Display Hex RLE Data \n 9. Display Hex Flat Data\n")

        # prompt user for menu option

        option = int(input("Select a Menu Option: "))



        if option == 0:
            break

        elif option == 1:
            # prompt the filename entered by user
            filename = input("Enter name of file to load: ")
            # store ConsoleGfx.load_file(filename) in image_data_variable

            image_data = ConsoleGfx.load_file(filename)

        elif option == 2:
            # store ConsoleGfx.test_image
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.\n")

        elif option == 3:
            image_data = input("Enter an RLE string to be decoded: ")  # user input stored in image_data

        elif option == 4:
            image_data = input("Enter the hex string holding RLE data: ")

        elif option == 5:
            image_data = input("Enter the hex string holding flat data: ")

        elif option == 6:
            # display the image_data using ConsoleGfx.display_image()
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)

        elif option == 7:
            res = string_to_data(image_data)
            print(f"RLE representation: {to_rle_string(res)}")

        elif option == 8:
            result = string_to_rle(image_data)
            print(f"RLE hex values: {to_hex_string(result)}")  # takes the result of string_to_rle and converts it to_hex_string

        elif option == 9:
            eric = string_to_rle(image_data)  # stores the result of image data when input to string_to_data
            steve = decode_rle(eric)

            print(f"Flat hex values: {to_hex_string(steve)}")


if __name__ == "__main__":
    main()
