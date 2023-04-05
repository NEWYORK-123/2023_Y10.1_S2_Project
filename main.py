#  Võ Thanh Tân
#     ~~~~~~ Library App ~~~~~~
#
#       Scan book ISBN
#           If the book is loaned out then return it
#           Display Book Details
#           Scan Member ID
#           Display Member details
#           Get the date
#       
#       Add 7days to date as Duedate
#       Add Date, Duedate, Book ISBN and Member ID to loan table
#
#       Display a message eg. Duedate
#
#       Returning a book:
#           Get the date 
#           find the loan ID where the member ID and the book ISBN is and not returned
#           input the returndate into the loan table

import datetime
import os 
import sqlite3
import streamlit as st


def get_date():
    ''' Get the current date to be used as both the borrow and return date '''
    thedate = datetime.datetime.now().strftime("%Y%m%d")
    return thedate

def Calc_Duedate():
    duedate = datetime.datetime.now() + datetime.timedelta(days=7)
    duedate = duedate.strftime("%Y%m%d")
    return duedate

def Return_theBook(isbn):
    # check if the isbn is in the loan table without a return date
    #save return date in the database.
    if isbn:
        st.title("The book has been returned")
        st.title("Võ Thanh Tân")
        thedate = get_date()
        st.title(f"{thedate}")
    else:
        print("404 error ISBN not found")

    print("")


def loan_book(member_ID, book_isbn):
    ''' This function controls how a book is borrowed '''
    if member_ID and book_isbn:
        Thisdate = get_date()
        Duedate = Calc_Duedate()
        display_Duedate = datetime.datetime.now() + datetime.timedelta(days=7)
        display_Duedate = display_Duedate.strftime("%Y%m%d")
        st.title("The book is due on:")
        st.title(f'{display_Duedate}')
        #send data to be written in DB
    else:
        st.title("member ID or ISBN was blank")


def write_to_database(return_date, isbn):
    if return_date:
        query = f'SELECT returndate from loanTable WHERE book_isbn={isbn}'
    elif isbn and member_id and borrow_date and due_date:
        query = f'SELECT returndate from loanTable WHERE book_isbn={isbn}'
    else:
        ...
    try:
        sqliteConnection = sqlite3.connect('Library.db')
        cursor = sqliteConnection.cursor()
        query = f'SELECT * from bookTable WHERE book_isbn={isbn}'
        cursor.execute(query)
        output = cursor.fetchone()[1]
        cursor.close()
    except sqlite3.Error as error:
        print('Error occurred - ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def create_UI():
    '''Creates the UI to allow users to interact with our program'''
    st.title("Library App")
    st.write("Võ Thanh Tân")
    member_ID = st.number_input(label="Member ID", value=0,step=1)
    book_isbn = st.number_input(label="Book ISBN", value=0,step=1)
    borrow_button_pressed = st.button("Borow Book")
    return_button_pressed = st.button("Return Book")
    if borrow_button_pressed:
        loan_book(member_ID,book_isbn)
    # output
create_UI()