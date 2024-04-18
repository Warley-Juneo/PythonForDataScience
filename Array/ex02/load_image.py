from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> list:
    """ Given a path to an image, return a 3D list of the RGB values of
    the image.

    Args:
        path (str): The path to the image.

    Returns:
        list: A 3D list of RGB values.
    """

    try:
        im = Image.open(path)
    except UnidentifiedImageError as e:
        print(f"Error: {e}")
        return []
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []

    im_rgb = im.convert("RGB")
    rgb_list = []
    for y in range(im.height):
        row = []
        for x in range(im.width):
            r, g, b = im_rgb.getpixel((x, y))
            row.append([r, g, b])
        rgb_list.append(row)

    return rgb_list


if __name__ == "__main__":
    print(ft_load("fausto.jpg"))
