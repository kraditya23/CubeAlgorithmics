# Displaying the basic instructions
print("WELCOME to the Rubik's cube solver.")
print("Enter all the faces one by one in the order asked.")
print("Each face should have exactly 9 characters.")
print("The format of your input should be like: 'RBGRBGRBG' (first three colors of the top row, then middle row, then last row)")
print("Valid colors: R = Red, B = Blue, G = Green, Y = Yellow, O = Orange, W = White")

valid_characters = {'R', 'B', 'G', 'Y', 'O', 'W'}

# Function to get and validate input for each face
def get_face_input(face_name):
    while True:
        face = input(f"Enter the {face_name} FACE of the cube: ")
        if len(face) == 9 and all(c.upper() in 'RGBYWO' for c in face):
            return [c.upper() for c in face]
        else:
            print("Invalid input. Make sure the input has exactly 9 characters and only contains 'RBGYOW'.")

# getting the configurations
front_face = get_face_input("FRONT")
back_face = get_face_input("BACK")
left_face = get_face_input("LEFT")
right_face = get_face_input("RIGHT")
top_face = get_face_input("TOP")
bottom_face = get_face_input("BOTTOM")

currentState = [front_face, back_face, left_face, right_face, top_face, bottom_face]

