# models.py
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

DATABASE_URL = "mariadb+mariadbconnector://root:1234@localhost:3307/company"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Board(Base):
    __tablename__ = 'board'
    no = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=False)
    resdate = Column(DateTime, default=datetime.datetime.utcnow)
    hits = Column(Integer, default=0)

class Qna(Base):
    __tablename__ = 'qna'
    qno = Column(Integer, primary_key=True, index=True)
    lev = Column(Integer, default=0)
    parno = Column(Integer)
    title = Column(String(255))
    content = Column(Text)
    author = Column(String(255))
    resdate = Column(DateTime, default=datetime.datetime.utcnow)
    hits = Column(Integer, default=0)

class Dataroom(Base):
    __tablename__ = 'dataroom'
    dno = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)
    author = Column(String(255))
    datafile = Column(String(255))
    resdate = Column(DateTime, default=datetime.datetime.utcnow)
    hits = Column(Integer, default=0)

class Product(Base):
    __tablename__ = 'product'
    pno = Column(Integer, primary_key=True, index=True)
    cate = Column(String(255))
    pname = Column(String(255))
    pcontent = Column(Text)
    img1 = Column(String(255))
    img2 = Column(String(255))
    img3 = Column(String(255))
    resdate = Column(DateTime, default=datetime.datetime.utcnow)
    hits = Column(Integer, default=0)

class Member(Base):
    __tablename__ = 'member'
    id = Column(String(50), primary_key=True, index=True)
    pw = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)
    birth = Column(Date, nullable=False)
    email = Column(String(255), nullable=False)
    tel = Column(String(20))
    addr1 = Column(String(255))
    addr2 = Column(String(255))
    postcode = Column(String(10))
    regdate = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
