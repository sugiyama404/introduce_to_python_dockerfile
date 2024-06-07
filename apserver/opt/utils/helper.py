import bcrypt

def generate_password_hash(password: str)->str:
    """
    パスワードをハッシュ化して返す関数

    Args:
        password (str): ハッシュ化したいパスワード

    Returns:
        str: 生成されたハッシュパスワード
    """
    # ランダムなソルトを生成
    salt = bcrypt.gensalt()
    # パスワードとソルトを使用してハッシュを生成
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def check_password_hash(password: str, hashed_password: str)->bool:
    """
    ハッシュされたパスワードと元のパスワードを照合する関数

    Args:
        password (str): 検証したいパスワード
        hashed_password (str): 照合するハッシュパスワード

    Returns:
        bool: パスワードが一致する場合は True、そうでない場合は False
    """
    # ハッシュされたパスワードと元のパスワードを比較
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
