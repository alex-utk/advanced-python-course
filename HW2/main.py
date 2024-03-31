from customlatexalexutk import generate_table, generate_image, \
    generate_graphics_path, tex_file_wrapper


if __name__ == '__main__':
    table = [
        ['a', 'bbbbb', 'c', 'a'],
        ['mmg', 'ad', 'yo', 'text'],
        ['aa', 'fasf', 'tat', 'fasfa'],
        ['gg', 'ag', 'aa', 'asfa'],
    ]
    image_path_1 = './latex_imgs/cool.jpg'
    image_path_2 = './latex_imgs/cat.jpg'
    
    folder_1, image_markup_1 = generate_image(image_path_1)
    folder_2, image_markup_2 = generate_image(image_path_2)
    
    table_markup = generate_table(table, 'c')
    graphics_path_string = generate_graphics_path(folder_1, folder_2)
    
    final_markup = tex_file_wrapper(graphics_path_string, image_markup_1, table_markup, image_markup_2)
    
    with open('task_1.tex', 'wt') as tex_file:
        tex_file.write(final_markup)