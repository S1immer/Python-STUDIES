def image_info(img):
    if 'image_id' in img and 'image_title' in img:
        image_id = img['image_id']
        image_title = img['image_title']
        return f"Image '{image_title}' has id {image_id}"
    else:
        return "Missing image id or title"
