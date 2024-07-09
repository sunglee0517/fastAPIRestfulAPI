# services.py
from sqlalchemy.orm import Session
from models import Board, Qna, Dataroom, Product, Member
from pydantic import BaseModel 
from typing import List, Optional

# Board
class BoardCreate(BaseModel):
    title: str
    content: str
    author: str

class BoardUpdate(BaseModel):
    no: int
    title: str
    content: str
    author: str

def get_boards(db: Session) -> List[Board]:
    return db.query(Board).all()

def get_board(db: Session, board_id: int) -> Board:
    return db.query(Board).filter(Board.no == board_id).first()

def create_board(db: Session, board: BoardCreate) -> Board:
    db_board = Board(**board.dict())
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def update_board(db: Session, board: BoardUpdate) -> Board:
    db_board = db.query(Board).filter(Board.no == board.no).first()
    if db_board:
        for key, value in board.dict().items():
            setattr(db_board, key, value)
        db.commit()
        db.refresh(db_board)
    return db_board

def delete_board(db: Session, board_id: int):
    db_board = db.query(Board).filter(Board.no == board_id).first()
    if db_board:
        db.delete(db_board)
        db.commit()

# Qna
class QnaCreate(BaseModel):
    title: str
    content: str
    author: str

class QnaUpdate(BaseModel):
    qno: int
    title: str
    content: str
    author: str

def get_qnas(db: Session) -> List[Qna]:
    return db.query(Qna).all()

def get_qna(db: Session, qna_id: int) -> Qna:
    return db.query(Qna).filter(Qna.qno == qna_id).first()

def create_qna(db: Session, qna: QnaCreate) -> Qna:
    db_qna = Qna(**qna.dict())
    db.add(db_qna)
    db.commit()
    db.refresh(db_qna)
    return db_qna

def update_qna(db: Session, qna: QnaUpdate) -> Qna:
    db_qna = db.query(Qna).filter(Qna.qno == qna.qno).first()
    if db_qna:
        for key, value in qna.dict().items():
            setattr(db_qna, key, value)
        db.commit()
        db.refresh(db_qna)
    return db_qna

def delete_qna(db: Session, qna_id: int):
    db_qna = db.query(Qna).filter(Qna.qno == qna_id).first()
    if db_qna:
        db.delete(db_qna)
        db.commit()

# Dataroom
class DataroomCreate(BaseModel):
    title: str
    content: str
    author: str
    datafile: str

class DataroomUpdate(BaseModel):
    dno: int
    title: str
    content: str
    author: str
    datafile: Optional[str]

def get_datarooms(db: Session) -> List[Dataroom]:
    return db.query(Dataroom).all()

def get_dataroom(db: Session, dataroom_id: int) -> Dataroom:
    return db.query(Dataroom).filter(Dataroom.dno == dataroom_id).first()

def create_dataroom(db: Session, dataroom: DataroomCreate) -> Dataroom:
    db_dataroom = Dataroom(**dataroom.dict())
    db.add(db_dataroom)
    db.commit()
    db.refresh(db_dataroom)
    return db_dataroom

def update_dataroom(db: Session, dataroom: DataroomUpdate) -> Dataroom:
    db_dataroom = db.query(Dataroom).filter(Dataroom.dno == dataroom.dno).first()
    if db_dataroom:
        for key, value in dataroom.dict().items():
            setattr(db_dataroom, key, value)
        db.commit()
        db.refresh(db_dataroom)
    return db_dataroom

def delete_dataroom(db: Session, dataroom_id: int):
    db_dataroom = db.query(Dataroom).filter(Dataroom.dno == dataroom_id).first()
    if db_dataroom:
        db.delete(db_dataroom)
        db.commit()

# Product
class ProductCreate(BaseModel):
    cate: str
    pname: str
    pcontent: str
    img1: str
    img2: str
    img3: str

class ProductUpdate(BaseModel):
    pno: int
    cate: str
    pname: str
    pcontent: str
    img1: str
    img2: str
    img3: str

def get_products(db: Session) -> List[Product]:
    return db.query(Product).all()

def get_product(db: Session, product_id: int) -> Product:
    return db.query(Product).filter(Product.pno == product_id).first()

def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: ProductUpdate) -> Product:
    db_product = db.query(Product).filter(Product.pno == product.pno).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.pno == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()

# Member
class MemberCreate(BaseModel):
    id: str
    pw: str
    name: str
    birth: str
    email: str
    tel: Optional[str]
    addr1: Optional[str]
    addr2: Optional[str]
    postcode: Optional[str]

class MemberUpdate(BaseModel):
    id: str
    pw: str
    name: str
    birth: str
    email: str
    tel: Optional[str]
    addr1: Optional[str]
    addr2: Optional[str]
    postcode: Optional[str]

# Member (continued)
def get_members(db: Session) -> List[Member]:
    return db.query(Member).all()

def get_member(db: Session, member_id: str) -> Member:
    return db.query(Member).filter(Member.id == member_id).first()

def create_member(db: Session, member: MemberCreate) -> Member:
    db_member = Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db: Session, member: MemberUpdate) -> Member:
    db_member = db.query(Member).filter(Member.id == member.id).first()
    if db_member:
        for key, value in member.dict().items():
            setattr(db_member, key, value)
        db.commit()
        db.refresh(db_member)
    return db_member

def delete_member(db: Session, member_id: str):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
