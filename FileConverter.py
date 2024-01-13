from PIL import Image
import os

def convert_image_to_image(input_file, output_format):
    try:
        img = Image.open(input_file)
        output_file = f"{os.path.splitext(input_file)[0]}.{output_format}"
        img.save(output_file)
        print(f"File converted and saved as {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

def convert_images_to_pdf(input_files, output_file):
    try:
        images = []
        for file in input_files:
            img = Image.open(file)
            img.convert("RGB")  # Convert image mode to RGB
            images.append(img)

        output_file = f"{os.path.splitext(output_file)[0]}.pdf"
        images[0].save(output_file, save_all=True, append_images=images[1:])
        print(f"Files converted and saved as {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

def main():
    
    input_file = input("Enter the file name/path to convert: ")
    output_format = input("Enter the output format (jpg, png, pdf): ").lower()

    if output_format in ['jpg', 'png']:
        convert_image_to_image(input_file, output_format)
    elif output_format == 'pdf':
        input_files = []
        input_files.append(input_file)
        while True:
            file_name = input("Enter the image file name/path (or type 'done' to finish): ")
            if file_name.lower() == 'done':
                break
            if file_name.lower().endswith(('.jpg', '.png')):
                input_files.append(file_name)
            else:
                print("Invalid file format. Please enter a JPG or PNG file.")

        if input_files:
            output_file = input("Enter the output PDF file name: ")
            convert_images_to_pdf(input_files, output_file)
        else:
            print("No image files provided.")
    else:
        print("Invalid output format. Please enter jpg, png, or pdf.")

if __name__ == "__main__":
    main()
