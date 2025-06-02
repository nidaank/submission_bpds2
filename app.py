import streamlit as st
import pandas as pd
import joblib

# --- Load model dan encoder ---
model = joblib.load("model/rf_model2.pkl")
encoder = joblib.load("model/onehot_encoder2.pkl")

important_categorical = ['Application_mode', 'Course', 'Gender', 'Previous_qualification']
important_numerical = [
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date', 'Scholarship_holder',
    'Age_at_enrollment', 'Debtor'
]

# === Fungsi untuk encoding input ===
def encode_input(df, encoder, cat_cols, num_cols):
    X_cat = encoder.transform(df[cat_cols])
    cat_names = encoder.get_feature_names_out(cat_cols)
    X_num = df[num_cols].reset_index(drop=True)
    X_ready = pd.concat([X_num, pd.DataFrame(X_cat, columns=cat_names, index=X_num.index)], axis=1)
    return X_ready

# === Sidebar ===
st.sidebar.title("Submission Akhir")
st.sidebar.markdown("### Menyelesaikan Permasalahan Institusi Pendidikan")
st.sidebar.markdown("[Klik di sini untuk mengunduh dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)")  # Ganti dengan URL aslinya
st.sidebar.markdown("© 2025 Nida'an Khafiyya")

# === Judul Utama ===
st.title("Prediksi Dropout Mahasiswa")
st.markdown("Silakan isi form di bawah untuk memprediksi apakah mahasiswa berpotensi dropout atau tidak.")

# === Form di tengah halaman ===
with st.form("prediction_form"):
    st.subheader("Input Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        app_mode = st.selectbox("Application Mode", ["1st Phase - General Contingent",
            "1st Phase - Special Contingent (Azores Island)",
            "1st Phase - Special Contingent (Madeira Island)",
            "2nd Phase - General Contingent", "3rd Phase - General Contingent",
            "Ordinance No. 612/93", "Ordinance No. 854-B/99",
            "International Student (Bachelor)", "Over 23 Years Old",
            "Transfer", "Change of Course", "Holders of Other Higher Courses",
            "Short Cycle Diploma Holders",
            "Technological Specialization Diploma Holders",
            "Change of Institution/Course",
            "Change of Institution/Course (International)"],
            help="Metode aplikasi yang dipakai mahasiswa")
        course = st.selectbox("Course", ["Biofuel Production Technologies",
            "Animation and Multimedia Design", "Social Service (Evening Attendance)",
            "Agronomy", "Communication Design", "Veterinary Nursing", "Informatics Engineering",
            "Equinculture", "Management", "Social Service", "Tourism", "Nursing", "Oral Hygiene",
            "Advertising and Marketing Management", "Journalism and Communication", "Basic Education",
            "Management (Evening Attendance)"],
            help='Kelas yang diambil mahasiswa')
        gender = st.selectbox("Gender", ["Male", "Female"])
        prev_qual = st.selectbox("Previous Qualification", ["Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", "10th Year of Schooling - Not Completed", "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
            "11th Year of Schooling - Not Completed", "Frequency of Higher Education", "Higher Education - Bachelor's Degree", "Higher Education - Degree (1st Cycle)", "Higher Education - Degree", "Higher Education - Master (2nd Cycle)",
            "Higher Education - Master's", "Secondary Education - 12th Year of Schooling or Eq.", "Professional Higher Technical Course", "Technological Specialization Course", "Other - 11th Year of Schooling"],
            help='Kualifikasi yang diperoleh siswa sebelum mendaftar di pendidikan tinggi.')
        age = st.slider("Age at Enrollment", 17, 70, 20)

    with col2:
        approved_2nd = st.number_input("2nd Sem Units Approved", 0.0, 30.0, 5.0)
        grade_2nd = st.number_input("2nd Sem Grade", 0.0, 20.0, 12.0)
        approved_1st = st.number_input("1st Sem Units Approved", 0.0, 30.0, 5.0)
        grade_1st = st.number_input("1st Sem Grade", 0.0, 20.0, 12.0)

    tuition_up_to_date = st.selectbox("Tuition Fees Up to Date?", [1, 0])
    scholarship = st.selectbox("Scholarship Holder?", [1, 0])
    debtor = st.selectbox("Debtor?", [1, 0])

    submit = st.form_submit_button("Prediksi")

# === Proses prediksi saat tombol submit diklik ===
if submit:
    data = pd.DataFrame([{
        "Application_mode": app_mode,
        "Course": course,
        "Gender": gender,
        "Previous_qualification": prev_qual,
        "Curricular_units_2nd_sem_approved": approved_2nd,
        "Curricular_units_2nd_sem_grade": grade_2nd,
        "Curricular_units_1st_sem_approved": approved_1st,
        "Curricular_units_1st_sem_grade": grade_1st,
        "Tuition_fees_up_to_date": tuition_up_to_date,
        "Scholarship_holder": scholarship,
        "Age_at_enrollment": age,
        "Debtor": debtor
    }])

    encoded = encode_input(data, encoder, important_categorical, important_numerical)
    pred = model.predict(encoded)[0]
    proba = model.predict_proba(encoded)[0][0]  # Probabilitas dropout (0)

    st.markdown("---")
    if pred == 0:
        st.error(f"❌ Mahasiswa diprediksi berpotensi **DROP OUT** dengan kemungkinan: **{proba:.2%}**")
    else:
        st.success(f"✅ Mahasiswa **TIDAK** diprediksi dropout. Kemungkinan bertahan: **{(1 - proba):.2%}**")
