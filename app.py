import streamlit as st
from chatbot import ask_ai, generate_email

# Read company data
with open("company_data.txt", "r", encoding="utf-8") as file:
    company_data = file.read()

st.set_page_config(page_title="Enterprise AI Chatbot", layout="wide")

st.title("🏢 Enterprise AI Chatbot for Business Automation")
st.subheader("TechNova Solutions Pvt. Ltd.")
st.set_page_config(page_title="Enterprise AI Chatbot", layout="wide")


st.write("""
Welcome to TechNova Business Automation Portal.

Helping employees with information, requests, and daily office tasks.
""")

menu = st.sidebar.selectbox(
    "Select Service",
    [
        "Ask Company Questions",
        "Leave Request",
        "IT Support",
        "Meeting Room Booking",
        "Email Generator"
    ]
)

# -------------------------------
# COMPANY CHATBOT
# -------------------------------
if menu == "Ask Company Questions":

    st.header("💬 Company Assistant")

    question = st.text_input("Ask your question")

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            answer = ask_ai(question, company_data)

            st.subheader("Answer")

            st.write(answer)

# -------------------------------
# LEAVE REQUEST
# -------------------------------
elif menu == "Leave Request":

    st.header("📝 Leave Request Form")

    employee = st.text_input("Employee Name")

    leave_type = st.selectbox(
        "Leave Type",
        [
            "Casual Leave",
            "Sick Leave",
            "Paid Leave"
        ]
    )

    start = st.date_input("Start Date")

    end = st.date_input("End Date")

    reason = st.text_area("Reason")

    if st.button("Submit Leave Request"):

        st.success("✅ Leave Request Submitted Successfully")

        st.write("### Leave Details")

        st.write(f"**Employee Name:** {employee}")
        st.write(f"**Leave Type:** {leave_type}")
        st.write(f"**Start Date:** {start}")
        st.write(f"**End Date:** {end}")
        st.write(f"**Reason:** {reason}")

        st.info("Status: Pending HR Approval")
# -------------------------------
# IT SUPPORT
# -------------------------------

elif menu == "IT Support":

    st.header("💻 IT Support Ticket")

    employee = st.text_input("Employee Name")

    department = st.text_input("Department")

    issue = st.selectbox(
        "Issue Type",
        [
            "Laptop Issue",
            "Password Reset",
            "Software Installation",
            "Printer Issue",
            "Internet/Wi-Fi Issue",
            "Email Issue",
            "Other"
        ]
    )

    description = st.text_area("Describe the issue")

    if st.button("Create Ticket"):

        import random

        ticket = "IT-" + str(random.randint(1000,9999))

        st.success("✅ IT Support Ticket Created")

        st.write("### Ticket Details")

        st.write(f"**Ticket ID:** {ticket}")
        st.write(f"**Employee:** {employee}")
        st.write(f"**Department:** {department}")
        st.write(f"**Issue:** {issue}")
        st.write(f"**Description:** {description}")

        st.info("Status: Open")
# -------------------------------
# MEETING ROOM BOOKING
# -------------------------------

elif menu == "Meeting Room Booking":

    st.header("📅 Meeting Room Booking")

    employee = st.text_input("Employee Name")

    room = st.selectbox(
        "Meeting Room",
        [
            "Conference Room A",
            "Conference Room B",
            "Board Room",
            "Training Hall"
        ]
    )

    meeting_date = st.date_input("Meeting Date")

    meeting_time = st.time_input("Meeting Time")

    participants = st.number_input(
        "Number of Participants",
        min_value=1,
        max_value=100,
        value=5
    )

    purpose = st.text_area("Purpose of Meeting")

    if st.button("Book Meeting Room"):

        st.success("✅ Meeting Room Booked Successfully")

        st.write("### Booking Details")

        st.write(f"**Employee Name:** {employee}")
        st.write(f"**Meeting Room:** {room}")
        st.write(f"**Date:** {meeting_date}")
        st.write(f"**Time:** {meeting_time}")
        st.write(f"**Participants:** {participants}")
        st.write(f"**Purpose:** {purpose}")

        st.info("Status: Booking Confirmed")

# -------------------------------
# EMAIL GENERATOR
# -------------------------------

elif menu == "Email Generator":

    st.header("📧 AI Email Generator")

    email_type = st.selectbox(
        "Select Email Type",
        [
            "Leave Request",
            "Work From Home Request",
            "IT Support Request",
            "Meeting Request",
            "General Email"
        ]
    )

    employee = st.text_input("Employee Name")

    recipient = st.text_input("Recipient")

    purpose = st.text_area("Purpose / Details")

    if st.button("Generate Email"):

        answer = generate_email(
            email_type,
            employee,
            recipient,
            purpose
        )

        st.subheader("Generated Email")
        st.write(answer)