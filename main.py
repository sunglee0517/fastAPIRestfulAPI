from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import init_db, SessionLocal, Board, Qna, Dataroom, Product, Member
from services import (get_boards, get_board, create_board, update_board, delete_board,
                      get_qnas, get_qna, create_qna, update_qna, delete_qna,
                      get_datarooms, get_dataroom, create_dataroom, update_dataroom, delete_dataroom,
                      get_products, get_product, create_product, update_product, delete_product,
                      get_members, get_member, create_member, update_member, delete_member,
                      BoardCreate, BoardUpdate,
                      QnaCreate, QnaUpdate,
                      DataroomCreate, DataroomUpdate,
                      ProductCreate, ProductUpdate,
                      MemberCreate, MemberUpdate)
from typing import List

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    init_db()

# Boards
@app.get("/company/boards/list", response_model=List[Board])
def read_boards(db: Session = Depends(get_db)):
    return get_boards(db)

@app.get("/company/boards/detail/{board_id}", response_model=Board)
def read_board(board_id: int, db: Session = Depends(get_db)):
    board = get_board(db, board_id)
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board

@app.post("/company/boards/insert", response_model=Board)
def create_board_endpoint(board: BoardCreate, db: Session = Depends(get_db)):
    return create_board(db, board)

@app.post("/company/boards/update", response_model=Board)
def update_board_endpoint(board: BoardUpdate, db: Session = Depends(get_db)):
    return update_board(db, board)

@app.post("/company/boards/delete")
def delete_board_endpoint(board_id: int, db: Session = Depends(get_db)):
    delete_board(db, board_id)
    return {"detail": "Board deleted"}

# Qna
@app.get("/company/qna/list", response_model=List[Qna])
def read_qnas(db: Session = Depends(get_db)):
    return get_qnas(db)

@app.get("/company/qna/detail/{qna_id}", response_model=Qna)
def read_qna(qna_id: int, db: Session = Depends(get_db)):
    qna = get_qna(db, qna_id)
    if qna is None:
        raise HTTPException(status_code=404, detail="Qna not found")
    return qna

@app.post("/company/qna/insert", response_model=Qna)
def create_qna_endpoint(qna: QnaCreate, db: Session = Depends(get_db)):
    return create_qna(db, qna)

@app.post("/company/qna/edit", response_model=Qna)
def update_qna_endpoint(qna: QnaUpdate, db: Session = Depends(get_db)):
    return update_qna(db, qna)

@app.post("/company/qna/delete")
def delete_qna_endpoint(qna_id: int, db: Session = Depends(get_db)):
    delete_qna(db, qna_id)
    return {"detail": "Qna deleted"}

# Dataroom
@app.get("/company/dataroom/list", response_model=List[Dataroom])
def read_datarooms(db: Session = Depends(get_db)):
    return get_datarooms(db)

@app.get("/company/dataroom/detail/{dataroom_id}", response_model=Dataroom)
def read_dataroom(dataroom_id: int, db: Session = Depends(get_db)):
    dataroom = get_dataroom(db, dataroom_id)
    if dataroom is None:
        raise HTTPException(status_code=404, detail="Dataroom not found")
    return dataroom

@app.post("/company/dataroom/upload", response_model=Dataroom)
def create_dataroom_endpoint(dataroom: DataroomCreate, db: Session = Depends(get_db)):
    return create_dataroom(db, dataroom)

@app.post("/company/dataroom/update", response_model=Dataroom)
def update_dataroom_endpoint(dataroom: DataroomUpdate, db: Session = Depends(get_db)):
    return update_dataroom(db, dataroom)

@app.post("/company/dataroom/delete")
def delete_dataroom_endpoint(dataroom_id: int, db: Session = Depends(get_db)):
    delete_dataroom(db, dataroom_id)
    return {"detail": "Dataroom deleted"}

# Product
@app.get("/company/products/list", response_model=List[Product])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@app.get("/company/products/detail/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/company/products/insert", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@app.post("/company/products/update", response_model=Product)
def update_product_endpoint(product: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product)

@app.post("/company/products/delete")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"detail": "Product deleted"}

# Member
@app.get("/company/members/getMemberList", response_model=List[Member])
def read_members(db: Session = Depends(get_db)):
    return get_members(db)

@app.get("/company/members/getMember/{member_id}", response_model=Member)
def read_member(member_id: str, db: Session = Depends(get_db)):
    member = get_member(db, member_id)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.post("/company/members/join", response_model=Member)
def create_member_endpoint(member: MemberCreate, db: Session = Depends(get_db)):
    return create_member(db, member)

@app.post("/company/members/myInfoEdit", response_model=Member)
def update_member_endpoint(member: MemberUpdate, db: Session = Depends(get_db)):
    return update_member(db, member)

@app.post("/company/members/delete")
def delete_member_endpoint(member_id: str, db: Session = Depends(get_db)):
    delete_member(db, member_id)
    return {"detail": "Member deleted"}