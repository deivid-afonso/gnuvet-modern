"""
Responsável por gerar e validar
hash de senha usando bcrypt.
"""

from passlib.context import CryptContext


# bcrypt é padrão da indústria
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Gera hash da senha.
    """

    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    """
    Verifica senha com hash.
    """

    return pwd_context.verify(password, hashed)