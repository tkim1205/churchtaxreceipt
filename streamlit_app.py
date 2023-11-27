#import requests
import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
from xhtml2pdf import pisa

st.set_page_config(page_title="Church Tax Recipt", page_icon="⛪")

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err
    
def main():
    st.title("Church Tax Recipt ⛪")

    gmail_sender = st.text_input('Sender Gmail Address')
    gmail_app_pw = st.text_input('Gmail App Password')
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    email_template = st.file_uploader("HTML File - Email Template", type='html', accept_multiple_files=False, disabled=False, label_visibility="visible")
    tax_receipt_template = st.file_uploader("HTML File - Tax Receipt Template", type='html', accept_multiple_files=False, disabled=False, label_visibility="visible")
    excel_email_list = st.file_uploader("Excel File - Email List", type='xlsx', accept_multiple_files=False, disabled=False, label_visibility="visible")

    if st.button("Rewordify"):
        try:
            if excel_email_list is not None and gmail_sender != '':
                with st.spinner('Running...'):
                    df = pd.read_excel(excel_email_list)
                    
                st.success('Done!')

            elif gmail_sender == '':
                st.write("Please enter an Email Address")
            
            elif excel_email_list is None:
                st.write("Please choose a valid Excel file")
                
        except Exception as e:
            st.write("Error occurred 😓")
            st.exception(e)
    
if __name__ == '__main__': 
    main()