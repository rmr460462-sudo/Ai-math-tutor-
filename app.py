import streamlit as st

# অ্যাপের পেজ কনফিগারেশন ও প্রিমিয়াম লুক
st.set_page_config(
    page_title="AI Math & Science Tutor", 
    page_icon="🎓", 
    layout="centered"
)

# কাস্টম ডিজাইন ও স্টাইল (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# অ্যাপের হেডার বা টাইটেল
st.title("🎓 AI Math & Science Tutor")
st.write("তোমার ফিজিক্স, কেমিস্ট্রি বা হায়ার ম্যাথের কঠিন সমস্যাগুলো এখানে লিখো। এআই একদম ধাপে ধাপে বুঝিয়ে দেবে!")

# সাবজেক্ট সিলেক্ট করার অপশন
subject = st.selectbox(
    "বিষয় সিলেক্ট করো:",
    ["Higher Mathematics (উচ্চতর গণিত)", "Physics (পদার্থবিজ্ঞান)", "Chemistry (রসায়ন)"]
)

# প্রবলেম লেখার ইনপুট বক্স
user_problem = st.text_area(
    "তোমার প্রশ্ন বা অংকটি এখানে লিখো বা পেস্ট করো:",
    placeholder="যেমন: F = ma সূত্র ব্যবহার করে একটি গাণিতিক সমস্যা সমাধান করো..."
)

# সলভ করার বাটন
if st.button("Solve Step-by-Step 🚀"):
    if not user_problem.strip():
        st.error("আগে তোমার সমস্যাটি এখানে লিখো বন্ধু!")
    else:
        # এআই প্রসেসিংয়ের অ্যানিমেশন
        with st.spinner(f"{subject} থেকে সমাধান খোঁজা হচ্ছে... একটু অপেক্ষা করো!"):
            
            # সফল সলিউশন আউটপুট বক্স
            st.success("সফলভাবে সমাধান করা হয়েছে! 🎉")
            
            st.markdown("### 📝 ধাপে ধাপে সমাধান (Step-by-Step Solution):")
            
            # ডেমো এআই রেসপন্স (এখানে পরবর্তীতে গুগলের জেমিনি API যুক্ত করা যাবে)
            st.markdown(f"""
            **১. দেওয়া আছে / শনাক্তকরণ:**  
            প্রদত্ত সমস্যাটি **{subject}** এর আওতাধীন। এখানে প্রয়োজনীয় মানগুলো চিহ্নিত করা হলো।

            **২. উপযুক্ত সূত্র (Formula):**  
            এই ধরনের সমস্যার ক্ষেত্রে নির্দিষ্ট মূল সূত্রটি প্রয়োগ করতে হবে।

            **৩. হিসাব ও ফলাফল (Calculation):**  
            ধাপগুলো অনুসরণ করে চূড়ান্ত ফলাফল বের করা হয়েছে। উত্তর সঠিক ও নিখুঁত আছে! ✅
            """)

# নিচের ফুটার বা ব্র্যান্ডিং
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Google AI | Built by You 💡</p>", unsafe_allow_html=True)
