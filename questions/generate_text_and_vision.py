import base64
import os

def encode_image(image_path):
    dataurl = ''
    with open(image_path, 'rb') as image_file:
        base64_utf8_str = base64.b64encode(image_file.read()).decode('utf-8')
        ext     = image_path.split('.')[-1]
        dataurl = f'data:image/{ext};base64,{base64_utf8_str}'
    return dataurl

def get_image_text(image_text_path):
    text = ''
    with open(image_text_path, 'r') as text_file:
        text = text_file.read()
    return text

def generate_prompts(image_folder, image_text_folder):
    vision_prompts = list()

    # Getting the base64 string
    image_list = os.listdir(image_folder)
    for image in image_list:
        prefix = image.split('.')[0]
        image_text_file = prefix + '.txt'
        image_text_path = os.path.join(image_text_folder, image_text_file)
        image_text = get_image_text(image_text_path)

        image_path = os.path.join(image_folder, image)
        base64_image_url = encode_image(image_path)

        if base64_image_url == '':
            print('Failed to encode image! Exiting')
            exit(-1)

        image_content =  [
            {
                "type": "text",
                "text": image_text,
            },
            {
                "type": "image_url",
                "image_url": {
                    "url":  base64_image_url
                },
            },
        ]
        vision_prompts.append({"role": "user", "content": image_content})

    return vision_prompts
