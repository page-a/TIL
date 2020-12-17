import os
def get_dir_path_product(product):
    """
    for:
        파일 읽고 저장할 때 계속 경로복사하는 시간 단축
    Args:
        product(str): 상품 이름
    Returns:
        str: product의 data 경로
    Todo:
        경로 없을 때 만들어 주는 기능
       
    """
    path = "G:\공유 드라이브\속성사전\\Data"
    for dir_path, dir_names, file_names in os.walk(path):
        if product in dir_names:
            return dir_path + '\\'+product