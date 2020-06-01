import os
from shutil import copyfile

def prepare(training_path, gallery_path, query_path, output_path):
    if not os.path.isdir(output_path):  os.mkdir(output_path)

    _prepare(training_path, os.path.join(output_path, 'train'))
    print('training_path >> ', training_path)
    _prepare(gallery_path, os.path.join(output_path, 'gallery'))
    print('gallery_path >> ', gallery_path)
    _prepare(query_path, os.path.join(output_path, 'query'))
    print('query_path >> ', query_path)

def _prepare(src_path, dst_path):
    query_path = src_path
    query_save_path = dst_path

    if not os.path.isdir(query_save_path):
        os.mkdir(query_save_path)

    for root, dirs, files in os.walk(query_path, topdown=True):
        for name in files:
            if not name[-3:]=='jpg':
                continue

            ID  = name.split('_')[0]

            src_path = query_path + '/' + name
            dst_path = query_save_path + '/' + ID

            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)

            copyfile(src_path, dst_path + '/' + name)


if __name__ == '__main__':
    train_path   = '../VisDA2020/devkit/challenge_datasets/personX/image_train'
    gallery_path = '../VisDA2020/devkit/challenge_datasets/target_validation/image_gallery'
    query_path = '../VisDA2020/devkit/challenge_datasets/target_validation/image_query'
    output_path = './data/VisDA'
    prepare(train_path, gallery_path, query_path, output_path)